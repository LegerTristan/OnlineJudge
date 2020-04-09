import sys

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

for line in lines:
    tot = list(map(int, line.split()))

    if(len(tot) > 1):
        rsltt = (tot[0] == tot[1])

        if(rsltt):
            print("=")

        else:
            rsltt2 = (tot[0] < tot[1])

            if(rsltt2):
                print("<")
            
            else:
                print(">")