#select a random word from a file

import os
import random

f = open('spword.txt','w')

for i in range(random.randint(0,10)):
    word = []
    for j in range(random.randint(1,10)):
        k=random.randint(1,26)
        k=k+64
        #print(k)
        word.append(chr(k))
    #print(word)
    x=''.join(word)
    x=x+'\n'
    print(x)
    f.write(x)
f.close()

f = open('spword.txt','r')
x=f.readline()
count=0
while x:
    count=count+1
    x=f.readline()
f.close()

k=random.randint(1,count)
print(k)
f = open('spword.txt','r')
x=f.readline()
count=1
while x:
    if count==k :
        print(x)
        f.close()
        break
    x=f.readline()
    count=count+1
