import sys

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

del lines[0]
 
for line in lines:
    value = list(map(int, line.split()))
    percentage = 0
    iterator = 1
    iterator2 = 1
    aboveAverage = 0
    while(iterator < len(value)):
        percentage = percentage + value[iterator]
        iterator = iterator + 1
    percentage = percentage / value[0]

    while(iterator2 < len(value)):
        if(value[iterator2] > percentage):
            aboveAverage = aboveAverage + 1
        iterator2 = iterator2 + 1

    aff = '{:.3%}'.format(aboveAverage  / value[0])

    print(aff)