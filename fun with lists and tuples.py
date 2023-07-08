x = [(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j][-1] > x[j + 1][-1]:
            x[j], x[j + 1] = x[j + 1], x[j]
print(x)
