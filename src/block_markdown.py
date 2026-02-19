from enum import Enum
from htmlnode import ParentNode
from textnode import *
from inline_markdown import text_to_textnodes
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    ORDERED_LIST = "ordered_list"
    UNORDERED_LIST = "unordered_list"
    QUOTE = "quote"
    CODE = "code"

def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    filtered = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered.append(block)
    return filtered

def block_to_block_type(block: str):
    lines = block.split("\n")
    # check if block starts with 1 to 6 # symbols followed by a space
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif block.startswith("- "):
        if all(line.startswith("- ") for line in lines):
            return BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        if all(lines[i].startswith(f"{i + 1}. ") for i in range(len(lines))):
            return BlockType.ORDERED_LIST
    elif block.startswith(">"):
        if all(line.startswith(">") for line in lines):
            return BlockType.QUOTE
    elif len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    else:
        return BlockType.PARAGRAPH
    
# uses text_to_textnodes and text_node_to_html_node to convert a block of markdown text into a list of LeafNodes
def text_to_children(block: str, block_type = BlockType.PARAGRAPH):
    if block_type == BlockType.UNORDERED_LIST:
        block = "".join("<li>" + line[2:] + "</li>" for line in block.split("\n"))
    elif block_type == BlockType.ORDERED_LIST:
        block = "".join(re.sub(r"^\d+\. ", "<li>", line + "</li>") for line in block.split("\n"))
    elif block_type == BlockType.HEADING:
        block = re.sub(r"^#{1,6} ", "", block, 1)
    elif block_type == BlockType.QUOTE:
        block = "\n".join(line.lstrip("> ") for line in block.split("\n"))
    elif block_type == BlockType.PARAGRAPH:
        block.replace("\n", " ")
    elif block_type == BlockType.CODE:
        raise Exception("Code blocks should not be handled by text_to_children()")
    else:
        raise Exception(f"Unknown block type: {block_type}")
    text_nodes = text_to_textnodes(block)
    return [text_node_to_html_node(node) for node in text_nodes]

def block_type_to_tag(block_type):
    if block_type == BlockType.PARAGRAPH:
        return "p"
    elif block_type == BlockType.CODE:
        return "code"
    elif block_type == BlockType.QUOTE:
        return "blockquote"
    elif block_type == BlockType.ORDERED_LIST:
        return "ol"
    elif block_type == BlockType.UNORDERED_LIST:
        return "ul"
    elif block_type == BlockType.HEADING:
        return "h"
    else:
        raise ValueError(f"Unknown block type: {block_type}")
    
def markdown_to_html_node(doc: str):
    blocks = markdown_to_blocks(doc)
    node = ParentNode("div", [])
    for block in blocks:
        block_type = block_to_block_type(block)
        tag = block_type_to_tag(block_type) # type: ignore
        if tag == "h":
            # count number of # symbols at the start of the block
            num_hashes = len(block) - len(block.lstrip("#").lstrip()) - 1
            tag = f"h{num_hashes}"
        # create new child of <div></div>
        block_node = ParentNode(tag, []) # type: ignore
        node.children.append(block_node)
        # set nested children
        if block_type != BlockType.CODE:
            block_node.children.extend(text_to_children(block, block_type)) # type: ignore
        else:
            pre_node = ParentNode("pre", [])
            new_textnode = TextNode(block.lstrip("`\n").rstrip("`"), TextType.TEXT)
            inner_node = text_node_to_html_node(new_textnode)
            pre_node.children.append(inner_node)
            block_node.children.append(pre_node)
    return node