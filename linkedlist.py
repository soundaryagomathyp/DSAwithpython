#linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n1.next=n2
current=n1
while current is not None:
    print (current.data)
    current=current.next