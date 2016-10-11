
class HuffmanTreeNode(object):

    def __init__(self, s, freq):
        self.val = s
        self.freq = freq
        self.left, self.right = None, None


def genOrderedNodeList(charDict):
    """return the the minimum priority queue"""

    orderedNodeList = []

    for i in sorted(charDict.items(), key=lambda x: x[1]):
        orderedNodeList.append(HuffmanTreeNode(i[0], i[1]))

    return orderedNodeList


def allocate(node1, node2):
    """allocate the 2 nodes"""

    new_freq = node1.freq + node2.freq

    new_node = HuffmanTreeNode(None, new_freq)
    new_node.left, new_node.right = node1, node2

    return new_node


def insertNode(orderedNodeList, new_node):
    """insert the new node to orderedNodeList"""

    for ele in orderedNodeList:
        if new_node.freq < ele.freq:
            orderedNodeList.insert(orderedNodeList.index(ele), new_node)
            return

    orderedNodeList.append(new_node)


def huffman(orderedNodeList):
    """generate the huffman tree, and return the tree root"""

    n = len(orderedNodeList)

    for i in range(n - 1):

        # pop the minimum 2 nodes
        node1 = orderedNodeList.pop(0)
        node2 = orderedNodeList.pop(0)

        # allocate the 2 nodes
        new_node = allocate(node1, node2)

        # insert the new node to orderedNodeList
        insertNode(orderedNodeList, new_node)

    return orderedNodeList[0]
