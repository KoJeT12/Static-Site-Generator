from htmlnode import HTMLNode

testpropDict = {"href":"https://www.google.com", "target":"_blank"}
htmlnode = HTMLNode("h1","test value string", None, testpropDict)

def test_props_html(htmlNode):
    print(htmlNode.props_to_html())
    
test_props_html(htmlnode)
print(repr(htmlnode))