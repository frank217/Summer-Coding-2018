
"""
Packing (KnapSack)
Difficulty : Medium

Given a number of items and its weight and urgency, find maximum 
number of urgency, its number of items and name of items. 

Input : 
2
6 10
laptop 4 7 
camear 2 10
xbox 6 6
grinder 4 7 
dumbell 2 5
encyclopedia 10 4
6 17
laptop 4 7 
camear 2 10d
xbox 6 6
grinder 4 7 
dumbell 2 5
encyclopedia 10 4

Output:
24 3
laptop
camera
grinder
30 4
laptop
camera
xbox
gridner
"""

"""
Solution:
Use DP to save maximum number of items at given capcity 

pack(capacity, item) = maximum urgency from given capcity items after this item.


Base case:
No item left.

Recursive case:

pack(capacity,item) = max(pack(capacity-w[item], item +1), pack(capacity, item +1))
"""

def pack(capacity,item):
    #Base case
    if item == n:
        return 0
    if capacity in cache:
        if item in cache[capacity]:
            return cache[capacity][item]
    else:
        cache[capacity] = [0 for i in range(n)]
    
    result = cache[capacity][item] = 0
    #Recursive
    result = pack(capacity, item +1)
    # Check if there is enough weight space for item
    if capacity >= w[item][1]:
        result = max(result, pack(capacity - w[item][1], item +1)+ w[item][2])
    return result
    
def track(capacity,item):
    if item == n:
        return
    if pack(capacity - w[item][1], item +1) == pack(capacity, item +1):
        track(capacity, item+1)
    else:
        picked.append(item)
        track(capacity-w[item][1], item+1)

    

t = int(input())


for i in range(t):
    n,wlimit = list(map(int,input().split(" ")))
    w =[]
    for j in range(n):
        # [Name, weight, urgency]
        name, weight, urgency = input().split(" ")
        w.append([name,int(weight),int(urgency)])

    # array.sort()
    # print (array)  
    cache = {}
    # cache = {}[[0 for j in range(len(array[i]))] for i in range(len(array))]
    result = pack(wlimit,0)
    picked = []
    track(wlimit,0) 
    print("Case ",i, "Anserwer :")
    print(result, len(picked))
    for i in picked:
        print(w[i][0])
    # print(cache)
