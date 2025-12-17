import json
import frontmatter
from pathlib import Path

def build_search_index():
    papers_dir = Path("papers")
    output_file = Path("search-data.json")
        
    search_data = []
    
    # Read all markdown files
    for md_file in sorted(papers_dir.glob("*.md")):
        if md_file.name == "template.md":
            continue
            
        try:
            post = frontmatter.load(md_file)
            
            # Extract searchable content
            content_text = post.content.strip()
            
            # Create search entry
            entry = {
                'filename': md_file.name,
                'title': post.get('title', ''),
                'authors': post.get('authors', ''),
                'year': post.get('year', ''),
                'field': post.get('field', ''),
                'method': post.get('method', ''),
                'arxiv': post.get('arxiv', ''),
                'tags': post.get('tags', []),
                'content': content_text[:500],  # First 500 chars for preview
                'date_reviewed': post.get('date_reviewed', ''),
            }
            
            search_data.append(entry)
            
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    # Write to JSON
    with open(output_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(search_data, jsonfile, indent=2, ensure_ascii=False)
    
    print(f"✓ Generated {output_file} with {len(search_data)} papers")

if __name__ == "__main__":
    build_search_index()
