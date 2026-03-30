import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_NoUrl(self):
        node = node = TextNode("This is a text node", TextType.BOLD)
        if node.url == None:
            print(f"True, No Url")
        elif node.url != None:
            print(f"False, Has Url")
            

if __name__ == "__main__":
    unittest.main()