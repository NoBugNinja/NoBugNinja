import json

def sync():
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()
    
    with open("preview_readme.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    marker_start = "const md = "
    marker_end = ";\n    document.getElementById('content')"

    start_idx = html_content.find(marker_start)
    end_idx = html_content.find(marker_end)

    if start_idx != -1 and end_idx != -1:
        new_html = html_content[:start_idx + len(marker_start)] + json.dumps(readme_content) + html_content[end_idx:]
        with open("preview_readme.html", "w", encoding="utf-8") as f:
            f.write(new_html)
        print("Successfully synced preview_readme.html with README.md")
    else:
        print("Markers not found in preview_readme.html")

if __name__ == "__main__":
    sync()
