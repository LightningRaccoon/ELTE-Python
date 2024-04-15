#slicing/copying
#mutable/immutable

#copying
list1 = [1,2,3]
list2 = list1
print("list1",list1)
print("list2",list2)
list1.append(4)
print("list2",list2)
print(id(list1))
print(id(list2))

#slicing
list2 = list1[:]
print("list2",list2)
list1.append(7)
print("list2",list2)
print(id(list1))
print(id(list2))

#mutable/immutable
string1 = 'asd'
print(string1[0])
#string[0] = 't' ezt nem lehet

list1[0] = 99
print(list1)


#join
separator = "-"
print(separator.join(["egy", "kettő", "három"]))

#reverse
list1.reverse()
print(list1)
#del, törli az objektumot, felszabadítja a memóriát is
del list1[0]
print(list1)
#del list1
#print(list1)
#del list1
#print(list2)

#len
print(len(list1))
print(len(string1)) #string1 = 'asd'

#and or not
x = (True and False) or (True and (not True))
print(x)

#warmup
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
print(list_1)
del list_2[:]
print(id("A"))
print(list_3)

#modul/package import

#pip show package, --version, pip3 list (-o), uninstall, install -U
#pypi

