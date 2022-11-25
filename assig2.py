from math import inf

with open('assignment02-1.txt', 'r') as file:
# with open('assignment02-2.txt', 'r') as file:
    l = int(file.readline())
    t = (file.readline())
    a = t.split(' ')
    a = [int(x) for x in a]


def mindis(a):  
    minimum = inf
    for i in range (l):
        for j in range (i+1,l):
            if a[i]==a[j]:
                minimum=min(minimum,j-i)
    if minimum == inf:
        return -1
    else: 
        return minimum

print(mindis(a))
