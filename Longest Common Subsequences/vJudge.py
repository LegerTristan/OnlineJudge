import sys
i = 0

lines = sys.stdin.readlines()
while (lines[-1] == '\n'):
    del lines[-1]



while i < len(lines):
    
    ligne1 = lines[i]
    ligne2 = lines[i + 1]

    i = i + 2
    matrice = [[0 for j in range(len(ligne2))] for k in range(len(ligne1))]

    for j in range (0, len(ligne1)):  
        
        for k in range (0, len(ligne2)):

            if j == 0 or k == 0:
                matrice[j][k] = 0
            elif(ligne1[j-1] == ligne2[k-1]):

                matrice[j][k] = matrice[j - 1][k - 1] + 1
            else:
                tab = []
                tab.append(matrice[j - 1][k])
                tab.append(matrice[j][k - 1])
                matrice[j][k] = max(tab)
            
    print(matrice[j][k])
