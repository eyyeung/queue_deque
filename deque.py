class Deque:
    def __init__(self):
        self.items= []
    
    def enqueue_back(self,item):
        self.items.append(item)

    def enqueue_front(self,item):
        self.items.insert(0,item)        

    def dequeue_front(self):
        return self.items.pop(0)
    
    def dequeue_back(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def head(self):
        return self.items[0]

    def tail(self):
        return self.items[-1]
    
    def at(self,index):
        return self.items[index]

#testing the dequeue class
def test():
    d = Deque()
    print("Deque Empty? ", d.isEmpty()) # should be True
    d.enqueue_back("Emily")
    print("Deque Empty? ", d.isEmpty()) # should be False

    d.enqueue_front("Amy") #pushes to the front of the deque.
    d.enqueue_front("Ben")
    d.enqueue_back("Cathy") #pushes to the back of the deque.
    d.enqueue_back("Gary")

    print("Deque Size: ", d.size()) # should be 5
    print("Item at the front: ", d.head()) # should be Ben
    print("Item at the back: ", d.tail()) # shoudl be Gary

    print("\n")
    print("Items in the Deque: ")
    for i in range(d.size()):
        #prints each item in the deque.
        print(d.at(i), end=" ")
    print("\n")
    # Ben Amy Emily Cathy Gary

    print("Deque from the back: ", d.dequeue_back()) # Gary should be out
    print("Deque from the front: ",d.dequeue_front()) # Ben should be out
 
    print("Item at the front: ", d.head()) # should be Amy
    print("Item at the back: ", d.tail()) # shoudl be Cathy
    print("Deque Size: ", d.size())

    print("\n")
    print("Items in the Deque: ")
    for i in range(d.size()):
        #prints each item in the deque.
        print(d.at(i), end=" ")
    print("\n")
    # Amy Emily Cathy