# 沅泽的学习博客

这是一个使用 Astro + Markdown 构建的个人学习博客。

## 本地运行

```powershell
npm install
npm run dev
```

浏览器打开终端显示的本地地址即可。

## 导入学习笔记

把 `.txt` 或 `.docx` 文件放入 `input/`，然后运行：

```powershell
npm run import:note -- input\2026-09-23-Python函数学习.docx
npm run build
```

脚本会：

1. 读取笔记内容；
2. 生成 `src/pages/posts/` 下的 Markdown 文章；
3. 将原始文件复制到 `archive/original/`；
4. 构建时自动更新文章索引。

`input/` 和 `archive/original/` 默认不会被提交到公开仓库，避免原始资料意外公开。

## 发布到 GitHub Pages

1. 在 GitHub 创建一个空仓库；
2. 将本地仓库 remote 设置为你的 GitHub 地址；
3. 推送到 `main` 分支；
4. 在仓库 Settings → Pages → Build and deployment 中选择 **GitHub Actions**；
5. 等待 `.github/workflows/deploy.yml` 执行完成。

项目站点默认地址：

```text
https://你的用户名.github.io/仓库名/
```

如果使用自定义域名，需要同步修改 `astro.config.mjs` 中的 `SITE_URL`，并按 GitHub Pages 的域名配置增加 `public/CNAME`。

## 目录说明

- `input/`：待导入的原始笔记
- `src/pages/posts/`：已发布的 Markdown 文章
- `archive/original/`：原始 Word/text 归档
- `scripts/`：笔记导入和文章索引脚本
- `.github/workflows/deploy.yml`：自动部署配置
