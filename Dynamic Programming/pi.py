
"""
Memorizing pi.

Given there is difficulty to memorize

Case                     | Example  | difficulty
------------------------------------------------
same numbers in a row    | 333,555  | 1
increment/decrement by 1 |23456,3210| 2
two repeating number     |323,54545 | 4
arithmatic sequence      | 147,8642 | 5
other                    | 17912,331|10

For a given input number we divide it by length between
3 to 5 inclusivly and add up the difficulty of each section.
Find the minimum difficulty for givin numbers

Input : 
5
12341234
11111222
12122222
22222222
12673939

Output:
4
2
5
2
14
"""

"""
Solution:

Base case:
length < 3 : return infinity 
lenght of 3 return its difficulty

Recursive case:
memoPi(index) = max of(
difficulty of length 3 section + minimum difficulty of rest of the section,
difficulty of length 4 section + minimum difficulty of rest of the section,
difficulty of length 5 section + minimum difficulty of rest of the section)

"""

def memoPi(index):
    if index == len(number):
        return 0
    # if data is cached:
    if cache[index]:
        return cache[index]
    elif len(number) - index <3:
        cache[index] = float("inf")
        return float("inf")
    
    result = float("inf")
    for i in range(3, min(len(number)- index,5)+1):
        result = min(result,memoPi(index+i) + getdif(number[index:index+i]))
        # print (index,i,len(number),result)
    cache[index] = result
    return result

def getdif(num):
    s = set(num)
    if len(s)== 1:
        return 1
    elif len(s) == 2:
        return 4

    p = num[0]
    inc = int(num[1])- int(num[0])
    for i in num[1:]:
        if inc != (int(i) - int(p)) :
            return 10
        p = i
    if inc ==1:
        return 2
    else:
        return 5



n = int(input())
for i in range(n):
    number = input()    
    cache = [0 for i in range(len(number))]
    result = memoPi(0)
    print(result)
