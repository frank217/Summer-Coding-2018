"""
Construct Array 

Difficulty : Medium

Detail :
https://www.hackerrank.com/challenges/construct-the-array/problem

Solution (DP): 
Limits 
1) Numbers can't be consecutive
2) Always start with 1
3) Always ends with given x


Base case :
n = 2 and x = 1:
0 possibility

n = 2 and x !=1:
1 possibility 

Recursive Case:
endWithX(n) = endWithAny(n-1) - endWithX(n-1)
endWithAny(n) = (k-1)^(n-1)
*** Look at explanation for how this is derived


Explanation:
In order to get array with lenght n with k numbers that ends in x
We need to know the number of array that can be formed with
lenght n -1 and doesn't ends with x.
Which is same ans "array that ends with any number" - "array that ends with x" 

Then we need number of array that can be formed with length n - 1
and k numbers which can be derived with simple multiplication.

First number needs to be 1.
so second number can be k-1 possible numbers.
Then third number can be k-1 possible number wasn't a second number.
Then nth number can be k-1 possible number as well.
So equation comse where 
1 * (k-1) .... (k-1) * (k-1) = (k-1)^(n-1)


Then number of array that ends with x can be found recursively
using the formulat attained above.



Input :
761 99 1
1000 100 1
17048 14319 1

Expected output:
236568308
43813792
803254122
"""


mod = 10**9 + 7
"""
Naive recursive version:
Too slow because anyend is calculated multiple time
again and again.
"""
def countArray(n, k, x):
    if n == 2:
        if x !=1:
            return 1
        return 0
    anyend = (k-1)**(n-2)
    withX = countArray(n-1,k,x)
    # print("CountArry :", n,k,x)
    # print ("n", n, anyend, withX)
    return  (anyend - withX)

"""
Better version:
Use DP or 
start from smaller value to larger value.
So Caculating any n length with k possible ending in any value
is not repeated
"""
def countArray2(n, k, x):
    
    """
    If length = 2 any number composition that
    start with 1 and end with 1 will be 0.
    Any other number ending will be 1.
    """
    prevany = 1
    if x == 1:
        prevwith = 0
    else:
        prevwith = 1
    # Start with n = 3
    for i in range(2,n):
        prevany =(prevany * (k-1)) % mod
        # print ("n",i +1,"any",prevany, "with", prevwith  )
        prevwith = (prevany - prevwith) % mod
        # print ("cur", prevwith)
    return  prevwith
