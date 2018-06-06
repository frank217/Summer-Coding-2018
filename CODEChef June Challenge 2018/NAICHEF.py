# Conquer and divide

"""
Naive Chef

https://www.codechef.com/JUNE18B/problems/NAICHEF


Input : 




"""

def naichef(dice ,a,b):
    countA = 0
    countB = 0
    for i in dice:
        if a == i:
            countA+=1
        if b == i:
            countB+=1
    return (countA/len(dice))*(countB/len(dice))
    
 
# n = int(input())
# for i in range(n):
#     s,a,b = list(map(int, input().split(" ")))
#     dice =  list(map(int, input().split(" ")))
#     result = naichef(dice, a,b)
#     print(result)


"""
Binary Shuffle 
Problem Code: BINSHFFL
https://www.codechef.com/JUNE18B/problems/BINSHFFL

Explanation :
------------------------------------------------------
There is certain formula for this problem.
With the 1 set of operation we can do two things.
1) increase number of 1 bits by 1.
2) decrease number of 1 bits from current value any value 
   between current value and 1. 

With this speculation we can notice that this problem should 
be solved using number 1 bits in A and B.
c1A(count of 1bits in A)
c2B(count of 1bits in B)

Inorder to make a certain number into B we know that we have to 
reach a number B-1 because operation always require plus to a value.
So if the B is odd. All we need to do is make A into the c2B-1 number of 1bits.
Therefor if c1A < c2B -1  we only need to do (c2B-1)  - c1A to add that
many 1 bits to A. 
If c1A > c2B-1 we only need one operation to decrease c1A 1bits 
to c2B-1 number of 1bits.
After this we only need to do 1 operation(add 1) to reach B.

If the B is even it's a we need one more thing to consider. 
Since B is even if we -1 to B, it will create 1 bits equal 
to how many tailing 0 bits it have. So now it is same as
making odd bits with (c1B-1) + tailing 0 bits.

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



"""
Naive version : 
for each querie
run through all the possible string and find the word
with longest common prefix that is lexicographically smallest.


Runtime : O(q * n * 10) = O(10^11) 
This only passes on the samll inputcase 

"""
def sheokand(strings,r, querie):
    # print (strings,r,querie)
    maxl = 0
    word = strings[0]
    for i in range(r):
        string = strings[i]
        index = 0
        while index < len(string) and index < len(querie):
            if string[index] == querie[index]:
                index +=1
            else:
                break
        # print(string, index)
        if maxl == index+1:
            word = min(string, word)
        elif maxl < index+1:
            maxl = index + 1
            word = string
    return word
# strings = ["abcd","abce","abcdex","abcde"]
# print(sheokand(strings,3,"abcy" ))
# print(sheokand(strings,3,"abcde" ))
# print(sheokand(strings,4,"abcde" ))
# print(sheokand(strings,4,"ab" ))
# 3 abcy
# 3 abcde
# 4 abcde


"""
**** Only works on  cases : WA
Better version:
Stores each string in to dictionary so that we can
decrease search space as we proceed with the given value.
Since limit is 

Strings : 1≤N≤100,000
length of string : 1≤|Si|≤10 for each valid i
Queries : 1≤Q≤100,000
R = upto what index we can use in strings to search.
 1≤R≤N
P = word given to search for longest common prefix
1≤|P|≤10

creating each dictionary will O(n*si) = O(n)

*** if dictionary is created every time it will be O(n * q) = 10 ^ 10
    which will be too slow
*** only create dictionary once.

Search will be O(Si) because depth of dictionary will be Si.
And bfs on the remain dictionary to find lexicographically
smallest one will take O(n*Si) = O(n)

Which should be fast enough for large input as well.

"""
def sheokand2(dic, querie):
    # print(querie,strings)

    # print(querie,dic)
    #search for queries
    curdic = dic
    word = ""
    for i in querie:
        if i in curdic :
            word += i
            curdic = curdic[i]
        else:
            break
    # print(word,curdic)
    # print("GETREM")
    word += getrem(curdic)    
    return word

def getrem(curdic):
    if "end" in curdic:
        return ""
    key = list(curdic.keys())
    # print("key", key[0])
    word = key[0] + getrem(curdic[key[0]]) 
    # print (word, curdic)
    for i in key[1:]:
        newword = i + getrem(curdic[i])
        # print(word, newword)
        word = min(word, newword)
    return word
import copy

def makedic(strings, queries):
    # Use set because look up takes O(1) where as list is O(n)
    dic = {}
    listdic = []
    for i in range(len(strings)):
        string = strings[i]
        curdic = dic
        for j in string:
            if j in curdic:
                curdic = curdic[j]
            else:
                curdic[j] = {}
                curdic = curdic[j]
        curdic["end"] = i
        listdic.append(copy.deepcopy(dic))
    for qq in queries:
        r , q = qq
        print (sheokand2(listdic[r-1],q))
    return


# strings = ["abcd","abce","abcdex","abcde"]
# queries = [(3,"abcy"),(3,"abcde"),(4,"abcde"),(4,"ab"),(4,"a"),(4,"aa"),(4,"b")]
# print("ANSWER :",makedic(strings,queries ))
# print("ANSWER :",input(strings,3,"abcde" ))
# print("ANSWER :",input(strings,4,"abcde" ))
# print("ANSWER :",input(strings,4,"ab" ))
# print("ANSWER :",input(strings,4,"a" ))
# print("ANSWER :",input(strings,4,"aa" ))

# print("ANSWER :",input(strings,4,"b" ))


# 4
# abcd
# abce
# abcdex
# abcde
# 3
# 3 abcy
# 3 abcde
# 4 abcde

# n = int(input())
# strings = []
# for i in range(n):
#     strings.append((input()))
# q = int(input())
# queries = []
# for i in range(q):
#     r, querie = input().split(" ")
#     queries.append((int(r),querie))
# makedic(strings,queries)




