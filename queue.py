class Queue:
    def __init__(self):
        self.items= []
    
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def head(self):
        return self.items[0]

    def tail(self):
        return self.items[-1]

#testing the queue class
# q=Queue() #create new queue

# q.enqueue(1) #add 1 to queue
# q.enqueue(2) #add 2 to queue
# q.enqueue(3) #add 3 to queue

# print(q.head()) #should be 1
# print(q.tail()) #should be 3
# print(q.dequeue()) #should pop out 1
# print(q.head()) #should now be 2
