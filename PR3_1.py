N = 10
a = [10, 15, 16, 143, 573, 1, 67, 58, 101, 34]

for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
 
print(a)
