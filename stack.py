""" stack data structure """

class Stack:
    """  implemented using python list """
    def __init__(self):
        self.a = []
        self.size = 0

    def push(self, k):
        """ push element k onto the stack """
        self.a.append(k)
        self.size += 1

    def pop(self):
        """ pop the top element off the stack """
        if self.isEmpty():
            return
        del self.a[-1]
        self.size -= 1

    def isEmpty(self):
        return self.size == 0

    def __repr__(self):
        return str(self.a)

class StackList:
    """ implemented using linked list """
    class Node:
        def __init__(self, key, nextNode):
            self.key = key
            self.next = nextNode


    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, k):
        if self.head is None:
            self.head = self.Node(k, None)
        else:
            new_node = self.Node(k, self.head)
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print("stack underflow")
        else:
            self.head = self.head.next
            self.size -= 1

    def isEmpty(self):
        return self.size == 0
        
    def __repr__(self):
        x = self.head
        s = ""
        while x is not None:
            s = str(x.key) + " " + s
            x = x.next
        return s


if __name__ == "__main__":
    stack = StackList()
    stack.push(5)
    stack.push(11)
    stack.push(2)
    stack.pop()
    print(stack)
