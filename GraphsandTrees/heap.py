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

def main():
    pq = PriorityQueue(contents=[6,8,2,1,5,9])
    print(pq)


if __name__ == '__main__':
    main()