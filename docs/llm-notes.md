# 大模型学习专区

在线入口：`/llm/`。内容分为 **大模型基础**、**模型量化**、**推理加速** 三个类别，分别存放在：

```text
src/pages/llm/notes/fundamentals/
src/pages/llm/notes/quantization/
src/pages/llm/notes/inference/
```

暂时没有学习笔记时，三个类别显示空状态，不会虚构学习内容。

新增笔记：从 `templates/llm-note.md` 复制一份到对应类别文件夹，换成实际标题、日期、摘要和正文；文件名建议英文/数字/连字符。每篇 Markdown 的 `layout` 固定为 `../../../../layouts/LlmNoteLayout.astro`，`topic` 与所在目录一致。`npm run build` 会验证基本元数据、更新分类索引并生成文章页。不要直接把未核查的原始 Word 或 TXT 当作已发布文章；原始文件放 `input/`，先核对出处、事实和私密信息后再整理。

内容建议区分：读到的结论、个人理解、实验条件与结果、未验证的猜测。比较量化或推理速度时记录测试条件，避免只写一个加速倍数。
