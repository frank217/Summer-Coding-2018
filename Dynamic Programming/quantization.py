
"""
Quantization.
Difficulty : Medium

Given a array of number n and integer s.
Find miminum sum square difference with s number of number on array n.

For example if array 1 2 3 4 5 6 7 8 9 10 is given and s = 2.
1 2 3 4 5 6 7 8 9 10 can be quantized to 3 3 3 3 3 8 8 8 8 8.
For 1 2 3 4 5 and s =2, it can be quantized to 2 2 3 3 3.

first line is number of test case
for each test case, first line is length of array and s,
second line is array. 

Input : 
2
10 3 
3 3 3 1 2 3 2 2 2 1
9 3
1 744 755 4 897 902 890 6 777
Output:
0
648
"""

"""
Solution:
If we sort the array array, any qunatized number will come in order 
because the value can't get smaller if the larger value has smaller qunatized
value that smaller value. 
So sorted array can be divided in to s number of section and each section will
have one qunatized value.
n = length of array
s = sections

Base case:
length < 3 : return infinity 
lenght of 3 return its difficulty

Recursive case:
quantize(index, secitons) = 
for sectionSize in size 1 to n-sections find minimum:
    findQValue(index,sectionSize) + 
    quantize(index +secitonSize,sections - 1)

findQvalue:
Finding the minimum sum difference sqaure.
array = [a,b...,z], l = length of array
For i in array:
    (i-m)^2
= l*m^2 - 2m * ∑(array[i]) + ∑(array[i]^2)
minimum is when slope = 0, so do differential.
2lm - 2* ∑(array[i]) = 0
m = ∑(array[i])/l


"""

def quantize(index,section):
    # If cached use it.
    if cache[index][section]:
        return cache[index][section]
    # Base Case1 : section == 0
    if section == 0:
        # no array remain
        if index ==n:
            return 0
        # Array remain : invalid
        else:
            cache[index][section] = float("inf")
            return float("inf")

    # Base Case 2: When more section than remaining number : not valid
    if n -index < section:
        cache[index][section] = float("inf")
        return float("inf")
    
    result = float("inf")

    for sectionSize in range(1, n -index+1):
        result = min(result,
        findQValue(index, sectionSize) + quantize(index +sectionSize,section-1))
    cache[index][section] = result
    return result 

"""
Optimize findQValue to O(1)
Optimization1 : precaculate sum O(1)
Optimization2 : precalculate array[i]^2 
Cache both data
"""
def findQValue(index,sectionSize):
    m = sum(array[index:index+sectionSize])/sectionSize
    result =0
    for i in array[index:index+sectionSize]:
        result += (i-m)**2
    return int(result)
# FindQValue Test
# array = [1,2,3,4,5]
# print (findQValue(0,5),10)
# array = [1, 4, 6]
# print (findQValue(0,3))
# array = [744, 755, 777]
# print (findQValue(0,3))
# array = [890, 897, 902]
# print (findQValue(0,3))

t = int(input())
for i in range(t):
    n, s = list(map(int,input().split(" ")))
    array = list(map(int,input().split(" ")))
    array.sort()
    print (array)  
    cache = [[0 for i in range(s+1)] for j in range(n+1)]
    result = quantize(0,s)
    print(result)
    print(cache)
