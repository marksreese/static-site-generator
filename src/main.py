from textnode import TextNode, TextType

print("hello world")

def main():
    sample_node = TextNode("This is some anchor text", TextType.LINK, "http://boot.dev")
    print(sample_node)

main()