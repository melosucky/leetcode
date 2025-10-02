# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        i,e = 0,0
        for ch in s:
            countS[ch] = countS.get(ch, 0) + 1
            print(countS)
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
            print(countT)
        
        return countS == countT

s = "aab"
t = "aba"
solu=Solution()   
print(solu.isAnagram(s,t))