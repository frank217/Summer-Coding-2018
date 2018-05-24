# Conquer and divide

"""
JumpGame.

Given  n x n board with a number 1 ~ 9 in each
panel, a player try to move from topleft corner
to bottom right corner. The number on panel mean
how many blocks a Player can move down or right.
Can player reach the end?

Input : fanmeet.txt
4
FFFMMM
MMMFFF
FFFFF
FFFFFFFFFF
FFFFM
FFFFFMMMMF
MFMFMFFFMMMFMF
MMFFFFFMFFFMFFFFFFMFFFMFFFFMFMMFFFFFFF

Expected Output : 
1
6
2
2

"""

def jump(board,x,y,cache):
    n = len(board)
    if y >= n or x >= n:
        return 0
    if y == n - 1 and x == n-1 :
        return 1
    result = cache[x][y]
    # If there was cached info use it
    if result != -1:
        return result
    # If no cache find the value
    jumpsize = board[x][y]
    result = (jump(board, x + jumpsize, y, cache) or jump(board,x, y+jumpsize, cache))
    cache[x][y] = result
    return result

    

f_out = open('jumpOutput.txt', 'w')
f_in = open('jump.txt', 'r')
# print (f_in.readlines())
lines = [line.strip() for line in f_in.readlines()][0:]
# print (lines)
cur = 1
for case in range(int(lines[0])):
    
    n = int(lines[cur])
    cur +=1
    
    board = []
    for i in range(n):
        line = []
        for j in lines[cur+i]:
            line.append(int(j))
        board.append(line)
    cur += n

    cache = [[-1 for i in range(len(board))] for i in range(len(board))]
    # print (board,cache)
    result = jump(board,0,0, cache)
    print (cache)
    print (result)
    # break

f_out.close()








