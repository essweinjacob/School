import random

class Node:
    # Constructor
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    #Insert a Node into tree
    def insertNode(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insertNode(data)
            else:
                self.leftChild = Node(data)
        else:
            if self.rightChild:
                return self.rightChild.insertNode(data)
            else:
                self.rightChild = Node(data)
                return True

    #Gets height of tree
    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
        elif self.leftChild:
            return 1 + self.leftChild.getHeight()
        elif self.rightChild:
            return 1 + self.rightChild.getHeight()
        else:
            return 1

class Tree:
    # Constructor
    def __init__(self):
        self.root = None

    #Insert a Node into tree
    def insertNode(self, data):
        if self.root:
            return self.root.insertNode(data)
        else:
            self.root = Node(data)

    #Get height of binary tree
    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return 0


def main():
    height = 0

    # Get variable inputs
    numTrees = int(input("How many trees would you like created?" ))
    keys = int(input("How many keys/nodes would you like to create?" ))

    for _ in range(0, numTrees):
        myTree = Tree()
        for i in range(1, keys):
            myTree.insertNode(random.randint(0,1000))

        height = height + myTree.getHeight()
    
    print("The average height for ", numTrees, " of these binary trees with ", keys, " keys : ", height/numTrees)

main()