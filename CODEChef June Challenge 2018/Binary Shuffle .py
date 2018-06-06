
"""
Binary Shuffle 
Problem Code: BINSHFFL
https://www.codechef.com/JUNE18B/problems/BINSHFFL

Explanation :
------------------------------------------------------
There is certain formula for this problem.
With the 1 set of operation we can do two things.
1) increase number of 1 bits by 1.
2) decrease number of 1 bits from current value to any value 
   between current value and 1. 

With this speculation we can notice that this problem should 
be solved using number 1 bits in A and B.
c1A(count of 1bits in A)
c1B(count of 1bits in B)

In order to make a certain numbers into B we know that we have to 
reach a number B-1 because operation always require plus one to a value.

If B is odd, all we need to do is make A into the c1B-1 number of 1bits,
and do 1 operation to reach B. 
Therefor if c1A <= c1B -1  we only need to do (c1B-1)  - c1A to add that
many 1 bits to A.
If c1A > c1B-1 we only need one operation to decrease c1A 1bits 
to c1B-1 number of 1bits.
After this we only need to do 1 operation(add 1) to reach B.

If the B is even it's a we need one more thing to consider. 
Since B is even, B - 1 will create 1 bits equal 
to how many tailing 0 bits it have pluse c1B-1 becuase one 1bit
is consumed to make tailing 0 bits into 1. Exmaple: 10100 -1 = 10011.
since B-1 is odd not it is same as making what we did in odd bits 
with (c1B-1) + tailing 0 bits as c1B.

------------------------------------------------------
Number of operation 

c1B-1 >= c1A : odd = (c1B-1) - c1A + 1 =  c1B - c1A
             : even  = ((c1B-1) + tz) - c1A + 1 = c1B + tz - c1A

odd only needs to add 1 bits with difference of c1B -1 and c1A
because c1B -1 > c1A. Then add 1 to reach from B-1 to B
Even does same. Get c1B-1 + tz number of 1 bits from c1A then 
add 1 to reach from B-1 to B.

c1B-1 < c1A  : odd = 1 + 1  =  2
             : (even) if (c1B-1 + tz)-1 >= c1A needs to add 1bits (ec1B =(c1B-1 + tz)-1)                
                 ((ec1B - c1A + 1) + 1 = c1B + tz - c1A
               (even) otherwise needs to delete 1bits and and
                  1 + 1 = 2 (delete, add 1)

odd needs only deleting 1bits to c1B-1 and adding 1 which is only 2 operation.
even is complecated because of tailing zero. 
B-1 has (c1B-1 + tz) = ec1B 1 bits and B-1 is odd.
If ec1B -1 <= c1A we need to add 1 bits. which is same operation we did above.
otherwise we delete 1 bits to make this B-1 then add 1 once more to make it B. 


Rumtime : O(T)
------------------------------------------------------
T =10^5
0 < A,B ≤ 10^18

for each task it takes constant time operation
because it is all discrete mathematic that all 
depends on number of digits of A and B 
so O(T) * O(1) = O(T)


So lets implements this.
"""
 
def binaryShuffle(a,b):
    # print("a",a,"b",b)
    if a == b :
        return 0
    if b <= 1:
        return -1
    
    binA = bin(a)[2:]
    binB = bin(b)[2:]
    tz = 0
    index = len(binB)-1
    while True:
        if binB[index] == "0":
            tz +=1
            index -=1
        else:
            break

    c1A = binA.count("1")
    c1B = binB.count("1")
    # print (binA,binB,c1A,c1B,tz)
    if c1B - 1 >= c1A:
        if binA[-1] == "1":
            return c1B-c1A
        else:
            return c1B-c1A + tz
    else:
        if binB[-1] == "1":
            return 2
        else:
            ec1B = c1B - 1 + tz
            if ec1B == c1A:
                return 1
            elif ec1B > c1A:
                return c1B + tz - c1A
            else:
                return 2
    


print (1,5,binaryShuffle(1,5),1)
print (2,4,binaryShuffle(2,4),2)
print (5,1,binaryShuffle(5,1),-1)
print (4,1,binaryShuffle(4,1),-1)
print (5,1,binaryShuffle(3,1),-1)
print (5,3,binaryShuffle(5,3),2)
print (2,7,binaryShuffle(2,7),2)
print (7,2,binaryShuffle(7,2),2)
print (2,7,binaryShuffle(2,7),2)
print (15,12,binaryShuffle(15,12),2)
print (15,24,binaryShuffle(15,24),1)
print (6,28,binaryShuffle(6,28),3)
print (15,16,binaryShuffle(15,16),1)
print (16,15,binaryShuffle(16,15),3)
print (12,3,binaryShuffle(12,3),2)

# n = int(input())
# for i in range(n):
#     a,b = list(map(int, input().split(" ")))
#     result = binaryShuffle(a,b)
#     print(result)
