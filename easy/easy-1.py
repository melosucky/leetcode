##Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
##You may assume that each input would have exactly one solution, and you may not use the same element twice.
##You can return the answer in any order.

lista=[2,7,11,15]
target=int(9)

def somma_t (lista,target,i=0):
    nums={}
    for i,indice in enumerate(lista):
        complementare=target-lista[i]

        if complementare in nums:
            print (nums)
            return [nums[complementare],i]
        
        nums[indice]=i
            

print(somma_t(lista,target))
