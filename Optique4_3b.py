from itertools import product

couches = [1, 2, 3, 4, 5, 6]

permutations = product(couches, repeat = 3)
# print(list(permutations))

indices = {1: 1.36, 2: 1.45, 3: 1.65, 4: 2, 5: 2.2, 6: 2.3}

n0 = 1
ns = 1.5

possibilities = []

def R(couches):
    n1 = indices[couches[0]]
    n2 = indices[couches[1]]
    n3 = indices[couches[2]]

    num = n0*ns*n2/(n1*n3) - n1*n3/n2
    den = n0*ns*n2/(n1*n3) + n1*n3/n2

    ref = abs(num/den)
    return ref

best = (1, 1, 1)

for i in list(permutations):
    if R(i) < R(best):
        best = i
    if R(i) < 0.001:
        possibilities.append(i)
        

print(f"Les possibilités sont: {possibilities}")
print(f"La meilleure combinaison est {best} avec R={R(best)}")