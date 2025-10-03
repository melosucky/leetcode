# You are given two integers numBottles and numExchange.
# numBottles represents the number of full water bottles that you initially have. 
# In one operation, you can perform one of the following operations:
# Drink any number of full water bottles turning them into empty bottles.
# Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.
# Note that you cannot exchange multiple batches of empty bottles for the same value of numExchange. 
# For example, if numBottles == 3 and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.
# Return the maximum number of water bottles you can drink.


class Solution:
    def __init__(self) -> None:
        self.numBottles=0
        self.BottlesDrunk=0
        self.emptyBottles=0
        pass
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        self.numBottles= numBottles
        self.BottlesDrunk+=self.numBottles
        self.emptyBottles+=self.numBottles
        self.numBottles=0
        self.emptyBottles-=numExchange
        numExchange+=1
        # print(self.numBottles,self.emptyBottles,numExchange,self.BottlesDrunk)
        if self.emptyBottles>=0:
            self.numBottles+=1
            return self.maxBottlesDrunk(self.numBottles,numExchange)
        else:
            return self.BottlesDrunk
        
# SENZA RECURSION
        
# class Solution:
#     def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
#         bottles_drunk = numBottles
#         empty = numBottles

#         while empty >= numExchange:
            
#             empty -= numExchange
#             numExchange += 1
#             bottles_drunk += 1
#             empty += 1  

#         return bottles_drunk
   

# solu=Solution()
# numBottles = 13
# numExchange = 6
# bevute=solu.maxBottlesDrunk(numBottles,numExchange)
# print(bevute)