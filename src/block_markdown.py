from enum import Enum

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

