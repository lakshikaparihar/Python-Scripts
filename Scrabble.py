'''
When playing Scrabble©, each player draws 7 letters and must find a word that scores the most points using these letters. A player doesn't necessarily have to make a 7-letter 
word; the word can be shorter. The only constraint is that the word must be made using the 7 letters which the player has drawn. For example, with the letters  etaenhs,
some possible words are: ethane, hates, sane, ant. Your objective is to find the word that scores the most points using the available letters (1 to 7 letters).

Rules
In Scrabble©, each letter is weighted with a score depending on how difficult it is to place that letter in a word. You will see below a table showing the points
corresponding to each letter:
 

Letters	Points
e, a, i, o, n, r, t, l, s, u	 --------> 1
d, g	                         --------> 2
b, c, m, p	                   --------> 3
f, h, v, w, y	                --------> 4
k	                            --------> 5
j, x	                         --------> 8
q, z	                         --------> 10

The word banjo earns you 3 + 1 + 1 + 8 + 1 = 14 points.

A dictionary of authorized words is provided as input for the program. 

* The program must find the word in the dictionary which wins the most points for the seven given letters 
* a letter can only be used once. 
* If two words win the same number of points, then the word which appears first in the order of the given dictionary should be chosen.
 

All words will only be composed of alphabetical characters in lower case. There will always be at least one possible word.

-------------------------------------------------------------||----------------------------------------------------------------
Game Input

Line 1: the number N of words in the dictionary
N following lines: the words in the dictionary. One word per line.
Last line: the 7 letters available.

Output
The word that scores the most points using the available letters (1 to 7 letters). The word must belong to the dictionary. Each letter must be used at most once in the solution. There is always a solution.
--------------------------------------------------------------||----------------------------------------------------------------


Example:
----------
Input    |
---------|
5        |
because  |
first    |
these    |
could    |
which    |
hicquwh  |
=========|
Output   |
---------|
which    |
----------

'''

sum = 0 
n = int(input())
w = list()
for i in range(n):
    w.append(input())
letters = input()
cmp = -1
for i in w:
    sum=0
    if False in [characters in list(letters) for characters in i]:
        pass
    else:
        for s in set(i):
            if s in ['e','a','i','o','n','r','t','l','s','u']:
                sum+=1
            elif s in ['d','g']:
                sum+=2
            elif s in ['b','c','m','p']:
                sum+=3
            elif s in ['f','h','v','w','y']:
                sum+=4
            elif s in ['k']:
                sum+=5
            elif s in ['j','x']:
                sum+=8
            elif s in ['q','z']:
                sum+=10

    if cmp<sum:
        cmp = sum
        word = i

seen = word[0]
ans = word[0]
for i in word[1:]:
   if i != seen:
      ans += i
      seen = i

if ans in w:
    print(ans)
else:
    print(word)
