from enum import Enum
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
    # check if block starts with 1 to 6 # symbols followed by a space
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{i + 1}. ") for i, line in enumerate(block.split("\n"))):
        return BlockType.ORDERED_LIST
    elif all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    else:
        return BlockType.PARAGRAPH