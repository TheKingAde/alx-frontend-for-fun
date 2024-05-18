#!/usr/bin/python3
"""
markdown2html module
Converts a markdown file to HTML.
"""

import sys
import os

def convert_markdown_to_html(markdown_file, html_file):
    """
    Converts the content of a markdown file to HTML and writes to an output file.
    """
    # Simple Markdown to HTML conversion
    replacements = [
        ("#", "<h1>", "</h1>"),
        ("##", "<h2>", "</h2>"),
        ("###", "<h3>", "</h3>"),
        ("####", "<h4>", "</h4>"),
        ("#####", "<h5>", "</h5>"),
        ("######", "<h6>", "</h6>"),
        ("*", "<ul><li>", "</li></ul>")
    ]

    try:
        with open(markdown_file, 'r') as md_file:
            with open(html_file, 'w') as html_file:
                for line in md_file:
                    line = line.strip()
                    for md, start_tag, end_tag in replacements:
                        if line.startswith(md):
                            line = line.replace(md, start_tag, 1) + end_tag
                            break
                    html_file.write(line + '\n')
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(markdown_file, html_file)
    sys.exit(0)
