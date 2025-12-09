import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(repr(node), "TextNode(This is a text node, italic, None)")

    def test_link_node(self):
        node = TextNode("Click here", TextType.LINK, "http://example.com")
        self.assertEqual(node.text, "Click here")
        self.assertEqual(node.text_type.value, "link")
        self.assertEqual(node.url, "http://example.com")

if __name__ == "__main__":
    unittest.main()