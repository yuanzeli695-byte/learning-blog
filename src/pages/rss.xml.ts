import posts from '../data/posts.json';

const escapeXml = (value) => String(value)
  .replaceAll('&', '&amp;')
  .replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;')
  .replaceAll("'", '&apos;');

export const GET = ({ site }) => {
  const origin = site?.toString().replace(/\/$/, '') || 'https://example.com';
  const items = posts.posts.map((post) => `
    <item>
      <title>${escapeXml(post.title)}</title>
      <link>${origin}/${post.url}</link>
      <guid>${origin}/${post.url}</guid>
      <pubDate>${new Date(`${post.date}T00:00:00+08:00`).toUTCString()}</pubDate>
      <description>${escapeXml(post.description)}</description>
    </item>`).join('');
  const xml = `<?xml version="1.0" encoding="UTF-8" ?>
  <rss version="2.0"><channel>
    <title>沅泽的学习博客</title>
    <link>${origin}</link>
    <description>记录学习、实践与复盘。</description>${items}
  </channel></rss>`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
