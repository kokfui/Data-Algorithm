class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insertTree(self, data):
        if self.data == data:
            return False        

        elif data < self.data: 
            if self.left:
                return self.left.insertTree(data)
            else:
                self.left = Node(data)
                return True

        else:
            if self.right:
                return self.right.insertTree(data)
            else:
                self.right = Node(data)
                return True
            
    def minValueNode(self, node):
        current = node

        while(current.left != None):
            current = current.left

        return current

    def maxValueNode(self, node):
        current = node

        while(current.right != None):
            current = current.right

        return current

    def removeTree(self, data,root): 
        if self == None:
            return None

        if data < self.data:
            self.left = self.left.removeTree(data,root)
        elif data > self.data:
            self.right = self.right.removeTree(data,root)
        else:
            if self.left == None:

                if self == root:
                    temp = self.minValueNode(self.right)
                    self.data = temp.data
                    self.right = self.right.removeTree(temp.data,root) 

                temp = self.right
                
                return temp
            elif self.right == None:

                if self == root:
                    temp = self.maxValueNode(self.left)
                    self.data = temp.data
                    self.left = self.left.removeTree(temp.data,root) 

                temp = self.left
                
                return temp

            temp = self.minValueNode(self.right)
            self.data = temp.data
            self.right = self.right.removeTree(temp.data,root)

        return self

    def findTree(self, data): 
        if(data == self.data):
            print ("this number is in the tree")
        elif(data < self.data):
            if self.left:
                return self.left.findTree(data)
            else:
                print ("this number is not in the tree")
        elif (data > self.data):
            if self.right:
                return self.right.findTree(data)
            else:
                print ("this number is not in the tree")

    def preorder(self):
        if self:
            print(str(self.data), end = ' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
	
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.data), end = ' ')
            if self.right:
                self.right.inorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.data), end = ' ')

class Tree(object):
    def __init__(self):
        self.root = None

    def insertTree(self, data):
        if self.root:
            return self.root.insertTree(data)
        else:
            self.root = Node(data)
            return True

    def removeTree(self, data):
        if self.root != None:
            return self.root.removeTree(data,self.root)

    def findTree(self, data):
        if self.root:
            return self.root.findTree(data)
        else:
            print ("this number is not in the tree")

    def preorder(self):
        if self.root != None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root != None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root != None:
            print('Postorder: ')
            self.root.postorder()

if __name__ == '__main__':
    tree = Tree()
    tree.insertTree(9)
    tree.insertTree(3)
    tree.insertTree(1)
    tree.insertTree(6)
    tree.insertTree(5)
    tree.insertTree(20)
    tree.insertTree(30)
    tree.insertTree(21)
    tree.insertTree(20)
    print(tree.findTree(1))
    print(tree.findTree(12))
    print(tree.findTree(100))
    tree.preorder()
    tree.inorder()
    tree.postorder()
    tree.removeTree(5)
    print("\nrespective order after 5 is deleted ")
    tree.preorder()
    tree.inorder()
    tree.postorder()

# https://github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Trees/BinarySearchTree.py
