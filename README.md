# CS2305 Project 3 — 第 17 组

选题：**冯·诺依曼架构 vs 存算一体 / 近内存计算（Processing-in-Memory, PIM）**

一篇英文对比分析报告（LaTeX 单文件）+ 配套图表。本仓库即报告的全部源文件。

## 最快上手（Overleaf）
1. 下载本仓库里的 **`Group17_Project3_Overleaf.zip`**（扁平结构，文件都在压缩包根目录，没有外层文件夹）。
2. Overleaf（latex.sjtu.edu.cn）→ New Project → **Upload Project** → 选这个 zip。
3. 菜单里设 **Compiler = pdfLaTeX**、**Main document = `CS2305_submission.tex`** → Recompile。参考文献会自动跑 bibtex。

> 注意：**不要**用 GitHub 绿色按钮 *Code → Download ZIP*，那个会把文件套进一层子文件夹，传到 Overleaf 后主文件在子目录里、不够顺手。请用上面的 `Group17_Project3_Overleaf.zip`。

## 文件说明
| 文件 | 作用 |
|------|------|
| `CS2305_submission.tex` | 报告主文件（单文件；各章节用 `% [P1]`–`% [P4]` 标注归属） |
| `CS2305_submission.bib` | 参考文献（9 条，均含 DOI，已核对元数据） |
| `application_scenarios.pdf` | 第 4 节用到的应用场景图 |
| `make_application_figure.py` | 生成该图的脚本（Python / matplotlib） |
| `Group17_Project3_Overleaf.zip` | 打包好的、可直传 Overleaf 的扁平压缩包 |
| `CS2305_submission.sty/.bst`、`natbib.sty`、`fancyhdr.sty`、`math_commands.tex` | 模板支持文件（不要改） |

## 给组员的提醒
- 把 `.tex` 里每个 `\textit{[P… outline …]}` 占位段替换成正式英文正文；各节字数尽量贴近预算（见 `.tex` 顶部注释）。
- **正文（Abstract + 各章节，不含 References 与 Appendix）最终须 ≤ 2000 词。**
- **提交前所有参考文献务必去 Google Scholar 逐条核对** —— 作业不允许直接使用 AI 给出的文献。
- 改完源文件后，仓库里的 zip 不会自动更新，需要重新打包再提交（可让维护者用一条 `zip` 命令重建）。
