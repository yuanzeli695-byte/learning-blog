import fs from 'node:fs';
import path from 'node:path';

const libraryRoot = path.resolve('python-code');

export type PythonEntry = {
  slug: string;
  title: string;
  topic: string;
  date: string;
  summary: string;
  notes: string[];
  code: string;
  file: string;
};

function walk(dir: string): string[] {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((item) => {
    const full = path.join(dir, item.name);
    if (item.isDirectory()) return walk(full);
    return item.isFile() && item.name.toLowerCase().endsWith('.py') ? [full] : [];
  });
}

export function getPythonEntries(): PythonEntry[] {
  if (!fs.existsSync(libraryRoot)) return [];

  return walk(libraryRoot).map((file) => {
    const relative = path.relative(libraryRoot, file).replaceAll(path.sep, '/');
    const slug = relative.replace(/\.py$/i, '');
    const metaPath = file.replace(/\.py$/i, '.json');
    const metadata = fs.existsSync(metaPath) ? JSON.parse(fs.readFileSync(metaPath, 'utf8').replace(/^\uFEFF/, '')) : {};
    const topic = relative.includes('/') ? relative.split('/')[0] : '未分类';

    if (metadata.notes !== undefined && (!Array.isArray(metadata.notes) || !metadata.notes.every((note: unknown) => typeof note === 'string'))) {
      throw new Error(`${metaPath}: notes 必须是字符串数组`);
    }

    return {
      slug,
      title: metadata.title || path.basename(file, '.py'),
      topic,
      date: metadata.date || '',
      summary: metadata.summary || '',
      notes: metadata.notes || [],
      code: fs.readFileSync(file, 'utf8').replace(/^\uFEFF/, ''),
      file: relative,
    };
  }).sort((a, b) => b.date.localeCompare(a.date) || a.file.localeCompare(b.file, 'zh-CN'));
}
