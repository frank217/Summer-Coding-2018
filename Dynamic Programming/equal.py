# Conquer and divide

"""
Equal

https://www.hackerrank.com/challenges/equal/problem

Since add to all but one is same as minus to one value,
find the lowest value and check how many operation it 
takes to make all the value same with just minus.

* Need to check min value ~ min value -1 because 
it may take less operation.
EXample 
1 3 3 3 7 
It is better to set all value to 0 rather than 1.
There is no point for any value below min value -1 
because that processs can be done 

"""

def equal(arr):
    mval = min(arr)
    result = float("inf")
    for m in range(mval, mval-2, -1):
        temp = 0
        for i in arr:
            dif = i - m 
            if dif>= 5:
                temp += int(dif/5)
                dif = dif%5
            if dif >= 3:
                temp += int(dif/3)
                dif = dif%3
            if dif>= 1:
                temp += dif
                dif = 0
        result = min(temp, result)
    return result


    

# f_out = open('triangleOutput.txt', 'w')
# f_in = open('trianglepath.txt', 'r')
# # print (f_in.readlines())
# lines = [line.strip() for line in f_in.readlines()][0:]
# # print (lines)
# cur = 1
# for case in range(int(lines[0])):
    
#     n = int(lines[cur])
#     cur +=1
    
#     board = []
#     for i in range(n):
#         line = lines[cur+i].split(" ")
        
#         board.append([int(i) for i in line])
#     cur += n

#     cache = [[-1 for i in range(len(board))] for i in range(len(board))]
#     # print (n, board,cache)
#     result = path(board,0,0, cache)
#     # print (cache)
#     print (result)
#     # break

# f_out.close()








