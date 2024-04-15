class SimpleClass:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    """def __str__(self):
        return self.name + " " +  str(self.__age)"""
    def __age_times_two(self):
        return self.__age * 2


first_obj = SimpleClass('nincs', 50)
print(first_obj)
#print(first_obj.age_times_two())
print(SimpleClass.__dict__)
print(first_obj.__dict__)
print(" ")
print(SimpleClass.__name__) ##folytatás


