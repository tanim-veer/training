
nombreMax = input("Jusqu'a quel nombre voulez-vous aller ? ")
nombrePair = 0
nombreImpair = 0

for i in range (1, int(nombreMax)+1):
    if i%2 == 0:
        nombrePair+=1
    else:
        nombreImpair+=1

print("Nombre de pairs : ", nombrePair)
print("Nombre d'impairs : ", nombreImpair)
