import unittest
from leafnode import LeafNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode("span", "Sample Text", props={"class": "highlight"})
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Sample Text")
        self.assertEqual(node.props, {"class": "highlight"})
    
    def test_repr(self):
        node = LeafNode("div", "Content", props={"id": "main"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Content, children=None, props={'id': 'main'})")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click here", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" target="_blank">Click here</a>')

    def test_leaf_to_html_without_props(self):
        node = LeafNode("h1", "Welcome")
        self.assertEqual(node.to_html(), "<h1>Welcome</h1>")

    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_text_node_to_html_node_image(self):
        node = TextNode("An image", TextType.IMAGE, "http://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "http://example.com/image.png", "alt": "An image"})

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")