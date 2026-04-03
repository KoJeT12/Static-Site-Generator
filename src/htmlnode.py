

class HTMLNode():
    def __init__(self, tag, value, children, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode( tag='{self.tag}', value='{self.value}', children='{self.children}', props='{self.props}')"
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props != None:
            props_string = ""
            for key, value in self.props.items():
                props_string += f'{key}="{value}" '
            return props_string
        else: 
            return ""

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        self.children = None

    def __repr__(self):
        return f"HTMLNode( tag='{self.tag}', value='{self.value}', props='{self.props}')"

    def to_html(self):
        if not self.value:
            raise ValueError
        if self.tag is None:
            return self.value
        props_string = self.props_to_html()
        html_string = f'<{self.tag}{props_string}>{self.value}</{self.tag}>'
        return html_string

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("No tag")
        if not self.children:
            raise ValueError("No Children")
        html_string_children = ""
        if len(self.children) > 0:
            for item in self.children:
                html_string_children += item.to_html()
        else: html_string_children += ""
        props_string = self.props_to_html()
        html_string = f'<{self.tag}{props_string}>{html_string_children}</{self.tag}>'
        return html_string

