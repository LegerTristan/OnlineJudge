import sys, heapq

iterator = 1
newIterator = 0
tabRegister = []
tabPeriod = {}

lines = sys.stdin.readlines()
while (lines[-1] == '\n'):
    del lines[-1]

for line in lines:
    ligne = list(map(str, line.split()))

    if(ligne[0] != '#'):
        
        tabPeriod[int(ligne[1])] = ligne[2]
        heapq.heappush(tabRegister, (int(ligne[2]), int(ligne[1])))
        iterator =  iterator + 1
    else:
        break
 
for i in range(iterator):
    del lines[0]

nbrIteration = int(lines[0])
while newIterator < nbrIteration:
    value = heapq.heappop(tabRegister)
    print(value[1])
    period = value[0] + int(tabPeriod[value[1]])
    heapq.heappush(tabRegister, (period, value[1]))
    newIterator = newIterator + 1
