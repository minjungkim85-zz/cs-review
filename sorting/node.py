class Node():
    def __init__(self,x):
        self.x = x
        self.less = None
        self.more = None
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
                nodes[i].more = nodes[ri]
            if li < len(nodes):
                nodes[i].less  = nodes[li]

        return

    def iterate(self):
        queue = []

        return queue
        
    def tostring(self):

        string = ""
        curr = self.root
        string = string + curr.tostring() + " "

        string = string + curr.less.tostring() + " "
        string = string + curr.more.tostring() + " "

        strleft  = curr.less.tostring()
        strright = curr.more.tostring()

        # TODO
        return string
