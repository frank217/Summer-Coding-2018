
"""
Tripathcnt
Difficulty : Medium

Find the numer of maxium path in a given traigle of numers

Input : 
4
9
5 7
1 3 2
3 5 5 6

Output:
2
"""

"""
Solution:
Convert the triangle of number to its max value path.
Then 

Base case:
At bottom row return its value.

Recursive case:
if child value are same:
    Add up the paths from two value
elif childA > childB: 
    return paths from childA
else:
    reuturn paths from childB


"""

def tri(x,y):
    #Base case
    if y == len(array)-1:
        return 1
    #Recursive
    A = tri(x,y+1)
    B = tri(x+1,y+1)
    if array[y+1][x] ==  cache[y+1][x+1] :
        return A + B
    elif array[y+1][x] > cache[y+1][x+1]:
        return A
    else:
        return B

def convert(x,y):
    if y == len(array)-1:
        return array[y][x]
    if cache[y][x]:
        return cache[y][x]
    result = max(convert(x,y+1),convert(x+1,y+1)) + array[y][x]
    cache[y][x] = result
    return result
    

    

t = int(input())
array =[]
for i in range(t):
    # n = int(input())
    # n, s = list(map(int,input().split(" ")))
    # array = list(map(int,input().split(" ")))
    array.append(list(map(int,input().split(" "))))

    # array.sort()
    # print (array)  
    cache = [[0 for j in range(len(array[i]))] for i in range(len(array))]
    convert(0,0) 
    result = tri(0,0)
    print(result)
    # print(cache)
