from collections import deque

def revQ(q):
    if (len(q) == 0):
        return 
    x = q.popleft()
    revQ(q)
    q.append(x)


q = deque()
q.append(1)
q.append(2)
q.append(3)

revQ(q)
print(q)