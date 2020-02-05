from deque import Deque

def palindromeChecker(word):
    d = Deque()

    for char in word:
        d.enqueue_back(char)

    while d.size()>1:
        first = d.dequeue_front()
        last = d.dequeue_back()
        if first != last:
            return False

    return True

#Test palindromeChecker
print(palindromeChecker("abe")) # False
print(palindromeChecker("radar")) # True
print(palindromeChecker("toot")) # True 