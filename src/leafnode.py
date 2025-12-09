from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None): # type: ignore
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        node_string = ""

        if self.value == None:
            raise ValueError()
        
        if self.tag is None:
            return self.value
        
        node_string = ' '.join(f'{key}="{value}"' for key, value in self.props.items()) if self.props else ''
        if node_string == "":
            node_string = f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            node_string = f'<{self.tag} {node_string}>{self.value}</{self.tag}>'

        return node_string
