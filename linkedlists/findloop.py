import numpy as np
from node import Node

def getdata(n=10,loop=False):
    nodes = [Node(i) for i in range(n)]
    for i,_ in enumerate(nodes[:-1]):
        nodes[i].next = nodes[i+1]

    if loop:
        i1 = None
        i2 = None
        while True:
            i1,i2 = np.random.permutation(n)[:2]
            if i2 < i1:
                # swap
                i1 = i1 + i2
                i2 = i1 - i2
                i1 = i1 - i2

            if (i2 is not nodes[-1].x) \
                and i2 != i1+1:
                break
        nodes[i1].next = nodes[i2]
        nodes[-1].next = nodes[i1+1]

    return nodes

def getorder(llist):

    curr  = llist[0]
    order = [None]*n
    for i in range(n):
        order[i] = curr.x
        curr = curr.next

    return order


n = 9
gtloop = False
data  = getdata(n,gtloop)
order = getorder(data)


curr = data[0]
fast = curr
slow = curr
i = 0
loop = False
while True:
    if (i > 0) & (fast.x == slow.x):
        loop = True
        break

    if (fast is None) or (fast.next is None):
        loop = False
        break

    fast = fast.next.next
    slow = slow.next

    i += 1

print("Ground truth: loop = %r" % gtloop)
print("Solution: loop = %r" % loop)
