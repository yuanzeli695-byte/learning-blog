import fs from 'node:fs';
import path from 'node:path';

const libraryRoot = path.resolve('python-code');

export type PythonSection = {
  title: string;
  intro: string;
  file: string;
  code: string;
};

export type PythonEntry = {
  slug: string;
  title: string;
  topic: string;
  date: string;
  summary: string;
  source: string;
  notes: string[];
  sections: PythonSection[];
};

function walk(dir: string): string[] {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((item) => {
    const full = path.join(dir, item.name);
    if (item.isDirectory()) return walk(full);
    return item.isFile() && item.name.endsWith('.json') ? [full] : [];
  });
}

export function getPythonEntries(): PythonEntry[] {
  if (!fs.existsSync(libraryRoot)) return [];

  return walk(libraryRoot).map((manifest) => {
    const metadata = JSON.parse(fs.readFileSync(manifest, 'utf8').replace(/^\uFEFF/, ''));
    const relative = path.relative(libraryRoot, manifest).replaceAll(path.sep, '/');
    const slug = relative.replace(/\.json$/, '');
    const topic = relative.split('/')[0];
    const chapterDir = path.resolve(path.dirname(manifest), path.basename(manifest, '.json'));

    if (!Array.isArray(metadata.sections) || !metadata.sections.length) {
      throw new Error(`${manifest}: 需要至少一个 sections 条目`);
    }

    const sections = metadata.sections.map((section: { title: string; intro: string; file: string }) => {
      if (!section.title || !section.intro || typeof section.file !== 'string' || !section.file.endsWith('.py')) {
        throw new Error(`${manifest}: 每段需要 title、intro 和 .py file`);
      }
      const source = path.resolve(chapterDir, section.file);
      if (!source.startsWith(chapterDir + path.sep) || !fs.existsSync(source)) {
        throw new Error(`${manifest}: 不存在或越界的代码文件 ${section.file}`);
      }
      return { title: section.title, intro: section.intro, file: section.file, code: fs.readFileSync(source, 'utf8').replace(/^\uFEFF/, '') };
    });

    return {
      slug,
      title: String(metadata.title || path.basename(manifest, '.json')),
      topic,
      date: String(metadata.date || ''),
      summary: String(metadata.summary || ''),
      source: String(metadata.source || ''),
      notes: Array.isArray(metadata.notes) ? metadata.notes : [],
      sections,
    };
  }).sort((a, b) => b.date.localeCompare(a.date) || a.slug.localeCompare(b.slug, 'zh-CN'));
}
