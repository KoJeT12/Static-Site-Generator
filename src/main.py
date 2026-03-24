from textnode import TextNode, TextType

def main():
    testType = TextType.text_code
    testUrl = "https://www.boot.dev"
    testNode = TextNode("Test Text", testType, testUrl)
    print(testNode)
#test
main()