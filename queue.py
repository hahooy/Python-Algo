""" elementary Queue data structure """

class LinkedListQueue:
    """ implemented using a linked list """
    class Node:
        def __init__(self, key, next_node):
            self.key = key
            self.next = next_node

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, key):
        if self.size == 0:            
            self.tail = self.Node(key, None)
            self.head = self.tail
        else:
            oldTail = self.tail
            self.tail = self.Node(key, None)
            oldTail.next = self.tail
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("the queue is empty")
        else:
            ret = self.head
            self.head = self.head.next
            self.size -= 1
            return ret.key

    def isEmpty(self):
        return self.size == 0

    def __repr__(self):
        x = self.head
        s = ""
        while x is not None:
            s = s + " " + str(x.key)
            x = x.next
        return s

if __name__ == "__main__":
    q = LinkedListQueue()
    q.enqueue(1)
    q.enqueue(2)
    print(q)
