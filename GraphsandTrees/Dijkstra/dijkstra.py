import random
import xml.dom.minidom
import sys
import operator


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


class OrderedTreeSet:
    class BinarySearchTree:
        # This is a Node class that is internal to the BinarySearchTree class.
        class Node:
            def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

            def getVal(self):
                return self.val

            def setVal(self, newval):
                self.val = newval

            def getLeft(self):
                return self.left

            def getRight(self):
                return self.right

            def setLeft(self, newleft):
                self.left = newleft

            def setRight(self, newright):
                self.right = newright

            # This method deserves a little explanation. It does an inorder traversal
            # of the nodes of the tree yielding all the values. In this way, we get
            # the values in ascending order.

            # @deprecated
            # def __iter__(self):
            #     if self.left != None:
            #         for elem in self.left:
            #             yield elem
            #
            #     yield self.val
            #
            #     if self.right != None:
            #         for elem in self.right:
            #             yield elem
            #

            def __repr__(self):
                return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"

        def __init__(self, root=None):
            self.root = root

        def insert(self, val):
            self.root = OrderedTreeSet.BinarySearchTree.__insert(self.root, val)

        def __insert(root, val):
            if root == None:
                return OrderedTreeSet.BinarySearchTree.Node(val)

            if val < root.getVal():
                root.setLeft(OrderedTreeSet.BinarySearchTree.__insert(root.getLeft(), val))
            else:
                root.setRight(OrderedTreeSet.BinarySearchTree.__insert(root.getRight(), val))

            return root

        def remove(self, val):
            self.root = OrderedTreeSet.BinarySearchTree._remove(self.root, val)

        def _remove(currentNode, val):
            if currentNode == None:
                return None

            if val < currentNode.getVal():
                currentNode.setLeft(OrderedTreeSet.BinarySearchTree._remove(currentNode.getLeft(), val))
            elif val > currentNode.getVal():
                currentNode.setRight(OrderedTreeSet.BinarySearchTree._remove(currentNode.getRight(), val))
            else:
                # case 1: no children
                if currentNode.getLeft() == None and currentNode.getRight() == None:
                    return None
                # case 2: has left child
                elif currentNode.getRight() == None:
                    return currentNode.getLeft()
                # case 3: has right child
                elif currentNode.getLeft() == None:
                    return currentNode.getRight()
                # case 4: has both children
                else:
                    successorNodeVal = OrderedTreeSet.BinarySearchTree.getRightMost(currentNode.getLeft())
                    currentNode.setVal(successorNodeVal)
                    currentNode.setLeft(
                        OrderedTreeSet.BinarySearchTree._remove(currentNode.getLeft(), successorNodeVal))

            return currentNode

        def getRightMost(currentNode):
            # base case
            if currentNode == None:
                return None
            # we found the max value
            elif currentNode.getRight() == None:
                return currentNode.getVal()
            # keep looking
            else:
                return OrderedTreeSet.BinarySearchTree.getRightMost(currentNode.getRight())

        def __iter__(self):
            s = Stack()
            currentNode = self.root
            done = False
            while not done:
                if currentNode != None:
                    s.push(currentNode)
                    currentNode = currentNode.getLeft()
                elif currentNode == None and s.is_empty() == False:
                    currentNode = s.pop()
                    yield currentNode.getVal()
                    currentNode = currentNode.getRight()
                else:
                    done = True

        def _find(node, val):
            if node.val == None:
                return False

            if node.getVal() == val:
                return True

            if val > node.getVal():
                return OrderedTreeSet.BinarySearchTree._find(node.getRight(), val)

            return OrderedTreeSet.BinarySearchTree._find(node.getLeft(), val)

        def _getLen(node):
            if node == None:
                return 0
            else:
                return (
                OrderedTreeSet.BinarySearchTree._getLen(node.getLeft()) + 1 + OrderedTreeSet.BinarySearchTree._getLen(
                    node.getRight()))

        def _getSmallest(node):
            if node == None:
                return None
            if node.getLeft() == None:
                return node.getVal()
            return OrderedTreeSet.BinarySearchTree._getSmallest(node.getLeft())


            # @deprecated
        # def __iter__(self):
        #     if self.root != None:
        #         return iter(self.root)
        #     else:
        #         return iter([])

        def __str__(self):
            return "BinarySearchTree(" + repr(self.root) + ")"

    def __init__(self, contents=None):
        self.tree = OrderedTreeSet.BinarySearchTree()
        if contents != None:
            # randomize the list
            indices = list(range(len(contents)))
            random.shuffle(indices)

            for i in range(len(contents)):
                self.tree.insert(contents[indices[i]])

            self.numItems = len(contents)
        else:
            self.numItems = 0

    def __str__(self):
        pass

    def __iter__(self):
        return iter(self.tree)

    # Following are the mutator set methods
    def add(self, item):
        OrderedTreeSet.BinarySearchTree.insert(self.tree, item)

    def remove(self, item):
        return OrderedTreeSet.BinarySearchTree.remove(self.tree, item)

    # Following are the accessor methods for the HashSet
    def __len__(self):
        return OrderedTreeSet.BinarySearchTree._getLen(self.tree.root)

    def intersection_update(self, otherTree):
        for item in self.tree:
            if item != None and item not in otherTree:
                OrderedTreeSet.BinarySearchTree.remove(self.tree, item)

    def update(self, otherTree):
        for item in otherTree:
            if item not in self.tree:
                self.tree.insert(item)

    def clear(self):
        self.tree.root = None

    def difference_update(self, otherTree):
        for item in otherTree:
            OrderedTreeSet.BinarySearchTree.remove(self.tree, item)

    def difference(self, otherTree):
        diffSet = OrderedTreeSet()
        for item in self.tree:
            if item != None and item not in otherTree:
                diffSet.add(item)
        return diffSet

    def issubset(self, otherTree):
        subTotal = 0
        for item in self.tree:
            if item in otherTree:
                subTotal += 1
        if self.__len__() == subTotal:
            return True
        return False

    def issuperset(self, otherTree):
        subTotal = 0
        for item in self.tree:
            if item in otherTree:
                subTotal += 1
        if self.__len__() > subTotal:
            return True
        return False

    def copy(self):
        newOrderTreeSet = OrderedTreeSet()
        for item in self.tree:
            newOrderTreeSet.add(item)
        return newOrderTreeSet

    def discard(self, item):
        try:
            OrderedTreeSet.BinarySearchTree.remove(self.tree, item)
        except Exception:
            pass

    def getSmallest(self):
        return OrderedTreeSet.BinarySearchTree._getSmallest(self.tree.root)

    def __contains__(self, val):
        return OrderedTreeSet.BinarySearchTree._find(self.tree.root, val)

    def __eq__(self, otherTree):
        if self.__len__() != otherTree.__len__():
            return False
        numSame = 0
        for item in self.tree:
            if item in otherTree:
                numSame += 1
        if self.__len__() == numSame:
            return True
        return False


