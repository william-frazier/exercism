
VALID_KEYS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if input_string == "":
        raise ValueError("Input string cannot be null.")
    if "(" not in input_string or ")" not in input_string:
        raise ValueError("Input string does not contain a tree.")
    if ";" not in input_string:
        raise ValueError("Input string does not contain a node.")
    tree = SgfTree()
    sanitized_input = input_string.replace("(","")
    sanitized_input = sanitized_input.replace(")","")
    sanitized_input = sanitized_input.split(";")[1:]
    print(f"starting on input", input_string)
    print(sanitized_input)
    if sanitized_input[0] == "":
        return tree
    for i in sanitized_input:
        node_list = i.split("[")
        if node_list[0] not in VALID_KEYS:
            raise ValueError("Nodes must be capitalized.")
        tree.properties[node_list[0]] = node_list[1]
        print(node_list)
        print(input_string)
        print(tree.properties)
    return tree
        
