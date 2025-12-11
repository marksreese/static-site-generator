from textnode import TextNode, TextType

def split_nodes_delimiter(nodes, delimiter: str, text_type):
    result = []
    current_sublist = []
    type = TextType.PLAIN
    paired = True
    for node in nodes:
        if node.text_type != TextType.PLAIN:
            result.append(node)
            continue
        chars = list(node.text)
        for char in chars:
            if char != delimiter:
                current_sublist.append(char)
            else:
                if len(current_sublist) > 0:
                    result.append(TextNode(''.join(current_sublist), type))
                    current_sublist = []
                if type == TextType.PLAIN:
                    type = text_type
                else:
                    type = TextType.PLAIN
                paired = not paired
    if len(current_sublist) > 0:
        result.append(TextNode(''.join(current_sublist), type))
    if paired is False:
        raise Exception("Unpaired delimiter found in nodes.")
    return result