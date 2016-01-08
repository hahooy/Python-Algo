'''
Created on Dec 9, 2015

@author: hahooy1
'''
#! /usr/bin/env python3

class BST:
    class Node:
        def __init__(self, value, left, right, parent=None):
            self.value = value
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert_helper(self.root, value, None)

    def find(self, value):
        return self.__find_helper(self.root, value)

    def contains(self, k):
        if self.find(k) is not None:
            return True
        else:
            return False

    def delete(self, x):
        """delete node x from the tree"""

        if x is None:
            print("the tree is empty")
            return
        
        if x.left is not None and x.right is not None:
            z = self.succ(x)
            x.value = z.value
            self.delete(z)
            return            
        
        # if x has no child, just delete it
        if x.left is None and x.right is None:
            z = None
        elif x.left is not None and x.right is None:
            z = x.left        
        else:
            z = x.right
        
        if x.parent is None:
            self.root = z
        elif x.parent.left is x:
            x.parent.left = z
        else:
            x.parent.right = z
            
        if z is not None:
            z.parent = x.parent
        
    def min(self):
        return self.__min_helper(self.root)
        

    def __min_helper(self, x):
        """find the minimum node in the tree rooted at x"""
        while x is not None and x.left is not None:
            x = x.left
        return x

    def max(self):
        return self.__max_helper(self.root)        

    def __max_helper(self, x):
        """find the maximum node in the tree rooted at x"""
        while x is not None and x.right is not None:
            x = x.right
        return x

    def succ(self, x):
        """find the successor of node x in the tree"""
        if x is None:
            return None

        if x is not None and x.right is not None:
            return self.__min_helper(x.right)

        y = x.parent
        while y is not None and y.left is not x:
            x = y
            y = x.parent
        return y

    def pred(self, x):
        """find the predecessor of node x in the tree"""
        if x is None:
            return None

        if x.left is not None:
            return self.__max_helper(x.left)

        y = x.parent
        while y is not None and y.right is not x:
            x = y
            y = x.parent
        return y



    def __insert_helper(self, root, value, parent):
        if root == None:
            return self.Node(value, None, None, parent)
        if value < root.value: # go left
            root.left = self.__insert_helper(root.left, value, root)
        elif value > root.value: # go right
            root.right = self.__insert_helper(root.right, value, root)
        return root

    
    def __find_helper(self, root, value):
        while root is not None and root.value != value:
            if root.value < value:
                root = root.right # go right
            else:
                root = root.left # go left
        return root

    def inorder_traverse(self, root, s):
        if root == None:
            return s
        s = self.inorder_traverse(root.left, s)
        s = s + " " + str(root.value)
        s = self.inorder_traverse(root.right, s)
        return s

    def __str__(self):
        s = self.inorder_traverse(self.root, "")
        return s[1:]

if __name__ == "__main__":
    """unit test"""
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
    assert(tree.contains(-11))
    assert(not tree.contains(2))
    assert(tree.min().value == -225)
    assert(tree.max().value == 6)
    assert(tree.succ(tree.find(-222)).value == -11)
    assert(tree.succ(tree.find(1)).value == 3)
    assert(tree.pred(tree.find(5)).value == 3)
    assert(tree.pred(tree.min()) is None)
    assert(tree.pred(tree.max()).value == 5)
    tree.delete(tree.find(5))
    assert(not tree.contains(5))
    tree.delete(tree.find(-225))
    assert(not tree.contains(-225))    
