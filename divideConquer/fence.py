# Conquer and divide

"""
Fence with maximum box.

Given array of fences with height
Find the largest retangular box that can be fit in the fences.
# The fence can't be tilted.

Divide and conquer the problem.
1) get the max value from left and right half.
2) Check if there exist the box that can be maximum across right and left

Return the max value among the three. 

Input : fence.txt
3
7
7 1 5 9 6 7 3
7
1 4 4 4 4 1 1
4
1 8 2 2

Expected Output : 
20
16
8
"""

def fence(left, right, fences):
    # print (left, right)
    # Base case
    if (left == right):
        # print("In the base case : ", fences[left])
        return fences[left]
    mid = int((left + right)/2)

    #Get the Best value from both the left and right subproblem.
    result = max(fence(left, mid,fences), fence(mid+1, right, fences))

    # print ("checking both box : ", left, right,result)
    #Check if the Box across both half can be maximum
    low = mid
    hi = mid + 1
    height = min(fences[low], fences[hi])
    result = max(result, height *2)
    while (left < low or  hi < right):
        # Get the higher height first.(Also if left = low)
        if (hi < right and (fences[low] < fences[hi] or left==low)):
            hi += 1
            height = min(height, fences[hi])
        else:
            low -= 1
            height = min(height, fences[low])
            
        result = max(result, height * (hi - low + 1))
        # print ("result", result, low, hi, height)
    return result
    

f_out = open('fenceOutput.txt', 'w')
f_in = open('fence.txt', 'r')
# print (f_in.readlines())
lines = [line.strip() for line in f_in.readlines()][0:]
# print (lines)

for case in range(int(lines[0])):
    numFences = lines[case*2 + 1]
    fences = [int(i) for i in lines[case*2 +2].split(" ")]
    # print (numFences, fences)
    result = fence(0, int(numFences)-1, fences)
    print (result)

f_out.close()







