class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None): # type: ignore
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        
        html_string = ""
        for key, value in self.props.items():
            html_string += f' {key}="{value}"'
        
        return html_string
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value: str, props: dict = None):  # type: ignore
        super().__init__(tag=tag, value=value, children=None, props=props) # type: ignore

    def to_html(self) -> str:
        node_string = ""

        if self.value == None:
            raise ValueError()
        
        if self.tag is None:
            return self.value
        
        props_string = self.props_to_html()
        
        if props_string == "":
            node_string = f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            node_string = f'<{self.tag}{props_string}>{self.value}</{self.tag}>'

        return node_string