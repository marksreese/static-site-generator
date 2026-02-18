import unittest
from block_markdown import *

class TestMarkdownBlocks(unittest.TestCase):
    def test_extract_blocks_from_markdown(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("- First item\n- Second item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("```\nCode block\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

    