import sys

maxLength = 56.0
maxWidth = 45.0
maxDepth = 25.0
total = 125.0
maxWeight = 7.0

counter = 0

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

del lines[0]

for line in lines:
    value = list(map(float, line.split()))
    valueTotal = value[0] + value[1] + value[2]
    if(value[0] <= maxLength and value[1] <= maxWidth and value[2] <= maxDepth or valueTotal <= total):
        
        if(value[3] <= maxWeight):
            print(1)
            counter = counter + 1
        else:
            print(0)
    else:
        print(0)
    
print(counter)