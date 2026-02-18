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
    for img_text, url in matches:
        images.append((img_text, url))
    return images

def extract_markdown_links(text: str):
    # pattern ignores leading exclamation marks which indicate images with (?<!!)
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    links = []
    for link_text, url in matches:
        links.append((link_text, url))
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

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            result.append(node)
            continue
        current_sublist = []
        remaining_text = node.text
        for text, url in images:
            split_text = remaining_text.split(f"![{text}]({url})", 1)
            if split_text[0] != "":
                current_sublist.append(TextNode(split_text[0], TextType.TEXT))
            current_sublist.append(TextNode(text, TextType.IMAGE, url))
            remaining_text = split_text[1]
        if remaining_text != "":
            current_sublist.append(TextNode(remaining_text, TextType.TEXT))
        result.extend(current_sublist)
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            result.append(node)
            continue
        current_sublist = []
        remaining_text = node.text
        for text, url in links:
            split_text = remaining_text.split(f"[{text}]({url})", 1)
            if split_text[0] != "":
                current_sublist.append(TextNode(split_text[0], TextType.TEXT))
            current_sublist.append(TextNode(text, TextType.LINK, url))
            remaining_text = split_text[1]
        if remaining_text != "":
            current_sublist.append(TextNode(remaining_text, TextType.TEXT))
        result.extend(current_sublist)
    return result

# use split functions to convert text in a block to textnodes with correct types
def text_to_textnodes(text: str):
    result = []
    initial_node = TextNode(text, TextType.TEXT)
    result.append(initial_node)
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    result = split_nodes_delimiter(result, "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    return result