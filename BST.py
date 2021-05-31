# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:19:53 2021

@author: user
"""
import sys
class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
class BST:
    def createSampleTree1(self):
        
        node50 =  Node(50)
        node30 =  Node(30)
        node70 =  Node(70)
        node30.parent = node50
        node70.parent = node50
        node50.left = node30
        node50.right = node70
        node23 =  Node(23)
        node35 =  Node(35)
        node23.parent = node30
        node35.parent = node30
        node30.left = node23
        node30.right = node35
        node11 =  Node(11)
        node25 =  Node(25)
        node11.parent = node23
        node25.parent = node23
        node23.left = node11
        node23.right = node25
        node31 =  Node(31)
        node42 =  Node(42)
        node31.parent = node35
        node42.parent = node35
        node35.left = node31
        node35.right = node42
        node80 =  Node(80)
        node80.parent = node70
        node70.right = node80
        node73 =  Node(73)
        node85 =  Node(85)
        node73.parent = node80
        node85.parent = node80
        node80.left = node73
        node80.right = node85
        self.root = node50
    def __printHelper(self, currPtr, indent, last):
        # print the tree structure on the screen
           if currPtr != None:
            sys.stdout.write(indent)
            if last:
                  sys.stdout.write("R----")
                  indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print (currPtr.data)

            self.__printHelper(currPtr.left, indent, False)
            self.__printHelper(currPtr.right, indent, True)
    
    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current

    def maxValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.right is not None):
            current = current.right

        return current


    def delete(self, data,root):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.left = self.left.delete(data,root)
        elif data > self.data:
            self.right = self.right.delete(data,root)
        else:
            # deleting node with one child
            if self.left is None:

                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.right = self.right.delete(temp.data,root) 

                temp = self.right
                self = None
                return temp
            elif self.right is None:

                if self == root:
                    temp = self.maxValueNode(self.left)
                    self.data = temp.data
                    self.left = self.left.delete(temp.data,root) 

                temp = self.left
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.right)
            self.data = temp.data
            self.right = self.right.delete(temp.data,root)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.data), end = ' ')
            if self.right:
                self.right.inorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.data), end = ' ')
    def prettyPrint(self):
        self.__printHelper(self.root, "", True)

if __name__ == '__main__':
    tree = BST ()
    tree.createSampleTree1()
    tree.prettyPrint()
'''https://github.com/Bibeknam/algorithmtutorprograms/blob/master/data-structures/binary-search-trees/BST.py''' 
'''https://github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Trees/BinarySearchTree.py'''
'''
