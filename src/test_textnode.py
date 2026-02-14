import unittest

from textnode import TextNode, TextType
from utility import split_nodes_delimiter

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

    # def test_delimiter_singleline(self):

    #     self.assertEqual
    
    def test_delimiter_multiline(self):
        nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("*bold*", TextType.TEXT),
            TextNode(" and ", TextType.TEXT),
            TextNode("*italic*", TextType.TEXT),
            TextNode(" text.", TextType.TEXT),
        ]

        result = split_nodes_delimiter(nodes, "*", TextType.BOLD)

        expected = [
            TextNode("This is ", TextType.TEXT, None),
            TextNode("bold", TextType.BOLD, None),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("italic", TextType.BOLD, None),
            TextNode(" text.", TextType.TEXT, None),
        ]

        self.assertEqual(result, expected)

    def test_unpaired_delimiter(self):
        nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("*bold and italic", TextType.TEXT),
            TextNode(" text.", TextType.TEXT),
        ]

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(nodes, "*", TextType.BOLD)

        self.assertTrue("Unpaired delimiter found in nodes." in str(context.exception))

if __name__ == "__main__":
    unittest.main()