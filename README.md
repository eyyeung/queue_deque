# Queue
## Description
Queue class and Deque class implemented in Python and some of the uses of queue.

Queue utilzies the first in first out principle and contains the essential functions: head, tail, enqueue, dequeue, isEmpty, size

Deque has two ends, the front and the rear / back. Items can be added to the front or the rear. Similarly, items can be removed from the front or the rear of the deque
## Content
* queue.py : contains the class Queue, has the following functions
    * head() : returns the element at the head / front of the queue
    * tails() : returns the  element at the tail / end of the queue
    * enqueue(n): put n in the queue
    * dequeue(): pop out the element at the front / head of the queue
    * isEmpty(): returns True if the queue is empty and False otherwise
    * size(): returns the szie of the queue
* deque.py : contains the Deque class, has the following functions:
    * head() : returns the element at the head / front of the queue
    * tail() : returns the  element at the tail / end of the queue
    * enqueue_front(n): put n in the front of the queue
    * enqueue_back(n): put n in the back of the queue
    * dequeue_front(): pop out the element at the front / head of the queue
    * dequeue_back(): pop out the element at the back / rear of the queue
    * isEmpty(): returns True if the queue is empty and False otherwise
    * size(): returns the szie of the queue
    * at(index): returns the element at the index of the queue
* hot_potato.py : contains a function that plays the hot Potato game using Queue class
    * hotPotato(names, num) : takes in a list of names and a num, after num of rounds, whoever has the potato is off the game. This function automatically prints who is elimianted at each round and output the remaining winner
* palindrome_checker.py : contains a function that checks whether a word is a palindrome (same forward and backward) using the deque class
    * palindromeChecker(word) : takes in a word and return True if the word is a palindrome and False if not
## Testing
* Queue:
```python
#testing the queue class
q=Queue() #create new queue

q.enqueue(1) #add 1 to queue
q.enqueue(2) #add 2 to queue
q.enqueue(3) #add 3 to queue

print(q.head()) #should be 1
print(q.tail()) #should be 3
print(q.dequeue()) #should pop out 1
print(q.head()) #should now be 2
```
* Deque:
```python
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
```
* hotPotato(names, num) :
```python
hotPotato(["a","b","c","d","e","f","g"],2)
"""
Output would be:
['a', 'b', 'c', 'd', 'e', 'f', 'g'] are 
playing a game of hot potaot with num = 
2
Round  1 :  c is eliminated
Round  2 :  f is eliminated
Round  3 :  b is eliminated
Round  4 :  g is eliminated
Round  5 :  e is eliminated
Round  6 :  a is eliminated
The only remaining person left is: d 
"""
```
* palindromeChecker(word) :
```python
print(palindromeChecker("abe")) # False
print(palindromeChecker("radar")) # True
print(palindromeChecker("toot")) #True 
```