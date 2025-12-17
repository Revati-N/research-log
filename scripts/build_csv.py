import os
import csv
import frontmatter
from pathlib import Path

def build_csv():
    papers_dir = Path("papers")
    output_file = Path("papers.csv")
    
    papers_data = []
    
    # Read all markdown files
    for md_file in sorted(papers_dir.glob("*.md")):
        if md_file.name == "template.md":
            continue
            
        try:
            post = frontmatter.load(md_file)
            
            # Extract metadata
            metadata = {
                'filename': md_file.name,
                'title': post.get('title', ''),
                'authors': post.get('authors', ''),
                'year': post.get('year', ''),
                'field': post.get('field', ''),
                'method': post.get('method', ''),
                'arxiv': post.get('arxiv', ''),
                'tags': ', '.join(post.get('tags', [])),
                'date_reviewed': post.get('date_reviewed', ''),
            }
            
            papers_data.append(metadata)
            
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    # Write to CSV
    if papers_data:
        fieldnames = ['filename', 'title', 'authors', 'year', 'field', 
                     'method', 'arxiv', 'tags', 'date_reviewed']
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(papers_data)
        
        print(f"✓ Generated {output_file} with {len(papers_data)} papers")
    else:
        print("No papers found to process")

if __name__ == "__main__":
    build_csv()
