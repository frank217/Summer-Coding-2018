# Conquer and divide

"""
Trianglepath.

Given numbers that forms triangle from top down.
Find a maximum value path from top to bottom.

Each position in the path should have a maximum
value path stored. So each path will only be
caculated once. 

Input : trianglepath.txt
2
5
6
1 2
3 4 7
9 4 1 7
2 7 5 9 4
5
1
2 4 
8 15 8
32 64 32 64
128 256 128 256 128


Expected Output : 
28
340
"""

def path(board,x,y,cache):
    # print(x,y, len(board))
    # Bottom row 
    if y == len(board)-1:
        return board[y][x]
    result = cache[y][x]
    if result != -1:
        return result
    result = max(path(board,x,y+1, cache), path(board,x+1,y+1, cache)) + board[y][x]
    cache[y][x] = result
    # print(x,y, result)

    return result


    

f_out = open('triangleOutput.txt', 'w')
f_in = open('trianglepath.txt', 'r')
# print (f_in.readlines())
lines = [line.strip() for line in f_in.readlines()][0:]
# print (lines)
cur = 1
for case in range(int(lines[0])):
    
    n = int(lines[cur])
    cur +=1
    
    board = []
    for i in range(n):
        line = lines[cur+i].split(" ")
        
        board.append([int(i) for i in line])
    cur += n

    cache = [[-1 for i in range(len(board))] for i in range(len(board))]
    # print (n, board,cache)
    result = path(board,0,0, cache)
    # print (cache)
    print (result)
    # break

f_out.close()








