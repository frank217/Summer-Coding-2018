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
def howManyGoodSubarrays2(A, m, k):
    cache = [[-1 for i in range(len(A))] for i in range(len(A))]
    count = 0
    # Return the number of good subarrays of A.
    for i in range(len(A)):
        for j in range(i,len(A)):
            if i == j:
                result = A[i]
            else:   
                result = cache[i][j-1]
                result *= A[j]
            cache[i][j] = result
            if result % m ==k:
                count +=1
    return count