from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

from htmlnode import HTMLNode
from textnode import TextNode

def text_node_to_html_node(text_node: 'TextNode'):
    type = text_node.text_type
    if type is None:
        raise Exception("TextNode must have a TextType")
    elif type == type.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif type == type.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif type == type.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif type == type.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif type == type.LINK:
        if text_node.url is None:
            raise Exception("Link TextNode must have a URL")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif type == type.IMAGE:
        if text_node.url is None:
            raise Exception("Image TextNode must have a URL")
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("Unknown TextType")
        

class TextNode():
    def __init__(self, text: str, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        return (
            self.text == node.text and
            self.text_type == node.text_type and
            self.url == node.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"