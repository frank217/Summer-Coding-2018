# Conquer and divide

"""
FanMeeting.

In this Fanmeeting the idol hugs fan,
but male idol will only handshake with male fan.
The fans will stand in a line in given order and 
fan meet the idol as in the given order and move to left.

Given array mixed idols(male and female)
and array of fans(male and femail)
Find number of occurence that all idol will be hugging.

Divide and conquer the problem using 
"Karatsuba fast multiply"

Solution : 
1) Only case that handshake occurs is when 
male idol meets male fan. So if we assume male to be "1"
and female to be "0" only the number of handshake will become 1.
So if we do the conversion and multiply idol and fan, each digit
in result of multiplication will imply how many handshake has 
occured in the status. To be more clear look at example below

                          A2    A1    A0
    *   B5    B4    B3    B2    B1    B0
    -------------------------------
                         A2*B0 A1*B0 A0*B0
                   A2*B1 A1*B1 A0*B1
             A2*B2 A1*B2 A0*B2
       A2*B0 A1*B3 A0*B3
 A2*B0 A1*B0 A0*B0
~
    -------------------------------
~ C6    C5    C4    C3    C2    C1    C0

So Ci imply sum of all state of fan and idol interacting
and only male coupling will give 1 so if the value of 
Ci = 0 that means at that given state there is no 
hand shaking. 

Although watch out that one needs to exclude the cases when
not all the memebers are in contact with fans. If not, there
can be situation where Ci = 0 but not all idol member is 
with the fan.  

* Implementation detail : 
Since idol meets fans from left and 
fans meets idol from right, the fans needs to be
in reverse order. 

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

######### Start of karatsuba fast multiply 
def karatsuba(a,b):
    # Get the number of digit for a and b
    an = len(a)
    bn = len(b)
    
    # a needs to be longer than b
    if (an < bn):
        return karatsuba(b,a)
    # One of them has zero
    if(an==0 or bn == 0):
        return 0
    # if short no need for fast multiplication
    if(an <= 50):
        return multiply(a, b)

    half = int(an/2)

    a0 = int(a[:half])
    a1 = int(a[half:])
    b0 = int(b[:min(half, len(b))])
    b1 = int(b[min(half, len(b)):])

    z2 = karatsuba(a1,b1)
    z0 = karatsuba(a0,b0)
    z1 = karatsuba((a0+a1), (b0+b1)) - z0 - z2

    return z0 + (z1 * 10**(half)) + (z2 * 10**(half*2))      
    
def multiply(a,b):
    result = [0 for i in range(len(a)+len(b))]
    for i in range(len(a)):
        for j in range(len(b)):
            result[i+j] += a[i]*b[j]
    # normalize(result)
    # print ("multiply: ",result, a ,b)
    return result

def normalize(c):
    for i in range(len(c)-1):
        if c[i] >= 0:
            c[i+1] += int(c[i]/10)
            c[i] = c[i]%10
        else:
            borrow = int(abs(c[i]+9)/10)
            c[i+1] -= borrow
            c[i] += borrow *10
######### End of karatusba



def fanmeet(members, fanmeets):
    m = []
    f = []

    for i in members:
        if i == "F":
            m.append(0)
        else:
            m.append(1)
    for i in fanmeets:
        if i == "F":
            f.append(0)
        else:
            f.append(1)
    # Need to reverse the order of input because index
    # Corresponds to index of digit. (fans needs to be reversed so it is kept same)
    m = m[::-1]
    value = karatsuba(m,f)
    # print (m,f,value)
    result = 0
    
    # Get how many occurencess when every member does hug. 
    for i in range(len(m)-1, len(f)):
        # print (value[i], i)
        if value[i] == 0:
            result += 1
    
    return result
    

f_out = open('fanmeetOutput.txt', 'w')
f_in = open('fanmeet.txt', 'r')
# print (f_in.readlines())
lines = [line.strip() for line in f_in.readlines()][0:]
# print (lines)

for case in range(int(lines[0])):
    members = lines[case*2 + 1]
    fanmeets = lines[case*2 +2]
    # print (numFences, fanmeets)
    result = fanmeet(members,fanmeets)
    print (result)
    # break

f_out.close()








