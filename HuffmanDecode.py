
def huffmanDecode(text, root):
    """Decode the code word"""

    result = ""
    cur = root

    for i in text:

        if not isLeaf(cur) and i == "0":
            cur = cur.left
        elif not isLeaf(cur) and i == "1":
            cur = cur.right

        if isLeaf(cur):
            result += cur.val
            cur = root

    return result


def isLeaf(node):
    """determine whether a tree node is leaf or not"""

    return node.left is None and node.right is None
