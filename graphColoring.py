import sys

n,m = map(int,input().split())

nodes = [[] for y in range(n)]

for x in range(m):
    a,b=map(int,input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)
    
seen = set()
seen.add(0)
nextUp = [] #this includes (node, steps)
steps = 0
cur = 0

while cur != n-1:
    for x in nodes[cur]:
        if x not in seen:
            nextUp.append( (x,steps+1) )
            seen.add(x)
    cur,steps = nextUp.pop(0)
print(steps-1)