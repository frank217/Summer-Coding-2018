# Dynamic programing
"""
Longest increasing subsequence

Given  array of n number find 
LIS


Input : lis.txt


Expected Output : 


"""
""" 
Solution 1: O(n^2)
Cache the LIS including the ith element.
Then loop through all the elements in the
array. Then also loop through all the elements 
after it with value larger then current value
then add + 1 to the maximum cached value.

Base case :
    last value in array.
Recursive : 
    current = current value in array.
    if current > array[i]:
        max (result,cache[i] + 1)
    


"""
def lis(l,cache, start):
    # Last element only one is possible
    if start == len(l) -1:
        return 1
    cur = l[start]
    result = 0
    for i in range(start+1, len(l)):
        if l[i] > cur:
            maxVal = cache[start]
            # value is cached
            if maxVal != -1:
                result = max(maxVal,result)
            # Need to get the value    
            else:
                result = max(lis(l,cache,i), result)
    
    cache[start] = result + 1
    return result +1

"""
Solution 2 : O(nlogn)

Basic idea is to keep track of all lenght of possible length and 
update as we progress through the array.
There are three ways to handle each value.
1) If the value is smallest among the ones  we had
    start a new list with legnth 1
2) If the value is largerst among the ones we had
    we copy the longest list copy it and add value.
3) Other wise find the list with largest end that is smaller than 
   value. Copy the list and add the value to it and delete other list
   with same length 

So if we have array [0, 8, 4, 12, 2, 10, 6, 14, -1]
value A[0] = 0 : 1)
0
-----------------------------
value A[1] = 8 : 2)
0
0 8 
-----------------------------
value A[1] = 4 : 3)
0
0 4 
-----------------------------
value A[2] = 12 : 2)
0
0 4 
0 4 12
-----------------------------
value A[3] = 2 : 3)
0
0 2
0 4 12
-----------------------------
value A[4] = 10 : 3)
0
0 2
0 2 10
-----------------------------
value A[5] = 6 : 3)
0
0 2
0 2 6
-----------------------------
value A[6] = 14 : 2)
0
0 2
0 2 6
0 2 6 14
-----------------------------
value A[7] = -1 : 1)
-1
0 2
0 2 6
0 2 6 14
-----------------------------
"""
import math

def lis2(l):
    print (l)
    cache = [[l[0]]]
    for i in l:
        # Case 1) Found smallest value so far
        if cache[0][0] >= i:
            cache[0][0] = i
        # Case 2) Found largest value so far
        elif cache[-1][-1] < i:
            nList = [i for i in cache[-1]]
            nList.append(i)
            cache.append(nList)
        # Case 3) In between
        else:
            n = findInCache(i,cache)
            # print ("n : ",n )
            nList = [i for i in cache[n]]
            nList.append(i)
            cache[n+1] = nList
    return len(cache[-1])

# Helper function to to binary search on cache
def findInCache(i, cache):
    low = -1
    hi = len(cache)

    while low + 1 < hi:
        mid = math.floor((low + hi)/2)
        if cache[mid][-1] <= i:
            low = mid
        else : 
            hi = mid
    return low
 
  
# Driver program to
# test above function
 
A = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
n =len(A)
 
print("Length of Longest Increasing Subsequence is ",
       lis2(A))
# Ans is 6
    

# f_out = open('lisOutput.txt', 'w')
# f_in = open('lis.txt', 'r')
# # print (f_in.readlines())
# lines = [line.strip() for line in f_in.readlines()][0:]
# # print (lines)
# cur = 1
# for case in range(int(lines[0])):
    
#     n = int(lines[cur])
#     cur +=1
    
#     board = []
#     for i in range(n):
#         line = []
#         for j in lines[cur+i]:
#             line.append(int(j))
#         board.append(line)
#     cur += n

#     cache = [[-1 for i in range(len(board))] for i in range(len(board))]
#     # print (board,cache)
#     result = jump(board,0,0, cache)
#     print (cache)
#     print (result)
#     # break

# f_out.close()




"""
Note : 
If the question require longest subsequence instead of of its length
one simply need to add another list that contains which index it has 
chosen to get the max length at each index. Doing so one can reconstruct
longest subsequence very easily. 

Use of index is because of better memory utilization(saving entire subsequence
will take n^2 instead of n).
"""



