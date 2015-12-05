#! /usr/bin/env python3

class BST:
    class Node:
        def __init__(self, value, left, right):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert_helper(self.root, value)

    def find(self, value):
        return self.__find_helper(self.root, value)

    def delete(self, value):
        node = self.find(value)
        if node == None:
            return self.root
            


    def __insert_helper(self, root, value):
        if root == None:
            return self.Node(value, None, None)
        if value < root.value: # go left
            root.left = self.__insert_helper(root.left, value)
        elif value > root.value: # go right
            root.right = self.__insert_helper(root.right, value)
        return root

    
    def __find_helper(self, root, value):
        if root == None:
            return None
        elif root.value > value:
            return self.__find_helper(root.left, value)
        elif root.value < value:
            return self.__find_helper(root.right, value)
        else:
            return root

    def traverse(self, root, s):
        if root == None:
            return s
        s = self.traverse(root.left, s)
        s = s + " " + str(root.value)
        s = self.traverse(root.right, s)
        return s

    def __str__(self):
        s = self.traverse(self.root, "")
        return s

if __name__ == "__main__":
    tree = BST()
    tree.insert(5)
    tree.insert(1)
    tree.insert(6)
    tree.insert(3)
    tree.insert(-11)
    tree.insert(-222)
    tree.insert(-222)
    tree.insert(-225)
    print(tree)
    print(tree.find(-11))
    print(tree.find(2))
