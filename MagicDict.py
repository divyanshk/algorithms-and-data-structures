# Problem: https://leetcode.com/problems/implement-magic-dictionary/description/
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictMap = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            if len(word) not in self.dictMap:
                self.dictMap[len(word)] = []
            self.dictMap[len(word)].append(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.dictMap:
            return False
        possibleMatches = self.dictMap[len(word)]
        for possibleMatch in possibleMatches:
            mismatch = 0
            for m, n in zip(word, possibleMatch):
                mismatch += 1 if m != n else 0
            if mismatch == 1:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
