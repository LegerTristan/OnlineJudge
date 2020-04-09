import sys

dictionnary = {}

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

for line in lines:
    value = list(map(str, line.split(" ")))
    if(len(value) > 1):
        dictionnary[value[1]] = value[0]
        
    elif(value[0] != '\n'):
        if(value[0] in dictionnary):
            print(dictionnary[value[0]])
        else:
            print('eh')