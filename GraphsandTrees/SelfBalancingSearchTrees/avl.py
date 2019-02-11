import random

class Stack:
    def __init__(self):
        self._items = []

    def push(self, new_item):
        self._items.append(new_item)

    def peek(self):
        if len(self._items) > 0:
            return self._items[-1]
        else:
            raise IndexError('The stack is empty')

    def __len__(self):
        return len(self._items)

    def size(self):
        return len(self._items)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0

    def clear(self):
        self._items = []
        return self._items

    def __str__(self):
        return str(self._items)


'''Start of AVLNode Class'''
class AVLNode:
    def __init__(self, item, balance=0, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
        self.balance = balance

    def getVal(self):
        return self.item

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getBalance(self):
        return self.balance

    def setBalance(self, newBalance):
        self.balance = newBalance

    def setLeft(self, newItem):
        self.left = newItem

    def setRight(self, newItem):
        self.right = newItem

    def depth(self):
        '''Return the depth of the node. (Leave nodes are depth one)'''
        return max(self.left.depth() if self.left else 0, self.right.depth() if self.right else 0) + 1

    def rotateLeft(self):
        '''  Perform a left rotation of the subtree rooted at the
         receiver.  Answer the root node of the new subtree.
        '''
        child = self.right
        if (child == None):
            print('Error!  No right child in rotateLeft.')
            return None

        self.right = child.left
        child.left = self
        return child

    def rotateRight(self):
        '''  Perform a right rotation of the subtree rooted at the
         receiver.  Answer the root node of the new subtree.
        '''
        child = self.left
        if (child == None):
            print('Error!  No left child in rotateRight.')
            return None

        self.left = child.right
        child.right = self
        return child

    def rotateRightThenLeft(self):
        '''Perform a double inside left rotation at the receiver.  We
         assume the receiver has a right child (the bad child), which has a left
         child. We rotate right at the bad child then rotate left at the pivot
         node, self. Answer the root node of the new subtree.  We call this
         case 3, subcase 2.
        '''
        self.right = self.getRight().rotateRight()
        return self.rotateLeft()

    def rotateLeftThenRight(self):
        '''Perform a double inside right rotation at the receiver.  We
         assume the receiver has a left child (the bad child) which has a right
         child. We rotate left at the bad child, then rotate right at
         the pivot, self.  Answer the root node of the new subtree. We call this
         case 3, subcase 2.
        '''
        self.left = self.getLeft().rotateLeft()
        return self.rotateRight()

    def __iter__(self):
        if self.left != None:
            for elem in self.left:
                yield elem

        yield self

        if self.right != None:
            for elem in self.right:
                yield elem

    def __str__(self):
        '''  This performs an inorder traversal of the tree rooted at self,
           using recursion.  Return the corresponding string.
        '''
        st = str(self.item) + ' ' + str(self.balance) + '\n'
        if self.left != None:
            st = str(self.left) + st  # A recursive call: str(self.left)
        if self.right != None:
            st = st + str(self.right)  # Another recursive call
        return st
        # return '(' + str(self.getVal()) + ',' + str(self.balance) + ')'

    def __repr__(self):
        return "AVLNode(" + repr(self.item) + "," + repr(self.left) + "," + repr(self.right) + ")"


'''Start of AVLTree Class'''
class AVLTree:
    def __init__(self, count=0, root=None):
        self.root = root
        self.count = count

    def __str__(self):
        st = 'There are ' + str(self.count) + ' nodes in the AVL tree.\n'
        return st + str(self.root)  # Using the string hook for AVL nodes

    def insert(self, newItem):
        '''  Add a new node with item newItem, if there is not a match in the
          tree.  Perform any rotations necessary to maintain the AVL tree,
          including any needed updates to the balances of the nodes.  Most of the
          actual work is done by other methods.
        '''
        pivot, pathStack, parent, found = self.search(newItem)

        if not found:
            newNode = AVLNode(newItem, 0)

            self.count += 1

            # self.root is None, set it equal to the new node
            if parent is None:
                self.root = newNode

            else:
                # insert newNode as either a left or right child
                if newNode.getVal() < parent.getVal():
                    parent.setLeft(newNode)
                else:
                    parent.setRight(newNode)

                # Case 1: no pivot
                if pivot == None:
                    self.case1(pathStack, pivot, newNode)
                else:
                    # Case 2: the subtree of the pivot node in which the new node was added has smaller height
                    if (newNode.getVal() < pivot.getVal() and pivot.getBalance() > 0) or (newNode.getVal() > pivot.getVal() and pivot.getBalance() < 0):
                        self.case2(pathStack, pivot, newNode)
                    # Case 3: newNode is added to the subtree in the direction of imbalance
                    else:
                        self.case3(pathStack, pivot, newNode)

    def adjustBalances(self, theStack, pivot, newNode):
        '''  We adjust the balances of all the nodes in theStack, up to and
           including the pivot node, if any.  Later rotations may cause
           some of the balances to change.
        '''
        foundPivot = False
        while not foundPivot and not theStack.is_empty():
            currentNode = theStack.pop()
            if newNode.getVal() < currentNode.getVal():
                currentNode.balance -= 1
            else:
                currentNode.balance += 1
            if currentNode == pivot:
                foundPivot = True

    def case1(self, theStack, pivot, newNode):
        '''  There is no pivot node.  Adjust the balances of all the nodes
           in theStack.
        '''
        self.adjustBalances(theStack, pivot, newNode)

    def case2(self, theStack, pivot, newItem):
        ''' The pivot node exists.  We have inserted a new node into the
           subtree of the pivot of smaller height.  Hence, we need to adjust
           the balances of all the nodes in the stack up to and including
           that of the pivot node.  No rotations are needed.
        '''
        self.adjustBalances(theStack, pivot, newItem)

    def case3(self, theStack, pivot, newNode): #newItem
        '''  The pivot node exists.  We have inserted a new node into the
           larger height subtree of the pivot node.  Hence rebalancing and
           rotations are needed.
        '''
        self.adjustBalances(theStack, pivot, newNode)

        # Define badChild
        # (badChild: the child of the pivot node in the direction of the imbalance)
        badChild = pivot.getLeft() if pivot.getBalance() < 0 else pivot.getRight()

        if (newNode.getVal() < badChild.getVal() and pivot.getBalance() < 0) or (newNode.getVal() > badChild.getVal() and pivot.getBalance() > 0) :
            '''
            Case 3a (single rotation): newNode is added to the subtree of 
            the bad child which is also in the direction of the imbalance.
            '''
            # Right rotation
            if newNode.getVal() < badChild.getVal():
                rootNewSubtree = pivot.rotateRight()
            # Left rotation
            else:
                rootNewSubtree = pivot.rotateLeft()

            # Regardless of whether it was a right/left rotation, reset pivot and badChild to 0
            pivot.setBalance(0)
            badChild.setBalance(0)
        else:
            '''
            Case 3b (double rotation): newNode is added to the subtree of 
            the bad child which is in the opposite direction of the imbalance 
            '''
            # Define badGrandchild
            # (badGrandchild: the child of the badChild node in the direction of the imbalance)
            if newNode.getVal() < badChild.getVal() and badChild.getLeft().getVal() != newNode.getVal():
                badGrandchild = badChild.getLeft()
            elif newNode.getVal() > badChild.getVal() and badChild.getRight().getVal() != newNode.getVal():
                badGrandchild = badChild.getRight()
            else:
                badGrandchild = None

            rotateDirection = 'right-left' if newNode.getVal() < badChild.getVal() else 'left-right'

            # Rotate right, then left
            if rotateDirection == 'right-left':
                rootNewSubtree = pivot.rotateRightThenLeft()
            # Rotate left, then right
            else:
                rootNewSubtree = pivot.rotateLeftThenRight()

            # Adjust balances
            if badGrandchild is None:
                pivot.setBalance(0)
                badChild.setBalance(0)
            else:
                badGrandchild.setBalance(0)
                if rotateDirection == 'right-left' and newNode.getVal() < badGrandchild.getVal():
                    badChild.setBalance(1)
                    pivot.setBalance(0)
                elif rotateDirection == 'right-left' and newNode.getVal() > badGrandchild.getVal():
                    badChild.setBalance(0)
                    pivot.setBalance(-1)
                elif rotateDirection == 'left-right' and newNode.getVal() < badGrandchild.getVal():
                    badChild.setBalance(0)
                    pivot.setBalance(1)
                elif rotateDirection == 'left-right' and newNode.getVal() > badGrandchild.getVal():
                    badChild.setBalance(-1)
                    pivot.setBalance(0)

            rootNewSubtree.setBalance(0)

        # Assign rootNewSubtree to it's new parent
        if not theStack.is_empty():
            grandParentNode = theStack.pop()
            if rootNewSubtree.getVal() < grandParentNode.getVal():
                grandParentNode.setLeft(rootNewSubtree)
            else:
                grandParentNode.setRight(rootNewSubtree)
        else:
            self.root = rootNewSubtree

    def search(self, newItem):
        '''  The AVL tree is not empty.  We search for newItem. This method will
          return a tuple: (pivot, theStack, parent, found).
          In this tuple, if there is a pivot node, we return a reference to it
          (or None). We create a stack of nodes along the search path -- theStack.
          We indicate whether or not we found an item which matches newItem.  We
          also return a reference to the last node the search examined -- referred
          to here as the parent.  (Note that if we find an object, the parent is
          reference to that matching node.)  If there is no match, parent is a
          reference to the node used to add a child in insert().
        '''
        parent = None
        node = self.root
        pivot = None
        pathStack = Stack()
        found = False

        while node != None and found != True:
            pathStack.push(node)

            if node.getBalance() != 0:
                pivot = node

            parent = node

            # newItem is larger than node
            if newItem > node.getVal():
                node = node.getRight()
            # newItem is smaller than node
            elif newItem < node.getVal():
                node = node.getLeft()
            # newItem equals node
            else:
                found = True

        return (pivot, pathStack, parent, found)

    # Caution: This method computationally heavy!
    def valid(self):
        for node in self:
            heightLeftSubTree = 0
            heightRightSubTree = 0
            if node.getLeft() is not None:
                heightLeftSubTree = node.getLeft().depth()
            if node.getRight() is not None:
                heightRightSubTree = node.getRight().depth()
            if heightRightSubTree - heightLeftSubTree not in [-1, 0, 1]:
                return False
        return True

    def __iter__(self):
        if self.root != None:
            return iter(self.root)
        else:
            return iter([])

    def __repr__(self):
        return "BinarySearchTree(" + repr(self.root) + ")"


def main():
    tree = AVLTree()

    error = False

    for i in range(10):
        if not error:
            tree.insert(random.randint(0, 501))
            if not tree.valid():
                print("Something is wrong with the AVLTree!")
                print()
                for node in tree:
                    print(node.getVal())
                error = True

    if error != True:
        print("AVLTree is balanced.")

    print(tree)


if __name__ == '__main__': main()
