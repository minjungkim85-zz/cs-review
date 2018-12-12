class Node():
    def __init__(self,x):
        self.x = x
        self.next = None
        return

    def tostring(self):
        return str(self.x)

class LinkedList():
    def __init__(self,n):

        nodes = [Node(i) for i in range(n)]
        for i,_ in enumerate(nodes[:-1]):
            nodes[i].next = nodes[i+1]

        self.head = nodes[0]

        return

    def tostring(self):

        string = ""
        curr = self.head
        while curr.next is not None:
            string = string + curr.tostring() + ", "
            curr = curr.next

        string = string[:-2]
        string = "[" + string + "]"

        return string
