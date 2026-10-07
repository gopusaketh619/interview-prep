

a1 = [2,5,7]
a2 = [4,6,8,10,15]

ar = []

i = j = k = 0

while i < len(a1) and j < len(a2):
    if a1[i] < a2[j]:
        ar.append(a1[i])
        i = i+1
    else:
        ar.append(a2[j])
        j = j+1
    k = k + 1

ar.extend(a1[i:])
ar.extend(a2[j:])
      
print(ar)