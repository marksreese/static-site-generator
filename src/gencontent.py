import os
from block_markdown import markdown_to_html_node


def extract_title(doc: str):
    lines = doc.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found in document")

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for dir in os.listdir(dir_path_content):
        dir_path = os.path.join(dir_path_content, dir)
        if os.path.isdir(dir_path):
            generate_pages_recursive(dir_path, template_path, os.path.join(dest_dir_path, dir))
        elif dir.endswith(".md"):
            dest_file_name = dir[:-3] + ".html"
            dest_file_path = os.path.join(dest_dir_path, dest_file_name)
            generate_page(dir_path, template_path, dest_file_path)
