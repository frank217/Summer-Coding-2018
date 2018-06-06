
"""
Sheokand and String
Problem Code: SHKSTR
https://www.codechef.com/JUNE18B/problems/SHKSTR
"""

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




