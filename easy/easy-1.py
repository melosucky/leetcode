##Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
##You may assume that each input would have exactly one solution, and you may not use the same element twice.
##You can return the answer in any order.

lista=[2,7,11,15]
target=int(9)

def somma_t (lista,target,i=0):
    if len(lista)==0:
        return print("lista vuota")
    

    for i in range (len(lista)):

        e=target-lista[i]
        if e in lista:
            ind=(i,lista.index(e))
            return print(f"gli indici sono {ind}")
        else:
            i=+1
            pass
            

somma_t(lista,target)
