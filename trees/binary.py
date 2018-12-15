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

        for i,_ in enumerate(nodes[:-1]):
            nodes[i].left  = nodes[2*i+1]
            nodes[i].right = nodes[2*i+2]
        return

    def tostring(self):

        string = ""
        curr = self.head
        while curr.left is not None:
            string = string + curr.tostring() + ", "
            curr = curr.next

        string = string[:-2]
        string = "[" + string + "]"

        return string
