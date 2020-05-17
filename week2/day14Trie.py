"""
Implement a trie with insert, search, and startsWith methods.

Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

class Trie(object):

    def __makeBlock(self):
        data = {
            "isEnd": False
        }
        return data
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if node.get(char) == None:
                node[char] = self.__makeBlock()
            node = node[char]
        node["isEnd"] = True
        

    def getNode(self, word):
        node = self.root
        for char in word:
            if node.get(char):
                node = node[char]
            else:
                node = None
                break
        return node
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.getNode(word)
        return node and node["isEnd"]
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return True if self.getNode(prefix) else False
        

def test():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True, '"apple" must be present'
    assert trie.search("app") == False, '"app" must not exist'
    assert trie.startsWith("app") == True, '"app" must be prefix'
    trie.insert("app")
    assert trie.search("app") == True, '"app" must exist'


if __name__ == "__main__":
    test()