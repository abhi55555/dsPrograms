class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pcrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pcrawl.children[index]:
                pcrawl.children[index] = self.getNode()
            pcrawl = pcrawl.children[index]

        pcrawl.isEnd = True

    def search(self, key):

        pcrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pcrawl.children[index]:
                return False
            pcrawl = pcrawl.children[index]

        return pcrawl != None and pcrawl.isEnd  # to ensure pcrawl.isEnd is True for returning true


if __name__ == '__main__':
    keys = ['the', 'that', 'a', 'anaser', 'dobule', 'boom']
    output = ['Word not present', 'Word present']

    t = Trie()
    for key in keys:
        t.insert(key)

    print('the -> ', output[t.search('the')])
    print('tha -> ', output[t.search('tha')])
    print('boom -> ', output[t.search('boom')])
    print('bool -> ', output[t.search('boo')])
