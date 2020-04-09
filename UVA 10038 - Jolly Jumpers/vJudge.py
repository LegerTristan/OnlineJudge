import sys

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

for line in lines:
    tabJolly = set()
    value = list(map(int, line.split()))

    if(len(value) != 0):
        if(len(value) == 2):
            if(value[1] == 1):
                print('Jolly')
        else:
            nbElem = value[0]

            for iterator in range(1, nbElem):
                valeur = abs(value[iterator] - value[iterator + 1])
                tabJolly.add(valeur)

            jolly = True

            for iteratorJolly in range(1, nbElem):
                if iteratorJolly not in tabJolly:
                    jolly = False
                    break
            
            if jolly == True:
                print('Jolly')
            else:
                print('Not jolly')
