class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __repr__(self):
        return f"{self.year} {self.brand} {self.model}"


person = Person("John", 30)
car = Car("Toyota", "Camry", 2020)

print(person)  # Person('John', 30)
print(car)     # 2020 Toyota Camry
