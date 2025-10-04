# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


class Solution:
    def groupAnagrams(self, strs: list[str]):
        contaL={}
        
        for e in (strs):
            char=tuple(sorted(e))
            contaL[char]=contaL.get(char,[])+[e]
            
        return list(contaL.values())


# sl=Solution()
# strs = ["eat","tea","tan","ate","nat","bat"]
# lista=sl.groupAnagrams(strs)
# print(lista)