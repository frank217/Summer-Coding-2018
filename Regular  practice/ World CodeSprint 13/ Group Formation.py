"""
World Code sprint 13
Group formation(medium)

Detail :
https://www.hackerrank.com/contests/world-codesprint-13/challenges/group-formation/problem

Expected output:
C
D
E
_______
C
D
E
F
G
_______
no groups
_______
Hulk
IronMan
SpiderMan
Thor
"""


"""
Runs in 
assessing input is O(n)
making group:
for each value in m
Case 1: Student in same group. DO nothing
    O(0)
Case 2: Converging two group if condition met  (both student in different group)
    Maximum groupsize + constant addtion and look up in set
    O(b) + O(1) = O(b)
Case 3: Add a student to  a group (one is in the group the other is not)
    constant look up in the set and ditionary
    O(1)
Case 4: Make a new group (Both not in same group)
    Constant time to make a new group
    O(1)

So runtime analysis give about O(m * b) in the worst case which is 
5 * 10^4  * 200 = 10^7
which is fast enough.

"""

def membersInTheLargestGroups(n, m, a, b, f, s, t):
    """
    n = number of 
    """
    grade = {}
    group = {}
    gnum = 0
    ass = {}
    gradeEval = {"1" : f, "2" : s,"3" : t}
    for i in range(n):
        person, g = input().split()
        grade[person] = g
        ass[person] = -1
    
    for i in range(m):
        
        person, desire = input().split()
        # print(person,desire)
        py = ass[person]
        dy = ass[desire]
        # print (py, dy)
        # Both assigned to same group
        if py != -1 and py == dy:
            # print ("case 1")
            continue
        # Both assigned but to different group. Converge if possible
        elif py!= -1 and dy !=-1:
            # print("case 2")
            
            # sum of two group is less then max group count
            if (len(group[py]["set"]) + len(group[dy]["set"])) <= b:
                #Converge the two
                gadd = group[dy]
                gori = group[py]
                if gadd["1"] + gori["1"] > f:
                    break
                if gadd["2"] + gori["2"] > s:
                    break
                if gadd["3"] + gori["3"] > t:
                    break
                gori["set"] = gori["set"] | gadd["set"]
                gori["1"] += gadd["1"]
                gori["2"] += gadd["2"]
                gori["3"] += gadd["3"]
                del group[dy]
            # Condition failed along the way move on
            continue
        # If one is already in the group and the other is not
        elif py!= -1 or dy !=-1:
            # print("case 3")
            # Decide which one is in the group
            if py != -1:
                gori = group[py]
                sadd = desire
                yy = py
            else:
                gori = group[dy]
                sadd = person
                yy = dy
            
            #Break condition 1 : group is at maximum count 
            if len(gori["set"]) >= b:
                continue
            #Break condition 2 : grade is at maximum count
            if gori[grade[sadd]] >= gradeEval[grade[sadd]]:
                continue
            # Good to add this student to set and add 1 to grade
            gori["set"].add(sadd)
            gori[grade[sadd]] += 1
            ass[sadd] = yy
        
        # Both is not in the group. Make a new group
        else:
            # print("case 4")
            group[gnum] = {"set": set([person,desire]),"1":0,"2":0,"3":0}
            group[gnum][grade[person]] += 1
            group[gnum][grade[desire]] += 1
            ass[person] = gnum
            ass[desire] = gnum
            gnum += 1
    # print (group)
    #Now loop through group that satifiest the condition(max student count and above min)
    maxcount = 0
    result = []
    for i in group.values():
        lset = len(i["set"])
        if lset > maxcount:
            maxcount = lset
            result = [i["set"]]            
        elif lset == maxcount:
            result.append(i["set"])
    if maxcount < a:
        print ("no groups")
        return 
    ans =[]
    for i in result:
        ans += list(i)
    ans.sort()
    for i in ans:
        print(i)
    return ans