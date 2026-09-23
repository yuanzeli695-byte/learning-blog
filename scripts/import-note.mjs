import fs from 'node:fs';
import path from 'node:path';
import mammoth from 'mammoth';

const input = process.argv[2];
if (!input) {
  console.error('用法: npm run import:note -- input/你的笔记.docx');
  process.exit(1);
}

const inputPath = path.resolve(input);
if (!fs.existsSync(inputPath)) {
  console.error(`找不到文件: ${inputPath}`);
  process.exit(1);
}

const ext = path.extname(inputPath).toLowerCase();
if (!['.txt', '.docx'].includes(ext)) {
  console.error('只支持 .txt 和 .docx 文件。');
  process.exit(1);
}

const localDate = new Intl.DateTimeFormat('en-CA', {
  timeZone: 'Asia/Shanghai', year: 'numeric', month: '2-digit', day: '2-digit',
}).format(new Date());
const dateMatch = path.basename(inputPath).match(/20\d{2}[-年]\d{1,2}[-月]\d{1,2}/);
const date = dateMatch ? dateMatch[0].replaceAll('年', '-').replaceAll('月', '-').replaceAll('日', '').replace(/-(\d)(?!\d)/g, '-0$1') : localDate;
const rawName = path.basename(inputPath, ext).replace(/^20\d{2}[-年]\d{1,2}[-月]\d{1,2}[-_ ]*/, '').trim();

let text;
if (ext === '.docx') {
  const result = await mammoth.extractRawText({ path: inputPath });
  text = result.value;
} else {
  text = fs.readFileSync(inputPath, 'utf8');
}

text = text.replace(/^\uFEFF/, '').replace(/\r\n/g, '\n').trim();
const paragraphs = text.split(/\n{2,}/).map((part) => part.trim()).filter(Boolean);
const firstLine = text.split('\n').map((line) => line.trim()).find(Boolean);
const title = rawName || firstLine || '未命名学习记录';
const slugBase = title
  .toLowerCase()
  .replace(/[^a-z0-9]+/g, '-')
  .replace(/^-+|-+$/g, '') || 'learning-note';
let slug = `${date}-${slugBase}`;
const postsDir = path.resolve('src/pages/posts');
fs.mkdirSync(postsDir, { recursive: true });
let index = 2;
while (fs.existsSync(path.join(postsDir, `${slug}.md`))) slug = `${date}-${slugBase}-${index++}`;

const body = paragraphs.length ? paragraphs.map((paragraph) => paragraph.split('\n').join('  \n')).join('\n\n') : '（原始笔记为空，请补充内容。）';
const markdown = `---\nlayout: ../../layouts/PostLayout.astro\ntitle: "${title.replaceAll('"', '\\"')}"\ndate: ${date}\ntags:\n  - 学习记录\ncategory: "学习记录"\ndescription: "${title.replaceAll('"', '\\"')}的学习记录。"\n---\n\n${body}\n`;
const outputPath = path.join(postsDir, `${slug}.md`);
fs.writeFileSync(outputPath, markdown, 'utf8');

const archiveDir = path.resolve('archive/original');
fs.mkdirSync(archiveDir, { recursive: true });
fs.copyFileSync(inputPath, path.join(archiveDir, path.basename(inputPath)));
console.log(`已生成: ${outputPath}`);
console.log(`原文归档: ${path.join(archiveDir, path.basename(inputPath))}`);

