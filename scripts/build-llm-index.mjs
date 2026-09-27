import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve('src/pages/llm/notes');
const output = path.resolve('src/data/llm-notes.json');
const topics = {
  fundamentals: '大模型基础',
  quantization: '模型量化',
  inference: '推理加速',
};

function readMetadata(file, topic) {
  const text = fs.readFileSync(file, 'utf8').replace(/^\uFEFF/, '');
  const match = text.match(/^---\s*\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/);
  if (!match) throw new Error(`${file}: 缺少 YAML frontmatter`);
  const fields = Object.fromEntries(
    match[1].split(/\r?\n/).filter(Boolean).map((line) => {
      const parts = line.match(/^([a-zA-Z]+):\s*(.*)$/);
      if (!parts) throw new Error(`${file}: 仅支持一行一个键值，不支持嵌套 YAML`);
      let value = parts[2].trim();
      if (value.startsWith('"')) value = JSON.parse(value);
      else value = value.replace(/^'|'$/g, '');
      return [parts[1], value];
    }),
  );
  for (const key of ['title', 'date', 'description']) {
    if (!fields[key] || typeof fields[key] !== 'string') throw new Error(`${file}: 必须填写 ${key}`);
  }
  if (!/^\d{4}-\d{2}-\d{2}$/.test(fields.date) || new Date(`${fields.date}T00:00:00Z`).toISOString().slice(0, 10) !== fields.date) {
    throw new Error(`${file}: date 必须是 YYYY-MM-DD`);
  }
  if (fields.topic !== topic) throw new Error(`${file}: topic 必须与所在目录 ${topic} 一致`);
  if (fields.layout !== '../../../../layouts/LlmNoteLayout.astro') {
    throw new Error(`${file}: layout 必须是 ../../../../layouts/LlmNoteLayout.astro`);
  }
  const order = fields.order === undefined ? null : Number(fields.order);
  if (order !== null && (!Number.isInteger(order) || order < 0)) throw new Error(`${file}: order 必须是非负整数`);
  const slug = path.basename(file, '.md');
  return {
    title: fields.title,
    date: fields.date,
    description: fields.description,
    topic,
    topicLabel: topics[topic],
    order,
    url: `llm/notes/${topic}/${slug}/`,
  };
}

const notes = Object.keys(topics).flatMap((topic) => {
  const dir = path.join(root, topic);
  return fs.readdirSync(dir, { withFileTypes: true })
    .filter((entry) => entry.isFile() && entry.name.endsWith('.md') && !entry.name.startsWith('_'))
    .map((entry) => readMetadata(path.join(dir, entry.name), topic));
}).sort((a, b) => b.date.localeCompare(a.date) || (a.order ?? Number.MAX_SAFE_INTEGER) - (b.order ?? Number.MAX_SAFE_INTEGER) || a.title.localeCompare(b.title, 'zh-CN'));

fs.writeFileSync(output, JSON.stringify({ notes }, null, 2) + '\n', 'utf8');
console.log(`Indexed ${notes.length} LLM learning note(s).`);