class Vertex:
    def __init__(self, vertexId, x, y, label):
        self.vertexId = vertexId
        self.x = x
        self.y = y
        self.label = label
        self.adjacent = [] # list of Edge objects
        self.previous = None # label of previous vertex
        self.cost = sys.maxsize

    def addEdge(self, otherVertexId):
        self.adjacent.append(otherVertexId)

    def getAdjacent(self):
        return self.adjacent

    def setPrevious(self, vertexId):
        self.previous = vertexId

    def getPrevious(self):
        return self.previous

    def getCost(self):
        return self.cost

    def updateCost(self, newCost):
        self.cost = newCost

    def getLabel(self):
        return self.label


class Edge:
    def __init__(self, v1, v2, weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def getWeight(self):
        return self.weight

    def getV1(self):
        return self.v1

    def getV2(self):
        return self.v2

class VertexCost:
    def __init__(self, cost, vertexId):
        self.cost = cost
        self.vertexId = vertexId

    def getCost(self):
        return self.cost

    def getVertexId(self):
        return self.vertexId

    def __lt__(self, other):
        if type(self) != type(other):
            raise Exception("Unorderable Types")
        return self.cost < other.cost

    def __gt__(self, other):
        if type(self) != type(other):
            raise Exception("Unorderable Types")
        return self.cost > other.cost

    def __repr__(self):
        return str((self.cost, self.vertexId))


def main():
    xmldoc = xml.dom.minidom.parse('graph.xml')
    vertexElements = xmldoc.getElementsByTagName("Vertex")
    edgeElements = xmldoc.getElementsByTagName("Edge")
    # dict of vertexIds:vertexObjs
    vertexIdVertexObjDict = {}

    startingVertex = None
    # get vertexIds, add to vertexIdVertexObjDict
    for s in vertexElements:
        vertexId = int(s.attributes['vertexId'].value)
        x = s.attributes['x'].value
        y = s.attributes['y'].value
        label = int(s.attributes['label'].value)
        vertexObj = Vertex(vertexId, x, y, label)
        if label == 0:
            vertexObj.updateCost(0)
            vertexObj.setPrevious(0)
            startingVertex = VertexCost(0, vertexId)
        vertexIdVertexObjDict[vertexId] = vertexObj

    # get edge weights
    edgeSet = set()
    for j in edgeElements:
        vertex1 = int(j.attributes['tail'].value)
        vertex2 = int(j.attributes['head'].value)
        weight = float(j.attributes['weight'].value)
        edgeSet.add(Edge(vertex1, vertex2, weight))

    # add Edge object to appropriate vertex
    for edge in edgeSet:
        vertex1 = edge.getV1()
        vertex2 = edge.getV2()
        vertexIdVertexObjDict[vertex1].addEdge(edge)
        vertexIdVertexObjDict[vertex2].addEdge(edge)

    visitedVertexIds = set()

    treeSet = OrderedTreeSet()
    treeSet.add(startingVertex)

    while len(treeSet) != 0:
        current = treeSet.getSmallest()  # smallest by cost
        if current.getVertexId() not in visitedVertexIds:
            visitedVertexIds.add(current.getVertexId())
            adjacent = vertexIdVertexObjDict[current.getVertexId()].getAdjacent()
            for edgeObj in adjacent:
                otherVertexId = edgeObj.getV1()

                # make sure we we're looking at the right vertex
                if otherVertexId == current.getVertexId():
                    otherVertexId = edgeObj.getV2()

                possNewCost = current.getCost() + edgeObj.getWeight()
                # check to see if the cost is smaller
                if possNewCost < vertexIdVertexObjDict[otherVertexId].getCost():
                    vertexIdVertexObjDict[otherVertexId].updateCost(possNewCost)
                    currentLabel = vertexIdVertexObjDict[current.getVertexId()].getLabel()
                    vertexIdVertexObjDict[otherVertexId].setPrevious(currentLabel)

                # add new vertex to treeset
                treeSet.add(VertexCost(possNewCost, otherVertexId))
        # delete current from tree
        treeSet.remove(current)

    # create a list sorted by vertex label
    sortedLabels = sorted(vertexIdVertexObjDict.values(), key=operator.attrgetter('label'))

    # print label, cost, previous
    for vertexObj in sortedLabels:
        print("Vertex:")
        print("label: ", vertexObj.getLabel())
        print("cost: {:.2f}".format(vertexObj.getCost()))
        print("previous: ", str(vertexObj.getPrevious()))
        print()


if __name__ == "__main__":
    main()
