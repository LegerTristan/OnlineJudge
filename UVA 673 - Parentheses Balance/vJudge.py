import sys

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

del lines[0]

for line in lines:
    tabCarac = []
    
    for carac in line:
        if carac == '(' or carac == '[':
            tabCarac.append(carac)
            print(tabCarac)
        else:
            if(len(tabCarac) != 0):
                if(carac == ')' and tabCarac[len(tabCarac) - 1] == '('):
                    carac = tabCarac.pop()
                    print(tabCarac)

                if(carac == ']' and tabCarac[len(tabCarac) - 1] == '['):
                    carac = tabCarac.pop()
                    print(tabCarac)
            else:
                if(carac != '\n'):
                    tabCarac.append(carac)

    if len(tabCarac) == 0:
        print('Yes')
    else:
        print('No')
