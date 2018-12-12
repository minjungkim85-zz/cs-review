from node import Node,LinkedList
from math import ceil

n = 9
data = LinkedList(n)

slow = data.head
fast = data.head

while True:
    if (fast is None) or (fast.next is None):
        break
    slow = slow.next
    fast = fast.next.next

print("Solution:")
print("Ground truth: %d" % ceil(n/2.))
print("Array mid-point: %d" % (slow.x+1))
