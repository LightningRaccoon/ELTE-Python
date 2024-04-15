#típusok
a = 1
b = 1.5
igaz = False
szo = "asdf"
None

szo = '"'

#típus kasztolás
szoveg = '45'
print(int(szoveg) + 6)
int()
str()
bool()
float()
#komment
'''
több soros
komment
'''
"""
több soros
komment
"""
#adattárolók
#list
list = []
list.append(6)
list.append(6)
list.append(6)

list.append('szöveg')
print(list)

#tuple
tuple1 = (1, 2, 3)
tuple = (1, 'szoveg')

#dictionary - szótár
dictionary1 = {1:'alma','körte':5} #{kulcs:érték,kulcs:érték}
print(dictionary1)
print(dictionary1['körte'])

#változók
my_variable = 100
x = 100 #ez nem ajánlatos
ev, honap, nap = [2023, 'szeptember', 22] #bármilyen adatkollekció lehet a jobb oldalon
ev, honap, nap = 2023, 'szeptember', 22 #adattároló nélkül is lehet
print(ev, honap, nap)

my_variable = "string" #felül írható bármilyen változó

CONSTANT_VARIABLE = 500

#print
print(a,b,igaz)
print("Ez itt egy szöveg")
valtozo1 = "egy"
valtozo2 = "szöveg"
print(f"Ez itt {valtozo1} {valtozo2}")
print("Ez itt egy", valtozo2, "ez itt a folytatas")
print("Ez itt" + "egy" + "szöveg")

#függvények
def osszead(a, b):
    return a + b

def lista_elso_elem(list1):
    return list1[0], list1[1]

print(osszead(1,2))

print("lista első eleme:",lista_elso_elem([9,8,7]))

#input
nev = input()
nev = input("Add meg a neved:")

print(nev)

#operátorok
#matematikai +, -, /, *, **, % <- maradékos osztás
print("osztás",int(11/5)) #lefelé kerekít

#logikai ==, not, and, or, <=, >=



