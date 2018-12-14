class Node():
    def __init__(self,x):
        self.x = x
        self.left = None
        self.right = None
        return

    def tostring(self):
        return str(self.x)

class BinaryTree():
    def __init__(self,n):

        nodes = [Node(i) for i in range(n)]
        self.root = nodes[0]

        for i in range(len(nodes)):
            li, ri = 2*i+1, 2*i+2

            if ri < len(nodes):
                nodes[i].right = nodes[ri]
            if li < len(nodes):
                nodes[i].left  = nodes[li]

        return

    def tostring(self):

        string = ""
        curr = self.root
        string = string + curr.tostring() + " "

        string = string + curr.left.tostring() + " "
        string = string + curr.right.tostring() + " "

        strleft  = curr.left.tostring()
        strright = curr.right.tostring()

        # TODO
        return string
