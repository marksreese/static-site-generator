from htmlnode import HTMLNode
from textnode import TextNode

def text_node_to_html_node(text_node: 'TextNode'): # type: ignore
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
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value: str, props: dict = None):  # type: ignore
        super().__init__(tag=tag, value=value, children=None, props=props) # type: ignore

    def to_html(self) -> str:
        node_string = ""

        if self.value == None:
            raise ValueError()
        
        if self.tag is None:
            return self.value
        
        node_string = self.props_to_html()
        
        if node_string == "":
            node_string = f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            node_string = f'<{self.tag}{node_string}>{self.value}</{self.tag}>'

        return node_string