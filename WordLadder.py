# Problem: https://leetcode.com/problems/word-ladder/description/
from sets import Set
from collections import deque
class Solution(object):    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        steps = 1
        queue = deque()
        wordList = Set(wordList)
        visited = Set([])
        queue.append(beginWord)
        numParent = 1
        numChild = 0
        if endWord not in wordList:
            return 0
        while queue:
            word = queue.popleft()
            #print word, steps
            numParent -= 1
            if word == endWord:
                break
                
            for i in xrange(len(word)):
                w = list(word)
                for ascii in xrange(97, 123):
                    w[i] = chr(ascii)
                    elem = ''.join(w)
                    if ((elem in wordList) and (elem not in visited)):
                        visited.add(elem)
                        queue.append(elem)
                        numChild += 1
            if numParent == 0:
                steps += 1
                #print queue
                numParent, numChild = numChild, numParent
        return steps if word == endWord else 0
