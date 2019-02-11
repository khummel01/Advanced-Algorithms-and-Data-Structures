class Trie:
    class TrieNode:
        def __init__(self, val, follows=None, next=None):
            self.val = val
            self.follows = follows
            self.next = next

        def getVal(self):
            return self.val

        def getFollows(self):
            return self.follows

        def getNext(self):
            return self.next

        def setFollows(self, followVal):
            self.follows = followVal

        def setNext(self, nextVal):
            self.next = nextVal

        def __repr__(self):
            return "Trie.TrieNode(" + repr(self.val) + "," + repr(self.follows) + "," + repr(self.next) + ")"

    '''Start of Trie Class'''
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = Trie.__insert(key + "$", self.root)

    def __insert(key, node):
        if key == "":
            return None
        # there are no more nodes to traverse, we must make a new one
        if node == None:
            node = Trie.TrieNode(key[0])
            node.setFollows(Trie.__insert(key[1:], None))
            return node
        # key[0] == node val, get follows
        if key[0] == node.getVal():
            node.setFollows(Trie.__insert(key[1:], node.getFollows()))
        # key doesn't match, insert rest of key into next
        else:
            node.setNext(Trie.__insert(key, node.getNext()))

        return node

    def __contains__(self, item):
        if len(item) == 0:
            return False
        return Trie.__contains(item+"$", self.root)

    def __contains(key, node):
        if len(key) == 0:
            return True
        elif node == None:
            return False
        elif key[0] == node.getVal():
            return Trie.__contains(key[1:], node.getFollows())
        else:
            return Trie.__contains(key, node.getNext())



def readDict(filename):
    words = []
    with open(filename, 'r') as wordsInfile:
        for line in wordsInfile:
            words.append(line.strip())
    return words


def getDecWords(filename):
    decWords = []
    # create list of declaration words
    with open(filename, 'r') as decInfile:
        for line in decInfile:
            words = line.split()
            for word in words:
                if "." in word and "-" in word:
                    periodIdx = word.index(".")
                    firstWord = word[:periodIdx].lower().strip()
                    secondWord = word[periodIdx + 3:].lower().strip()
                    decWords.append(firstWord)
                    decWords.append(secondWord)
                elif word[0] == "-":
                    decWords.append(word[2:].lower().strip())
                elif word.strip()[-1] in ".,:;-":
                    decWords.append(word.lower().strip()[:-1])
                elif word != "&":
                    decWords.append(word.lower().strip())
    return decWords


def main():
    words = readDict('wordsEn.txt')
    decWords = getDecWords('independence.txt')

    trie = Trie()

    for word in words:
        trie.insert(word)

    print("Incorrect words:")
    for word in decWords:
        if word not in trie:
            print(word)



if __name__ == '__main__':
    main()

'''
Time complexity of Trie is O(1). This is because there 
is an upper bound on the length of the chain of first letter values 
which is 26, the num of letters in the alphabet. From there, the 
time complexity depends on the length of the individual word which 
in most cases will be less than 26 letters, giving Trie an time 
complexity of O(1). 
'''