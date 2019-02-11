import xml.dom.minidom
import sys
import operator

# MIN HEAP
class PriorityQueue:
    def __init__(self, degree=2, contents=[]):
        self.degree = degree
        self.data = list(contents)
        self.size = len(contents)

        parentIndex = (self.size - 2) // self.degree
        for i in range(parentIndex, -1, -1):
            self.__siftDownFromTo(i, self.size - 1)

    def enqueue(self, item):
        self.data.append(item)
        self.size += 1
        self.__siftUp(self.size-1)

    def dequeue(self):
        min = self.data[0]
        self.data[0] = self.data[self.size-1]
        del self.data[self.size-1]
        self.size -= 1
        parentIndex = (self.size - 2) // self.degree
        for i in range(parentIndex, -1, -1):
            self.__siftDownFromTo(i, self.size - 1)
        return min

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def __siftUp(self, idx):
        childIdx = idx
        done = False
        while not done:
            parentIndex = (childIdx - 1) // self.degree
            if childIdx == 0:
                done = True
            elif self.data[childIdx] < self.data[parentIndex]:
                self.data[parentIndex], self.data[childIdx] = \
                    self.data[childIdx], self.data[parentIndex]
                childIdx = parentIndex
            else:
                done = True

    def __siftDownFromTo(self, fromIndex, toIndex):
        parentIndex = fromIndex
        done = False

        while not done:
            childIndex = self.__bestChildOf(parentIndex, toIndex)

            if childIndex == None:
                done = True

            elif self.data[parentIndex] > self.data[childIndex]:
                self.data[parentIndex], self.data[childIndex] = \
                    self.data[childIndex], self.data[parentIndex]

                parentIndex = childIndex
            else:
                done = True

    def __bestChildOf(self, parentIndex, toIndex): # least child
        firstChildIndex = parentIndex * self.degree + 1
        endIndex = min(parentIndex * self.degree + self.degree, toIndex)

        if firstChildIndex > endIndex:
            return None

        bestChildIndex = firstChildIndex # this is a guess

        for k in range(firstChildIndex, endIndex + 1):
            if self.data[k] < self.data[bestChildIndex]:
                bestChildIndex = k

        return bestChildIndex

    def __repr__(self):
        return "PriorityQueue(" + str(self.degree) + "," + str(self.data) + ")"

    def __str__(self):
        return repr(self)


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

    pq = PriorityQueue()
    pq.enqueue(startingVertex)

    while not pq.isEmpty():
        # returns min VertexCost obj and removes it from the heap
        current = pq.dequeue()
        if current.getVertexId() not in visitedVertexIds:
            visitedVertexIds.add(current.getVertexId())
            adjacent = vertexIdVertexObjDict[current.getVertexId()].getAdjacent()
            for edgeObj in adjacent:
                otherVertexId = edgeObj.getV1()

                # make sure we're looking at the correct vertex
                if otherVertexId == current.getVertexId():
                    otherVertexId = edgeObj.getV2()

                possNewCost = current.getCost() + edgeObj.getWeight()
                # check to see if the cost is smaller
                if possNewCost < vertexIdVertexObjDict[otherVertexId].getCost():
                    vertexIdVertexObjDict[otherVertexId].updateCost(possNewCost)
                    currentLabel = vertexIdVertexObjDict[current.getVertexId()].getLabel()
                    vertexIdVertexObjDict[otherVertexId].setPrevious(currentLabel)

                    # add new vertex to heap
                    pq.enqueue(VertexCost(possNewCost, otherVertexId))

    # create a list sorted by vertex label (for printing purposes)
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
