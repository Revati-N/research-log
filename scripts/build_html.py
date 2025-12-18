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
            font-family: 'Georgia', 'Times New Roman', serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.8;
            background: linear-gradient(135deg, #D4C5B9 0%, #C9B8A8 50%, #B8A594 100%);
            min-height: 90vh;
        }}
        
        .container {{
            background: #F5F0E8;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(61, 53, 49, 0.15);
            border: 1px solid #C9B8A8;
        }}
        
        h1 {{
            color: #3D3531;
            font-size: 2.2rem;
            margin-bottom: 20px;
            font-weight: 350;
            letter-spacing: 0.5px;
            border-bottom: 2px solid #B0CCCB;
            padding-bottom: 15px;
        }}
        
        h2 {{
            color: #4A7A7C;
            font-size: 1.6rem;
            margin-top: 30px;
            margin-bottom: 15px;
            font-weight: 500;
        }}
        
        h3 {{
            color: #5A5147;
            font-size: 1.3rem;
            margin-top: 25px;
            margin-bottom: 12px;
        }}
        
        p {{
            color: #3D3531;
            margin-bottom: 15px;
        }}
        
        .meta {{
            color: #5A5147;
            margin-bottom: 30px;
            padding: 15px;
            background: rgba(176, 204, 203, 0.2);
            border-radius: 8px;
            border-left: 4px solid #4A7A7C;
        }}
        
        a {{
            color: #4A7A7C;
            text-decoration: none;
            border-bottom: 2px solid transparent;
            transition: all 0.3s;
            font-weight: 600;
        }}
        
        a:hover {{
            border-bottom-color: #4A7A7C;
            color: #5A8A8C;
        }}
        
        .back-link {{
            display: inline-block;
            margin-top: 30px;
            padding: 10px 20px;
            background: #4A7A7C;
            color: #FFFCF7;
            border-radius: 8px;
            border: 2px solid #4A7A7C;
            transition: all 0.3s;
        }}
        
        .back-link:hover {{
            background: #5A8A8C;
            border-color: #5A8A8C;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(74, 122, 124, 0.3);
            border-bottom: 2px solid #5A8A8C;
        }}
        
        code {{
            background: #E8DED3;
            padding: 2px 6px;
            border-radius: 4px;
            color: #3D3531;
            font-family: 'Consolas', 'Monaco', monospace;
        }}
        
        pre {{
            background: #E8DED3;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            border: 1px solid #C9B8A8;
        }}
        
        pre code {{
            background: none;
        }}
        
        ul, ol {{
            color: #3D3531;
            margin-bottom: 15px;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        blockquote {{
            border-left: 4px solid #B0CCCB;
            padding-left: 20px;
            margin: 20px 0;
            color: #5A5147;
            font-style: italic;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{post.get('title', 'Untitled')}</h1>
        <div class="meta">
            <strong>{post.get('authors', '')}</strong> • {post.get('year', '')} • {post.get('field', '')}<br>
            <a href="{post.get('arxiv', '#')}" target="_blank">📄 arXiv PDF</a>
        </div>
        {html_content}
        <br><br>
        <a href="../" class="back-link">← Back to Archive</a>
    </div>
</body>
</html>"""
        
        # Save HTML file
        output_file = output_dir / f"{md_file.stem}.html"
        output_file.write_text(html, encoding='utf-8')
    
    print(f"✓ Generated HTML pages in {output_dir}/")


if __name__ == "__main__":
    build_html_pages()
