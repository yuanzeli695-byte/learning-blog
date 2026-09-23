import fs from 'node:fs';
import path from 'node:path';

const postsDir = path.resolve('src/pages/posts');
const outputPath = path.resolve('src/data/posts.json');

function parseFrontmatter(filePath) {
  const source = fs.readFileSync(filePath, 'utf8').replace(/^\uFEFF/, '');
  const match = source.match(/^---\s*\n([\s\S]*?)\n---/);
  const frontmatter = match?.[1] || '';
  const read = (key, fallback = '') => {
    const line = frontmatter.match(new RegExp(`^${key}:\\s*(.*)$`, 'm'));
    return line ? line[1].trim().replace(/^['"]|['"]$/g, '') : fallback;
  };
  const tagsLine = frontmatter.match(/^tags:\s*\n((?:\s+-\s+.*\n?)+)/m);
  const tags = tagsLine ? [...tagsLine[1].matchAll(/^\s+-\s+(.+)$/gm)].map((m) => m[1].trim().replace(/^['"]|['"]$/g, '')) : [];
  const relative = path.relative(postsDir, filePath).replaceAll(path.sep, '/');
  const slug = relative.replace(/\.md$/, '');
  return {
    slug,
    url: `posts/${slug}/`,
    title: read('title', slug),
    date: read('date', '1970-01-01'),
    description: read('description', '学习记录。'),
    category: read('category', '学习记录'),
    tags,
  };
}

function walk(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const full = path.join(dir, entry.name);
    return entry.isDirectory() ? walk(full) : full.endsWith('.md') ? [full] : [];
  });
}

const posts = walk(postsDir)
  .map(parseFrontmatter)
  .sort((a, b) => b.date.localeCompare(a.date) || a.title.localeCompare(b.title, 'zh-CN'));

fs.writeFileSync(outputPath, JSON.stringify({ posts }, null, 2) + '\n', 'utf8');
console.log(`Indexed ${posts.length} post(s).`);
