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

    # Find node in tree
    def find(self, data):
        if(self.value == data):
            print(self.value)
            return True

        elif self.value > data:
            if self.leftChild:
                print(self.value)
                return self.leftChild.find(data)
            else:
                print(self.value)
                return False
        else:
            if self.rightChild:
                print(self.value)
                return self.rightChild.find(data)
            else:
                print(self.value)
                return False     

    # Pre-Order Traversal
    def preOrder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preOrder()
            if self.rightChild:
                self.rightChild.preOrder()
    
    # Post-Order Traversal
    def postOrder(self):
        if self:
            if self.leftChild:
                self.leftChild.postOrder()
            if self.rightChild:
                self.rightChild.postOrder()
            print(str(self.value))

    # In-Order Traversal
    def inOrder(self):
        if self:
            if self.leftChild:
                self.leftChild.inOrder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inOrder()

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

    # Removes node from tree
    def removeNode(self, data):
    	# empty tree
        if self.root is None:
            return False
			
		# data is in root node	
        elif self.root.value == data:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
            elif self.root.leftChild and self.root.rightChild:
                delNodeParent = self.root
                delNode = self.root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild
					
                self.root.value = delNode.value
                if delNode.rightChild:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.leftChild = delNode.rightChild
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.rightChild = delNode.rightChild
                else:
                    if delNode.value < delNodeParent.value:
                        delNodeParent.leftChild = None
                    else:
                        delNodeParent.rightChild = None
						
            return True
		
        parent = None
        node = self.root
		
        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            elif data > node.value:
                node = node.rightChild
		
		# case 1: data not found
        if node is None or node.value != data:
            return False
			
		# case 2: remove-node has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True
			
        # case 3: remove-node has left child only
        elif node.leftChild and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True
			
		# case 4: remove-node has right child only
        elif node.leftChild is None and node.rightChild:
            if data < parent.value:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True
			
		# case 5: remove-node has left and right children
        else:
            delNodeParent = node
            delNode = node.rightChild
            while delNode.leftChild:
                delNodeParent = delNode
                delNode = delNode.leftChild
				
            node.value = delNode.value
            if delNode.rightChild:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    delNodeParent.rightChild = delNode.rightChild
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.leftChild = None
                else:
                    delNodeParent.rightChild = None

    # Find node in tree
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    # Pre-Order Traversal
    def preOrder(self):
        print("Pre-Order")
        self.root.preOrder()

    #Post-Order Traversal
    def postOrder(self):
        print("Post-Order")
        self.root.postOrder()

    #In-Order Traversal
    def inOrder(self):
        print("In-Order")
        self.root.inOrder()

    #Get height of binary tree
    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return 0


def main():
    # Create a Tree
    myTree = Tree()

    # Insert Nodes into tree
    myTree.insertNode(30)
    myTree.insertNode(10)
    myTree.insertNode(45)
    myTree.insertNode(38)
    myTree.insertNode(20)
    myTree.insertNode(50)
    myTree.insertNode(25)
    myTree.insertNode(33)
    myTree.insertNode(8)
    myTree.insertNode(12)


    print("Height of tree is", (myTree.getHeight()))

    print("Search for 38: ", (myTree.find(38)))
    print("Search for 9: ", (myTree.find(9)))

    myTree.removeNode(10)
    myTree.preOrder()
    myTree.postOrder()
    myTree.inOrder()

main()