print(" '' ")
print(" \" \' ")
print("első sor\n\nmásodik sor")

print("Ez egy szöveg", end=". . . .")
print("Ez egy szöveg,","ez meg egymásik", end=". . . .\n")

print("egy", "kettő", "három", sep="/")

print(0.0000000000000000000001)
print(1.0000000000000000000001)

print(2**2**3)
print(2**(2**3)) #a kettő megegyezik

print(2/3)
print(2//3)

print(-2)

print("példák")
print("1)",2 * 3 % 5)
print("2)",(5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print("3)",(2 ** 4), (2 * 4.), (2 * 4))
print("4)",(-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print("5)",(2 % -4), (2 % 4), (2 ** 3 ** 2))


my_number = 1
print("elso:{}".format(my_number))
print(f"elso: {my_number}")

#for ciklus
for i in range(5):
    print(i)
print("\n")
for i in range(2,5):
    print(i)

print("\n")
for i in range(0,10,2):
    print(i)
print("\n")
for i in range(0,10,-1): #el sem indul a ciklus
    print(i)

#"foreach"
lista1 = ["a", "b", "c", "d"]
for x in lista1:
    print(x)

#while
i = 20
while i > 0:
    print(i)
    i -= 2


#lista apróság

lista1 = ["a", "b", "c", "d"]
print(lista1[3])
print(lista1[1:])
print(lista1[:1])
print(lista1[1:3])

#lista negatív index

print(lista1[-1])
print(lista1[:-10])