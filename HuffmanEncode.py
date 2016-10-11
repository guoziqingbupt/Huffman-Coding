import HuffmanTreeGen


def gen_tf(text):
    """generate the term frequency table"""

    result = {}

    for i in text:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result


def genCharCodeTable(root):
    """return the char-code table"""

    path = ""
    result = {}

    huffmanDFS(root, path, result)

    return result


def huffmanDFS(root, path, result):
    """auxiliary function of genCharCodeTable which used DFS"""

    if root is None:
        return

    if root.left is None and root.right is None:
        result[root.val] = path

    if root.left:
        path += '0'
        huffmanDFS(root.left, path, result)

    if root.right:
        path = path[:-1] + '1'
        huffmanDFS(root.right, path, result)


def huffmanEncode(text, root):
    """Encode a text with Huffman coding"""

    # build charCodeTable
    charCodeTable = genCharCodeTable(root)

    result = ""

    for i in text:
        result = result + charCodeTable[i]

    # return the binary string
    return result


def encodeHelper(text):
    """the auxiliary function of huffmanEncode which generate root with text"""

    # build TF table
    termFreq = gen_tf(text)

    # build orderedNodeList
    orderedNodeList = HuffmanTreeGen.genOrderedNodeList(termFreq)

    # build Huffman Tree
    return HuffmanTreeGen.huffman(orderedNodeList)















