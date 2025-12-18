import frontmatter
from pathlib import Path
import markdown

def build_html_pages():
    papers_dir = Path("papers")
    output_dir = Path("paper-pages")
    output_dir.mkdir(exist_ok=True)
    
    for md_file in papers_dir.glob("*.md"):
        if md_file.name == "template.md":
            continue
        
        post = frontmatter.load(md_file)
        
        # Convert markdown content to HTML
        html_content = markdown.markdown(post.content)
        
        # Create HTML page
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{post.get('title', 'Paper')}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.6;
        }}
        h1, h2, h3 {{ color: #333; }}
        .meta {{ color: #666; margin-bottom: 30px; }}
        a {{ color: #667eea; }}
    </style>
</head>
<body>
    <h1>{post.get('title', 'Untitled')}</h1>
    <div class="meta">
        <strong>{post.get('authors', '')}</strong> • {post.get('year', '')} • {post.get('field', '')}<br>
        <a href="{post.get('arxiv', '#')}" target="_blank">📄 arXiv PDF</a>
    </div>
    {html_content}
    <br><br>
    <a href="../">← Back to Archive</a>
</body>
</html>"""
        
        # Save HTML file
        output_file = output_dir / f"{md_file.stem}.html"
        output_file.write_text(html, encoding='utf-8')
    
    print(f"✓ Generated HTML pages in {output_dir}/")

if __name__ == "__main__":
    build_html_pages()
