from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None): # type: ignore
        super().__init__(tag, value=None, children, props) # type: ignore
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        if self.value is None:
            raise ValueError("ParentNode must have children.")
        
        props_html = self.props_to_html()
        children_html = "".join(child.to_html() for child in self.children)

        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"