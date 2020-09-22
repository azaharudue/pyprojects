#Area calculator: 
def area(a, b): 
    return a*b
print(area(100,20))
# infinite string in  function parameter manipualation: 
def str_sort(*args): 
    args = [ i.upper() for i in args]
    return sorted(args)
print(str_sort("aba","xzy","cds","gdf", "jkl", "acd"))
# to access dictionaries: keyword argumets in function parameters: 
def mean(**kwargs): 
     return sum(kwargs.values())/len(kwargs)
print(mean(a=7.0, b=8.0,c=6))

print([i*2 for i in [1, 5, 10]])
