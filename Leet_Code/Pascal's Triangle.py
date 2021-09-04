#n = input('numbers:')
list_P = []
for i in range(5):
    list_P.append([])
    for j in range(i+1):
        if j == 0 or i==j:
            list_P[i].append(1)
        else:
            list_P[i].append(list_P[i-1][j-1] + list_P[i-1][j])
print(list_P)
print(list_P[4])