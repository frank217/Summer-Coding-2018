
"""
Tiling2
Difficulty : Easy

Given 2 *n  size rectangle, find number of ways to fill
this rectangle with 2 *1 rectangle.


Input : 

Output:
"""

"""
Solution:
The tile can fit in only two ways.
1) one vetically that takes 1 space
2) two horizontally that takes 2 space.

So for each possiblity, go down recursively and 
add up the value. Along the way we can cache value.

Base case:


Recursive case:



"""

def tiling2(index):
    # Base case
    if index >= n-1:
        return 1
    if cache[index]:
        return cache[index]
    return tiling2(index+1) + tiling2(index+2)

t = int(input())
for i in range(t):
    n = int(input())
    # n, s = list(map(int,input().split(" ")))
    # array = list(map(int,input().split(" ")))
    # array.sort()
    # print (array)  
    cache = [0 for i in range(n)] 
    result = tiling2(0)
    print(result)
    print(cache)
