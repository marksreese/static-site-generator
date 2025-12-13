import unittest
from utility import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_no_match(self):
        matches = extract_markdown_images(
            "This is text with no images."
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "Here is an ![image1](https://example.com/image1.png) and another ![image2](https://example.com/image2.jpg)."
        )
        self.assertListEqual([
            ("image1", "https://example.com/image1.png"),
            ("image2", "https://example.com/image2.jpg")
        ], matches)

    def test_extract_markdown_images_edge_cases(self):
        matches = extract_markdown_images(
            "![alt text](http://example.com/image.png) ![another image](https://example.com/img.jpg)"
        )
        self.assertListEqual([
            ("alt text", "http://example.com/image.png"),
            ("another image", "https://example.com/img.jpg")
        ], matches)

    def test_extract_markdown_images_special_characters(self):
        matches = extract_markdown_images(
            "![image with spaces](https://example.com/image%20with%20spaces.png) ![image_with_underscores](https://example.com/image_with_underscores.jpg)"
        )
        self.assertListEqual([
            ("image with spaces", "https://example.com/image%20with%20spaces.png"),
            ("image_with_underscores", "https://example.com/image_with_underscores.jpg")
        ], matches)

    def test_extract_markdown_images_no_alt_text(self):
        matches = extract_markdown_images(
            "This is an image with no alt text: ![](https://example.com/no_alt.png)"
        )
        self.assertListEqual([
            ("", "https://example.com/no_alt.png")
        ], matches)

    def test_extract_markdown_images_no_url(self):
        matches = extract_markdown_images(
            "This is an image with no URL: ![alt text]()"
        )
        self.assertListEqual([
            ("alt text", "")
        ], matches)

    # def test_extract_markdown_images_nested_brackets(self):
    #     matches = extract_markdown_images(
    #         "This is an image with nested brackets: ![alt [text]](https://example.com/image.png)"
    #     )
    #     self.assertListEqual([
    #         ("alt [text]", "https://example.com/image.png")
    #     ], matches)

    # def test_extract_markdown_images_special_urls(self):
    #     matches = extract_markdown_images(
    #         "This is an image with special URL: ![alt text](https://example.com/image(1).png)"
    #     )
    #     self.assertListEqual([
    #         ("alt text", "https://example.com/image(1).png")
    #     ], matches)

    def test_extract_markdown_images_multiline(self):
        matches = extract_markdown_images(
            "This is an image:\n![alt text](https://example.com/image.png)\nEnd of text."
        )
        self.assertListEqual([
            ("alt text", "https://example.com/image.png")
        ], matches)

    def test_extract_markdown_images_no_exclamation(self):
        matches = extract_markdown_images(
            "This is a link, not an image: [alt text](https://example.com/page.html)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_similar_syntax(self):
        matches = extract_markdown_images(
            "This is not an image: ![alt text][1]\n\n[1]: https://example.com/image.png"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_escaped_characters(self):
        matches = extract_markdown_images(
            r"This is an image with escaped characters: !\[alt text\](https://example.com/image.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_complex_case(self):
        matches = extract_markdown_images(
            "Here is an image ![img1](http://example.com/img1.png) and some text ![img2](http://example.com/img2.jpg) followed by more text."
        )
        self.assertListEqual([
            ("img1", "http://example.com/img1.png"),
            ("img2", "http://example.com/img2.jpg")
        ], matches)

    def test_extract_markdown_images_no_spaces(self):
        matches = extract_markdown_images(
            "![img](http://example.com/img.png)![img2](http://example.com/img2.png)"
        )
        self.assertListEqual([
            ("img", "http://example.com/img.png"),
            ("img2", "http://example.com/img2.png")
        ], matches)

    def test_extract_markdown_images_leading_trailing_spaces(self):
        matches = extract_markdown_images(
            " ![ img ]( http://example.com/img.png ) "
        )
        self.assertListEqual([
            (" img ", " http://example.com/img.png ")
        ], matches)

    def test_extract_markdown_images_empty_string(self):
        matches = extract_markdown_images(
            ""
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_only_image(self):
        matches = extract_markdown_images(
            "![only image](http://example.com/only_image.png)"
        )
        self.assertListEqual([
            ("only image", "http://example.com/only_image.png")
        ], matches)

    def test_extract_markdown_images_image_at_end(self):
        matches = extract_markdown_images(
            "Some text before the image ![end image](http://example.com/end_image.png)"
        )
        self.assertListEqual([
            ("end image", "http://example.com/end_image.png")
        ], matches)

    def test_extract_markdown_images_image_at_start(self):
        matches = extract_markdown_images(
            "![start image](http://example.com/start_image.png) Some text after the image"
        )
        self.assertListEqual([
            ("start image", "http://example.com/start_image.png")
        ], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com/page.html)"
        )
        self.assertListEqual([("link", "https://example.com/page.html")], matches)

    def test_extract_markdown_links_no_match(self):
        matches = extract_markdown_links(
            "This is text with no links."
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "Here is a [link1](https://example.com/page1.html) and another [link2](https://example.com/page2.html)."
        )
        self.assertListEqual([
            ("link1", "https://example.com/page1.html"),
            ("link2", "https://example.com/page2.html")
        ], matches)

    def test_extract_markdown_links_edge_cases(self):
        matches = extract_markdown_links(
            "[Click here](http://example.com) to visit the site."
        )
        self.assertListEqual([
            ("Click here", "http://example.com")
        ], matches)

    def test_extract_markdown_links_special_characters(self):
        matches = extract_markdown_links(
            "[link with spaces](https://example.com/page%20with%20spaces.html) [link_with_underscores](https://example.com/page_with_underscores.html)"
        )
        self.assertListEqual([
            ("link with spaces", "https://example.com/page%20with%20spaces.html"),
            ("link_with_underscores", "https://example.com/page_with_underscores.html")
        ], matches)

    # def test_extract_markdown_links_no_alt_text(self):
    #     matches = extract_markdown_links(
    #         "This is a link with no alt text: []((https://example.com/no_alt.html)"
    #     )
    #     self.assertListEqual([
    #         ("", "https://example.com/no_alt.html")
    #     ], matches)

    def test_extract_markdown_links_no_url(self):
        matches = extract_markdown_links(
            "This is a link with no URL: [alt text]()"
        )
        self.assertListEqual([
            ("alt text", "")
        ], matches)

    # def test_extract_markdown_links_nested_brackets(self):
    #     matches = extract_markdown_links(
    #         "This is a link with nested brackets: [alt [text]](https://example.com/page.html)"
    #     )
    #     self.assertListEqual([
    #         ("alt [text]", "https://example.com/page.html")
    #     ], matches)

    # def test_extract_markdown_links_special_urls(self):
    #     matches = extract_markdown_links(
    #         "This is a link with special URL: [alt text](https://example.com/page(1).html)"
    #     )
    #     self.assertListEqual(
    #         [("alt text", "https://example.com/page(1).html")
    #     ], matches)

    def test_extract_markdown_links_multiline(self):
        matches = extract_markdown_links(
            "This is a link:\n[alt text](https://example.com/page.html)\nEnd of text."
        )
        self.assertListEqual([
            ("alt text", "https://example.com/page.html")
        ], matches)

    def test_extract_markdown_links_exclamation_mark(self):
        matches = extract_markdown_links(
            "This is not an image: ![alt text](https://example.com/image.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links_similar_syntax(self):
        matches = extract_markdown_links(
            "This is not a link: [alt text][1]\n\n[1]: https://example.com/page.html"
        )
        self.assertListEqual([], matches)

    # def test_extract_markdown_links_escaped_characters(self):
    #     matches = extract_markdown_links(
    #         r"This is a link with escaped characters: \[alt text\](https://example.com/page.html)"
    #     )
    #     self.assertListEqual([], matches)

    def test_extract_markdown_links_complex_case(self):
        matches = extract_markdown_links(
            "Here is a link [link1](http://example.com/page1.html) and some text [link2](http://example.com/page2.html) followed by more text."
        )
        self.assertListEqual([
            ("link1", "http://example.com/page1.html"),
            ("link2", "http://example.com/page2.html")
        ], matches)

    def test_extract_markdown_links_no_spaces(self):
        matches = extract_markdown_links(
            "[link](http://example.com/page.html)[link2](http://example.com/page2.html)"
        )
        self.assertListEqual([
            ("link", "http://example.com/page.html"),
            ("link2", "http://example.com/page2.html")
        ], matches)

    def test_extract_markdown_links_leading_trailing_spaces(self):
        matches = extract_markdown_links(
            " [ link ]( http://example.com/page.html ) "
        )
        self.assertListEqual([
            (" link ", " http://example.com/page.html ")
        ], matches)

    def test_extract_markdown_links_empty_string(self):
        matches = extract_markdown_links(
            ""
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links_only_link(self):
        matches = extract_markdown_links(
            "[only link](http://example.com/only_link.html)"
        )
        self.assertListEqual([
            ("only link", "http://example.com/only_link.html")
        ], matches)

    def test_extract_markdown_links_link_at_end(self):
        matches = extract_markdown_links(
            "Some text before the link [end link](http://example.com/end_link.html)"
        )
        self.assertListEqual([
            ("end link", "http://example.com/end_link.html")
        ], matches)

    def test_extract_markdown_links_link_at_start(self):
        matches = extract_markdown_links(
            "[start link](http://example.com/start_link.html) Some text after the link"
        )
        self.assertListEqual([
            ("start link", "http://example.com/start_link.html")
        ], matches)