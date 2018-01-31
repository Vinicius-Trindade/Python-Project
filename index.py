def func1(x, y, z):
    print("example")
    return x * y * z
print(func1(3, 4, 5))

b = [1, 2, 3]
total = 0
for a in b:
    total = total + a
print(total)

a = list(range(1, 100))
for  ß in a:
    if ß % 3 == 0:
        print("Multiplo de 3")
        print(ß)
    elif ß % 5 == 0:
        print("Multiplo de 5")
        print(ß)
