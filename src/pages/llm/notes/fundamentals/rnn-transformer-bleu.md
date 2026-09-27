---
layout: ../../../../layouts/LlmNoteLayout.astro
title: "从 RNN、卷积到 Transformer：多头注意力与 BLEU"
date: 2026-09-27
description: "理清循环与卷积的历史语境、Transformer 的多头注意力，以及 BLEU 的评价边界。"
topic: fundamentals
order: 60
---

> 这是一份术语关系笔记，不是模型复现或机器翻译测评报告。更细的 Q/K/V 与 MLP 分工见[《Transformer 层：注意力与前馈网络》](../transformer-layer/)。

## Recurrence and convolutions 指什么

在序列建模的历史语境里，**recurrence** 是循环递推（如 RNN），**convolutions** 是通过卷积操作建模局部或多层上下文。Transformer 原论文提出以注意力为核心的架构，**不使用循环或卷积来构成其提出的编码器/解码器主结构**，从而让训练时的序列位置计算更易并行。这里说的是原论文架构，不等于“所有叫 Transformer 的变体都不含卷积”，也不等于生成一个新 token 时能无依赖地同时知道后面所有生成结果。

## 多头注意力为什么不只一个头

单头注意力得到一组对可见位置的加权信息；**多头注意力**对输入做多组可训练投影，各头分别计算注意力，再合并结果。不同头有机会关注不同关系或表示子空间，但不能保证每个头都能被稳定解释为一个单独的自然语言概念。其 Q、K、V 如何计算，参见同专区的 Transformer 层笔记。

## BLEU 是什么，不是什么

**BLEU** 是机器翻译等生成任务中提出的一种自动评价方法：它根据候选译文和参考译文之间的多元词组（n-gram）重合情况，并加上长度惩罚来计算分数。它能提供一种可重复的比较信号，却**不能独自证明译文流畅、事实正确或语义完全一致**；不同参考答案或分词方式也会影响解释。这里没有任何模型的 BLEU 实测结果。

## 把几个名词放在一起

```text
词/token 向量 → 序列建模
  ├─ RNN：按时间步递推隐藏状态
  ├─ 卷积式模型：以卷积组合局部信息
  └─ Transformer：用多头注意力交互位置表示

BLEU：评价生成文本与参考文本的一种指标，不是模型结构
```

参考：[Attention Is All You Need 原论文](https://arxiv.org/abs/1706.03762)、[BLEU 原论文（ACL Anthology）](https://aclanthology.org/P02-1040/)。
