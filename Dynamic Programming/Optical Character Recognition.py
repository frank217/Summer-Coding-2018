
"""
OCR (Hidden Markov Model)
Difficulty : high

Given a String of words find the sentence that has the highest probability
after running Optical Character Recognition.

Given a string of words Optical character recognition
checks what this strings of words should have been given,
probability of each word starting the sentence,
probability of a word appearing after certain words,
probability that a word will be recognized as other words.

Input 
first line is number of words m(1≤ m ≤ 500) appearing in the sentence and 
number of sentences q(1≤ q ≤100)
Second line is m words
Third line is probability each word is at the begining of sentence.
Consequent m line is probability of each word appearing after ith word.
Then, next consequent m line is probability of each word recognized as other m words.  
Next consequent q line is number of word in input sentences ans string sentence.

Input : 
5 3
I am a boy buy
1.0 0.0 0.0 0.0 0.0
0.1 0.6 0.1 0.1 0.1
0.1 0.1 0.6 0.1 0.1
0.1 0.1 0.1 0.6 0.1
0.2 0.2 0.2 0.2 0.2
0.8 0.1 0.0 0.1 0.0
0.1 0.7 0.0 0.2 0.0
0.0 0.1 0.8 0.0 0.1
0.0 0.0 0.0 0.5 0.5
0.0 0.0 0.0 0.5 0.5
4 I am a buy
4 I am a boy
4 I am am boy



Output:
I am a boy
I am a boy
I am a boy
"""

"""
Solution:
This a Marvok model problem with Bayes theorem.

So The to find the maximum probability, we use Bayes theorem.
Given sentence R find the most probable sentence Q. 
We want max value this, which is represented as
Max value of P(Q|R), probability of Q given R

Using Bayes theorem, we get.
P(Q|R) = P(R|Q) * P(Q)/ P(R)

We should assume P(R) is same for Q, so we just need to find
maximum P(R|Q) * P(Q)

n = number of words in R
P(R|Q) = probabily of translator converting Q to R which is 
for every word in Q multiply probability that Q[i] is translated to R[i]
Lets simplify this to M(Q,R)

P(Q) = probability that sentence Q will appear. Assuming that 
this sentence Q is created by markov model.

P(Q) = probability Q[0] is start of setence * for every word after Q[0],
multiply probability of Q[i] leading to Q[i+1].
Lets simplify this to T(Q,Q1)

Now P(Q|R) can be achieved.



########
DP to cache data.


Base case:
No word left in the sentence
Return 0

Recursive case:
recognize(curindex,prevWord) = 
max (for t in index after given curent index : recogize(s+1,t)*g(t))
"""

def recognize(index, prev):
    #Base case
    if index == n:
        return 0
    if cache[index][prev]:
        return cache[index][prev]
    
    result = cache[index][prev]
    choosen = picked[index][prev]

    for i in range(0,m):
        curResult = translateP[prev][i] + consequentP[i][R[index]] + recognize(index+1,i)
        if curResult > result:
            result = curResult
            choosen = i
    return result

def track(index,prev):
    choosen = picked[index][prev]
    return words[choosen] + " " + track(i,choosen)

    

    

m, query = list(map(int,input().split(" ")))
words =  input().split(" ")
consequentP = []
translateP = []

for i in range(m+1):
    consequentP = list(map(int,input().split(" ")))
for i in range(m):
    translateP = list(map(int,input().split(" ")))
cache = {}
for i in range(query):
    temp = input().split(" ")
    n = int(temp[0])
    R = temp[1:]
    # cache = {}[[0 for j in range(len(array[i]))] for i in range(len(array))]
    result = recognize(0,0)
    picked = []
    print (track(0,0))

# print(cache)
