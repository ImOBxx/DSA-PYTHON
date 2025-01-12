from collections import deque 

class MyDs:
    def __init__(self):
        self.dq = deque()

    def insertMin(self, x):
        self.dq.appendleft(x)

    def insertMax(self, x):
        self.dq.append(x)

    def extractMin(self):
        self.dq.popleft()

    def extractMax(self):
        self.dq.pop()

    def getMin(self):
        return self.dq[0]
    
    def getMax(self):
        return self.dq[-1]
    
    def printds(self):
        print(self.dq)

d = MyDs()
d.insertMin(10)
d.printds()
d.insertMin(5)
d.printds()
d.insertMax(20)
d.printds()
d.insertMin(3)
d.printds()
print(d.extractMin())
d.printds()
print(d.extractMax())
d.printds()
print(d.getMin())
print(d.getMax())
d.printds()

