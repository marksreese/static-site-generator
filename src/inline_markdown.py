from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter: str, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        current_sublist = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid markdown, unclosed section found")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                current_sublist.append(TextNode(sections[i], TextType.TEXT))
            else:
                current_sublist.append(TextNode(sections[i], text_type))
        result.extend(current_sublist)
    return result

def extract_markdown_images(text: str):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    images = []
    for text, url in matches:
        images.append((text, url))
    return images

def extract_markdown_links(text: str):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    links = []
    for text, url in matches:
        links.append((text, url))
    return links

def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    filtered = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered.append(block)
    return filtered