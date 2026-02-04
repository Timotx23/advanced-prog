def zip_sum(*lists):
    """
    Return elementwise sums across all input lists.
    """
    #iterative way
    



    
    #combine=list(map(lambda i,x: i=len(lists) x+lists[i],lists, ))
    


# Tests
print(zip_sum([1, 2, 3], [10, 20, 30]))                                       # [11, 22, 33]
print(zip_sum([0], [0], [0]))                                                 # [0]
print(zip_sum([5, -5], [2, 3], [-1, 4]))                                       # [6, 2]

print(zip_sum())                                                              # []  (edge: no lists)
print(zip_sum([], [], []))                                                    # []  (edge: empty lists)
