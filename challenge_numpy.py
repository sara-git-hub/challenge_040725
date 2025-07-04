# Challenge : Analyse de Températures

import numpy as np

temperatures= np.array([27,30,40,25])
print(f"Moyenne: {np.mean(temperatures)}")
print(f"Median: {np.median(temperatures)}")
print(f"std: {np.std(temperatures)}")
print("\n")

#Challenge : Normalisation de Données

tableau1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"tableau  non normalisé:{tableau1}")
m=np.mean(tableau1)
print(m)
s=np.std(tableau1)
tableau1=(tableau1-m)/s
print(f"tableau normalisé:{tableau1}")
print("\n")

#Challenge : Comparaison de Tableaux

tableau2=np.array([[1,2,3],[4,5,6],[7,8,9]])
tableau3=np.array([[1,2,3],[10,5,6],[20,8,9]])
diff=np.where(tableau2!=tableau3,1,0)
print(diff)
for i in range(3):
    for j in range (3):
        if diff[i][j]==1:
            print(f"indices[{i}],[{j}] tableau2: {tableau2[i][j]} tableau2: {tableau3[i][j]}")

#Challenge : Opérations Matricielles

matrice1=np.array([[1,4,3],[4,5,8],[1,8,9]])
matrice2=np.array([[1,2,3],[10,5,6],[20,8,9]])

matrice3=np.dot(matrice1,matrice2)
print(matrice3)

matrice1_transpose=matrice1.T
print(matrice1_transpose)

matrice1_inverse=np.linalg.inv(matrice1)
print(matrice1_inverse)
print(np.dot(matrice1,matrice1_inverse))
print("\n")


#Challenge : Sélection Basée sur Conditions

matrice_cond=np.array([[1,4,6],[8,10,12],[14,16,18]])

matrice_sup=np.where(matrice_cond>10,1,0)

print(matrice_sup)

valeurs_sup=matrice_cond[matrice_sup>0]

print(valeurs_sup)
