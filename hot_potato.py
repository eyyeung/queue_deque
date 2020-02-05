from queue import Queue

def hotPotato(names, num):
    q = Queue()
    print (names, "are playing a game of hot potaot with num =", num)
    for name in names:
        q.enqueue(name)
    round_num=1
    while q.size() >1:
        for i in range(num):
            q.enqueue(q.dequeue())

        print("Round ",round_num,": ",q.dequeue(), "is eliminated")
        round_num+=1
            
    print("The only remaining person left is:",q.dequeue())

# Testing the function
#hotPotato(["a","b","c","d","e","f","g"],2)
