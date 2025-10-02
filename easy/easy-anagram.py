# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for c in s:
            countS[c] = countS.get(c, 0) + 1 #.get per contare quante volte c è il carattere
            
        for c in t:
            countT[c] = countT.get(c, 0) + 1
            
        return countS == countT

