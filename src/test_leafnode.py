import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode("span", "Sample Text", props={"class": "highlight"})
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Sample Text")
        self.assertEqual(node.props, {"class": "highlight"})

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_repr(self):
        node = LeafNode("div", "Content", props={"id": "main"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Content, children=None, props={'id': 'main'})")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click here", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" target="_blank">Click here</a>')

    def test_leaf_to_html_without_props(self):
        node = LeafNode("h1", "Welcome")
        self.assertEqual(node.to_html(), "<h1>Welcome</h1>")