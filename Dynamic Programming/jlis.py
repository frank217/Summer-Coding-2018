# Conquer and divide

"""
**** Unresolved ***** (Bug when two array has same value)
Joined Longest Increasing Subsequence.

Given two array find the joined longest increase
subsequence that can be formed using subsequence 
from each array.

example : [4,7,6] and [4,3,7,6,9]
answer = 3
[]

Input : trianglepath.txt


Expected Output : 

i = index of array A
j = index of array B
jlis(i,j) = jlis starting from index i and j

Base case :
1) i or j reaches last index
2) both reach last index
recursive :
jlist(i,j) =
    max --- nextA = for all index after i
        |       max(jlis(nextA, j))
        --- nextB = for all index after j
                max(jlist(i, nextB))



"""



def jlis(i,j):
    print(i,j)
    # Valuse is cached
    if cache[i][j] != -1:
        return cache[i][j]
    # Base case

    # If value is same only one can be in result
    if A[i] == B[j]:
        result = 0
        cache[i][j] = 0
        return 0
    else:
        result = 2
    
    larger = max(A[i],B[j])
    # Recursive case
    for a in range(i+1,len(A)):
        if A[a] > A[i] and A[a] != B[j]:
            result = max(result, jlis(a,j) + 1)
        if i==1 and j==1 :
            print ("chechA",a,A[a],result)
    for b in range(j+1,len(B)):
        if B[b] > B[j] and B[b] != A[i]:
            result = max(result, jlis(i,b) + 1)
        if i==1 and j==1 :
            print ("chechB",b, B[b],result)
    print("finished", i,j, result)
    cache[i][j] = result
    return result

# Error : the arrays can have same value
# in the previous array.
    

f_out = open('jlisOutput.txt', 'w')
f_in = open('jlis.txt', 'r')
# print (f_in.readlines())
lines = [line.strip() for line in f_in.readlines()][0:]
# print (lines)
for case in range(int(lines[0])):
    la, lb = list(map(int,lines[case*3+1].split(" ")))
    A = list(map(int, lines[case*3 +2].split(" ")))
    B = list(map(int, lines[case*3 +3].split(" ")))
    cache =[[-1 for i in range(int(lb))] for i in range(int(la))]
    print ("A and B",A,B)
    result = 0

    # for i in range(la):
    #     for j in range(lb):
    #         if A[i] == B[j]:
    #             cache[i][j] = 0
    #             continue
    #         if cache[i][j] != -1:
    #             cur = cache[i][j]
    #         else:
    #             cur = jlis(i,j)
    #         result = max(result, cur)
    result = jlis(0,0)
    print (result)
    print(cache)
    break

f_out.close()







