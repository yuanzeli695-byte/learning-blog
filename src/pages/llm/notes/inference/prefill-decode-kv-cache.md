---
layout: ../../../../layouts/LlmNoteLayout.astro
title: "Prefill、Decode 与 KV Cache"
date: 2026-09-27
description: "分清提示词处理与逐 token 生成，并估算 KV Cache 的基础容量。"
topic: inference
order: 10
---

> 这篇记录的是推理流程和缓存的**理论估算**，不是本机的速度或显存实测。它不讨论训练时的梯度与优化器更新。

## 自回归生成：为什么要逐步输出

生成第一个新 token 后，第二个新 token 要以先前内容（包括刚生成的 token）为条件。因此**同一条序列的新 token 通常按顺序生成**；不同请求可以组成 batch 一起处理。这与训练时已知整段目标文本、可以并行计算多个位置的损失不同。

## Prefill：处理已有提示词

已有的提示词 token 可以在一次或分块的前向计算中处理；因果掩码保证每个位置只看得到允许的上下文。推理实现通常会在这一阶段建立提示词对应的 K/V 缓存。长提示词可能采用**分块 prefill**，并不要求无论多长都一次送完。

## Decode：逐个生成新 token

接下来每一步根据当前上下文预测一个新 token，再把它加入后续步骤的上下文。若每步都重新计算所有前文位置的 K/V，会做重复工作；**KV Cache 保存各层已处理位置的 K 和 V**，让下一步复用。新 token 的 K/V 也会加入缓存。缓存减少重复计算，却会随着已缓存 token 数量增加而占用更多内存。

## KV Cache 的基础容量估算

若 batch 中每条序列都缓存 `T` 个 token，各层头数与头维度一致，未考虑分页预留、对齐和其他中间状态，则 K/V **数据本体**的字节数为：

```text
KV bytes = 2 × B × T × L × H_KV × d_head × b
```

- `2`：每个位置存 K 和 V 两份；
- `B`：序列数（batch size）；
- `T`：每条序列中已缓存的 token 数，含提示词和已处理的生成 token；
- `L`：Transformer 层数；
- `H_KV`：每层的 K/V 头数，**不是查询头数**；
- `d_head`：每个 K/V 头的维度；
- `b`：每个缓存元素占用的字节数，例如 BF16 为 2 字节。

以官方 Qwen3-8B 配置的 `L=36`、`H_KV=8`、`d_head=128` 为例，若 `B=1`、`T=1024`、KV 元素按 BF16 的 2 字节存储：

```text
2 × 1 × 1024 × 36 × 8 × 128 × 2
= 150,994,944 字节 = 144 MiB
```

这个结果**只估算理想情况下的 KV 张量本体**，不包含模型权重、激活、分配器与分页开销等，不能当作整模型的显存占用。若不同请求的长度不一样，实际有效 token 的估算应对各序列长度求和；实际分配量还取决于实现和预留策略。

## 待实践验证

目前还没有记录本机的 prefill 延迟、decode 吞吐或显存曲线。之后若做对比，需要同时记下模型版本、精度、输入/输出长度、batch 大小、硬件和测量方式，避免仅凭一个数字判断加速效果。

参考：[Hugging Face KV Cache 说明](https://huggingface.co/docs/transformers/cache_explanation)、[Hugging Face 连续批处理架构中的 Prefill/Decode](https://huggingface.co/docs/transformers/continuous_batching_architecture)、[Qwen3-8B 官方配置](https://huggingface.co/Qwen/Qwen3-8B/blob/main/config.json)。
