"""
World Code sprint 13
Watson's Love for Arrays(medium)

Detail :
https://www.hackerrank.com/contests/world-codesprint-13/challenges/watsons-love-for-arrays
Expected output:
13
3
1
9
"""


"""
Naive version:
Runtime Analysis

n = len(A)
O(n*3) where n is max 10^5 so this will be very slow
"""

def howManyGoodSubarrays(A, m, k):
    count = 0
    # Return the number of good subarrays of A.
    for i in range(len(A)):
        for j in range(i,len(A)):
            result = 1
            for a in A[i:j+1]:
                result *= a
            if result % m ==k:
                count +=1
    return count
"""
Better version:
Use DP
have cahce for n x n matrix that keeps the multiplied value from i to j.

"""
def kingdomDivision(n, roads):
    tree ={}
    for i in range(1,n+1):
        
        # Tree dictionary also cache information for parent, child,
        # How many different one it has probability it has with 
        tree[i] = {"parent": -1, "child":[],"red":-1, "black":-1}
        
    tList = [[] for i in range(n+1)]
    for i in roads:
        f,s = i 
        tList[f].append(s)
        tList[s].append(f)
    
    queue = [(1,0)]
    while queue:
        
        node,prev = queue[0]
        queue = queue[1:]
        tree[node]["parent"] = prev
        for i in tList[node]:
            if i != prev:
                queue.append((i,node))
                tree[node]["child"].append(i)    
    print(tree)
#     #Assume all input is correct
#     for i in roads:
#         f,s = i
#         if tree[f]["parent"] != -1 and tree[s]["parent"] != -1:
#             if tree[s]["parent"] == 0:
#                 tree[s]["parent"] = f
#                 tree[f]["child"].append(s)
#             else:
#                 tree[f]["parent"] = s
#                 tree[s]["child"].append(f)
                
#         elif tree[f]["parent"] != -1:
#             tree[s]["parent"] = f
#             tree[f]["child"].append(s)
#         elif tree[s]["parent"] != -1:
#             tree[f]["parent"] = s
#             tree[s]["child"].append(f)
#         #first case when two nodes doesn't have parent, assume first one is parent
#         else :
#             tree[f]["parent"] = 0 
#             tree[s]["parent"] = f
#             tree[f]["child"].append(s)
    
    queue =[(1,0)]
    level = 0
    lList = []
    while queue:
        node, l = queue[0]
        queue = queue[1:]
        if l != level:
            print (level)
            print(lList)
            lList = []
            level = l
        lList.append(node)
        for i in tree[node]["child"]:
            queue.append((i,l + 1))
    print(level)
    print(lList)
    
    print("Algorithm :")
    #Get possible ways it can be formed
    return helper(tree, 1)

"""
Input : tree(dictionary of required value, its parent and child nodes, ways for if it is black and red)
        root, current root node
        color of roots parent node
Output : return tree with the root node red and black information filled

"""
def helper(tree, root, parent):
    
    #Flag if the root node has a leaf node
    flag = False
    
    #If node is leaf node
    if len(tree[root]["child"]) == 0:
        tree[root]["red"] == 1
        tree[root]["black"] == 1
        return 1
    
    # If not leaf node caculate what value is possible
    result = 1
    # Never caculated before
    if tree[root]["red"] == -1:
        children = tree[root]["child"]
        for i in children:
            value = helper(tree, i)
            # if root ==3:
                # print("Value", value, "i", i,"root", root)
            if value == 1:
                flag = True
            result *= value
        # if root == 3:
            # print("result",result, "flage",flag,"root", root)
        if flag:
            tree[root]["red"] = result
            tree[root]["black"] = result
            result *=2
        else:
            for i in tree[root]["child"]:
                tree[i]
            tree[]
            
            # minusRVal = 1
            # minusBVal = 1
            # for i in children:
            #     minusRVal *= tree[i]["black"]
            #     minusBVal *= tree[i]["red"]
            #     # print("children", i,tree[i]["black"] ,tree[i]["red"])
            # tree[root]["red"] = result - minusRVal
            # tree[root]["black"] = result - minusBVal
            # result = result *2 - minusBVal - minusRVal
            # # if root ==3:
            #     # print(result, minusRVal, minusBVal)
    print("root",root, "Result",result)
    return result
