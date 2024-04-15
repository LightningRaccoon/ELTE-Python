import random

list = []
tuple = ()
dict = {}

list.append(1)
list.append("kutya")
list.append(1.45)

tuple = (1, "kutya", 1.45)

dict["kutya"] = 1
dict["kutya2"] = 2


print(list)
print(tuple)
print(dict)
print(dict["kutya"])

print(f"list[0]: {list[0]}")

randI = 0

while (randI != 50):
    randI = random.randint(0, 100)
    print(f"randI: {randI}")


print()

n = 5  # Change n to the size of your matrix
matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

def find_similar_numbers(matrix, row, col, radius):
    similar_numbers = set()
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            new_row, new_col = row + i, col + j
            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
                similar_numbers.add(matrix[new_row][new_col])
    return similar_numbers

random_row = random.randint(0, n - 1)
random_col = random.randint(0, n - 1)
selected_element = matrix[random_row][random_col]

radius = 1
similar_numbers = find_similar_numbers(matrix, random_row, random_col, radius)

for i in range(len(matrix)):
    print(matrix[i])
print(f"Selected Element: {selected_element}")
print(f"Similar Numbers within a Radius of {radius}: {similar_numbers}")


foo = [i + i for i in range(5)]

print (foo)

from datetime import time

t = time(14, 39)

print(t.strftime("%H:%M:%S"))

#Írj egy lambda függvényt, ami egy listát kapva paraméterül visszaadja a legnagyobb elemét a listának!

any_list = [1, 2, 3, 4]
max_item_of_list = lambda list: max(list)

print(max_item_of_list)


class Vowels:
    def __init__(self):
        self.vow = "aeiouy "  # Yes, we know that y is not always considered a vowel.
        self.pos = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]

vowels = Vowels()

for v in vowels:
    print(v, end=' ')