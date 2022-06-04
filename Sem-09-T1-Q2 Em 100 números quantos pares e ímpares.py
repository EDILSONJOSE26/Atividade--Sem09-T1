x = []
par = []
impar = []

for numero in range(0, 100):
    x.append(int(input()))

for numero in range(0, 100):
    if x[numero] % 2 == 0:
        par.append(x[numero])
    else:
        impar.append(x[numero])
print(len(par))
print(len(impar))
