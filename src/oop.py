class Person:
    def __init__(self, name, age, country):
        self.__name: str = name
        self.__age: int = age
        self.__country: str = country

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def country(self):
        return self.__country

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @country.setter
    def country(self, country):
        self.__country = country

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Country: {self.country}"


p1 = Person("John", 36, "Norway")
p1.name = "Jane"
print(p1)
