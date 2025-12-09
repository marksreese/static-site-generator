from htmlnode import HTMLNode
from textnode import TextNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None): # type: ignore
        super().__init__(tag=tag, value=value, props=props)

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

    def text_node_to_html_node(text_node: 'TextNode') -> LeafNode: # type: ignore
        type = text_node.text_type
        match type:
            case None:
                raise Exception("TextNode must have a TextType")
            case type.PLAIN:
                return LeafNode(tag="", value=text_node.text) # type: ignore;
            case type.BOLD:
                return LeafNode(tag="b", value=text_node.text)
            case type.ITALIC:
                return LeafNode(tag="i", value=text_node.text)
            case type.CODE:
                return LeafNode(tag="code", value=text_node.text)
            case type.LINK:
                if text_node.url is None:
                    raise Exception("Link TextNode must have a URL")
                return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
            case type.IMAGE:
                if text_node.url is None:
                    raise Exception("Image TextNode must have a URL")
                return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
            case _:
                raise Exception("Unknown TextType")