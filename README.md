# Research Paper Archive 📚

A simple, fully static system to track, review, and search research papers.

- Write **one Markdown file per paper**.
- Auto-generate a **CSV** for Excel/Google Sheets.
- Get a **searchable web UI** hosted on **GitHub Pages**.
- No backend, no database, no embeddings, no RAG.

---

## Features

- 📝 **Markdown-based reviews**  
  Each paper is a Markdown file with YAML frontmatter for metadata and structured sections for notes.

- 🔎 **Client-side search**  
  Search by title, authors, field, method, tags, and note content directly in the browser.

- 📊 **CSV export**  
  All paper metadata is collected into `papers.csv`, ready for Excel/Google Sheets.

- 🌐 **Static hosting**  
  Entire system is static and runs on GitHub Pages. No servers or databases.


---


## How to Use (Your Workflow)

Every time you review a new paper:

1. **Create a new Markdown file**

   In `papers/`:
papers/bert-pretraining.md -> Use lowercase and hyphens instead of spaces.

2. **Copy the template**
Copy everything from `papers/template.md` into your new file.

3. **Fill in metadata and notes**
- Update the YAML frontmatter (title, authors, year, etc.).
- Write your summary, key insights, methodology, etc.

4. **Generate CSV and search data**

From the project root:

`pip install python-frontmatter` # first time only

```
python scripts/build_csv.py
python scripts/build_search.py
```

This updates:

- `papers.csv`
- `search-data.json`

5. **Commit and push**
```
git add .
git commit -m "Add review: BERT pretraining"
git push
```

6. **View on GitHub Pages**: 
After 1–2 minutes, your new paper appears on your site.

---

## GitHub Page: 
[https://revati-n.github.io/research-log/](https://revati-n.github.io/research-log/)

---

## Frontend (Search UI)

- `docs/index.html` is a single-page app:
- Loads `search-data.json` via `fetch`.
- Uses JavaScript and a fuzzy search library to match queries against:
 - title, authors, field, method, tags, and content.
- Renders a list of results with:
 - Title, authors, year, field, method.
 - Link to arXiv PDF.
 - Link to your Markdown notes in `papers/`.
- Also exposes a **Download CSV** button pointing to `/papers.csv`.

---

## Typical Update Cycle

- 📖 Read paper
- 📝 Create new .md in papers/
- ✍️ Fill metadata + notes
- 🐍 Run build_csv.py + build_search.py
- 🌐 git add . && git commit && git push
- ✅ Paper appears on GitHub Pages

---

## Notes
- This is designed to be:
  - **Simple**: just Markdown + Python + static HTML.
  - **Durable**: no external services, easy to back up.
  - **Portable**: CSV export lets you slice/dice your library anywhere.
