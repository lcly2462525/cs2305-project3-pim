# Group 17 — Project 3 (Overleaf upload)

Topic: **Von Neumann Architecture vs. Processing-in-Memory (PIM)**

## Quickest start (Overleaf)
1. Download **`Group17_Project3_Overleaf.zip`** from this repo (it is flat — files
   sit at the zip root, no wrapper folder).
2. Overleaf → New Project → **Upload Project** → select that zip.
3. Menu → **Compiler = pdfLaTeX**, **Main document = `CS2305_submission.tex`** →
   Recompile. Bibliography is handled automatically (bibtex).

> Tip: do **not** use GitHub's green *Code → Download ZIP*; that wraps everything
> in a sub-folder. Use the `Group17_Project3_Overleaf.zip` above instead.

## Files
| File | Role |
|------|------|
| `CS2305_submission.tex` | Main report (single file; sections marked `% [P1]`–`% [P4]`) |
| `CS2305_submission.bib` | References (9 verified entries, with DOIs) |
| `application_scenarios.pdf` | Figure used in Section 4 |
| `make_application_figure.py` | Script that generates the figure (Python/matplotlib) |
| `CS2305_submission.sty/.bst`, `natbib.sty`, `fancyhdr.sty`, `math_commands.tex` | Template support files (do not edit) |

## Notes for the team
- Replace each `\textit{[P… outline …]}` placeholder with real prose; keep each
  section near its word budget (see comments at the top of the `.tex`).
- **Main body (Abstract + Sections, excluding References & Appendix) must stay
  ≤ 2000 words.**
- **Verify every reference on Google Scholar before submission** — AI-supplied
  references are not allowed.
