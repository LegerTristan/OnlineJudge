import sys

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

for line in lines:
    nbr = []
    nbr = line.strip().split(" ")
    rsltt = 0
    rsltt = abs(int(nbr[1])) - abs(int(nbr[0]))
    print(str(rsltt))