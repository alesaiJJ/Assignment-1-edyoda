series = (4,6,2,5,1,7,8,80,81,83,82,9,6,5,4)
odd = 0
even = 0
for i in series:
    if i%2 == 0:
        even+=1
    else :
        odd += 1
print(f'the series has {odd} odd numbers')
print(f'the series has {even} even numbers')
