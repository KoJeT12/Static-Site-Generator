from enum import Enum

class TextType(Enum):
    text_plain = "Plain"
    text_bold = "Bold"
    text_italic = "Italic"
    text_code = "Code"
    text_link = "Link"
    text_image = "Image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

