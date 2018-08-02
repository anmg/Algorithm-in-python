class Singleton(object):
    __instance = None
    __first_init = None
    
    def __new__(cls, age, name):
        if not cls.__instance:
            Singleton.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True


a = Singleton(21, "tom")
b = Singleton(2, "tom")

print id(a)
print id(b) 


print a.age
print b.age


a.age = 33
print b.age

b.age = 50
print a.age
