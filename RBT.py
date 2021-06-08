import sys

# data structure that represents a node in the tree
class Node():
    def __init__(self, key):
        self.key = key  # holds the key
        self.parent = None #pointer to the parent
        self.left = None # pointer to left child
        self.right = None #pointer to right child
        self.color = 1 # 1 . Red, 0 . Black


# class RedBlackTree implements the operations in Red Black Tree
class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def preOrderFunc(self, node):
        if node != TNULL:
            sys.stdout.write(node.key + " ")
            self.preOrderFunc(node.left)
            self.preOrderFunc(node.right)

    def inOrderFunc(self, node):
        if node != TNULL:
            self.inOrderFunc(node.left)
            sys.stdout.write(node.key + " ")
            self.inOrderFunc(node.right)

    def postOrderFunc(self, node):
        if node != TNULL:
            self.postOrderFunc(node.left)
            self.postOrderFunc(node.right)
            sys.stdout.write(node.key + " ")

    def searchTreeFunc(self, node, key):
        if node == TNULL or key == node.key:
            return node

        if key < node.key:
            return self.searchTreeFunc(node.left, key)
        return self.searchTreeFunc(node.right, key)

    # fix the rb tree modified by the delete operation
    def fixDelete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    # case 3.1
                    s.color = 0
                    x.parent.color = 1
                    self.rotateLeft(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    # case 3.2
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        # case 3.3
                        s.left.color = 0
                        s.color = 1
                        self.rotateRight(s)
                        s = x.parent.right

                    # case 3.4
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.rotateLeft(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    # case 3.1
                    s.color = 0
                    x.parent.color = 1
                    self.rotateRight(x.parent)
                    s = x.parent.left

                if s.left.color == 0 and s.right.color == 0:
                    # case 3.2
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        # case 3.3
                        s.right.color = 0
                        s.color = 1
                        self.rotateLeft(s)
                        s = x.parent.left 

                    # case 3.4
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.rotateRight(x.parent)
                    x = self.root
        x.color = 0

    def redBlackTrans(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def deleteFunc(self, node, key):
        # find the node containing key
        z = self.TNULL
        while node != self.TNULL:
            if node.key == key:
                z = node

            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Couldn't find key in the tree")
            return

        y = z
        yOri = y.color
        if z.left == self.TNULL:
            x = z.right
            self.redBlackTrans(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.redBlackTrans(z, z.left)
        else:
            y = self.min(z.right)
            yOri = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.redBlackTrans(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.redBlackTrans(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if yOri == 0:
            self.fixDelete(x)
    
    # fix the red-black tree
    def  fixInsert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left # uncle
                if u.color == 1:
                    # case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # case 3.2.2
                        k = k.parent
                        self.rotateRight(k)
                    # case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rotateLeft(k.parent.parent)
            else:
                u = k.parent.parent.right # uncle

                if u.color == 1:
                    # mirror case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent 
                else:
                    if k == k.parent.right:
                        # mirror case 3.2.2
                        k = k.parent
                        self.rotateLeft(k)
                    # mirror case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rotateRight(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def printTreeFunc(self, node, indent, last):
        # print the tree structure on the screen
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self.printTreeFunc(node.left, indent, False)
            self.printTreeFunc(node.right, indent, True)
    
    # Pre-Order traversal
    # Node.Left Subtree.Right Subtree
    def preorder(self):
        self.preOrderFunc(self.root)

    # In-Order traversal
    # left Subtree . Node . Right Subtree
    def inorder(self):
        self.inOrderFunc(self.root)

    # Post-Order traversal
    # Left Subtree . Right Subtree . Node
    def postorder(self):
        self.postOrderFunc(self.root)

    # search the tree for the key k
    # and return the corresponding node
    def searchTree(self, k):
        return self.searchTreeFunc(self.root, k)

    # find the node with the minimum key
    def min(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    # find the node with the maximum key
    def max(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    # find the successor of a given node
    def successor(self, x):
        # if the right subtree is not None,
        # the successor is the leftmost node in the
        # right subtree
        if x.right != self.TNULL:
            return self.min(x.right)

        # else it is the lowest ancestor of x whose
        # left child is also an ancestor of x.
        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    # find the predecessor of a given node
    def predecessor(self,  x):
        # if the left subtree is not None,
        # the predecessor is the rightmost node in the 
        # left subtree
        if (x.left != self.TNULL):
            return self.max(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    # rotate left at node x
    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def rotateRight(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # insert the key to the tree in its appropriate position
    # and fix the tree
    def insert(self, key):
        # Ordinary Binary Search Insertion
        node = Node(key)
        node.parent = None
        node.key = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1 # new node must be red

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # if new node is a root node, simply return
        if node.parent == None:
            node.color = 0
            return

        # if the grandparent is None, simply return
        if node.parent.parent == None:
            return

        # Fix the tree
        self.fixInsert(node)

    def getRoot(self):
        return self.root

    # delete the node from the tree
    def delete(self, key):
        self.deleteFunc(self.root, key)

    # print the tree structure on the screen
    def printTree(self):
        self.printTreeFunc(self.root, "", True)

if __name__ == "__main__":
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(12)
    rbt.insert(5)
    rbt.insert(4)
    rbt.insert(20)
    rbt.insert(8)
    rbt.insert(7)
    rbt.insert(15)
    rbt.insert(13)
    rbt.printTree()

    rbt.delete(20)
    rbt.printTree()

    rbt.delete(10)
    rbt.printTree()
    
# https://github.com/Bibeknam/algorithmtutorprograms/blob/master/data-structures/red-black-trees/red_black_tree.py
