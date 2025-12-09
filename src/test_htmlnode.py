import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        childNode = HTMLNode(tag="child", value="childValue")
        childrenList = [childNode, childNode]
        node = HTMLNode(tag="htmlTag", value="nodeValue", children=[childNode, childNode], props={"key": "value"})
        self.assertEqual(node.tag, "htmlTag")
        self.assertEqual(node.value, "nodeValue")
        self.assertEqual(node.children, childrenList)
        self.assertEqual(node.props, {"key": "value"})
    
    def test_repr(self):
        node = HTMLNode(tag="p", value="Paragraph")
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=Paragraph, children=None, props=None)")

    def test_props_to_html_with_props(self):
        node = HTMLNode(props={"a": "b", "c": "d"})
        self.assertEqual(node.props_to_html(), ' a="b" c="d"')

    def test_props_to_html_without_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")