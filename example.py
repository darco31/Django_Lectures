# class OOP example

# class Student():

#     species = 'Human'  # Class object attribute

#     def __init__(self, name, gpa):

#         self.name = name  # Attributes
#         self.gpa = gpa


# student1 = Student(name="Steve", gpa=4.0)
# student2 = Student(name="Paul", gpa=3.0)

# print(student1.gpa)


# New class example

# class Agent():

#     origin = 'USA'

#     def __init__(self, name, height, weight):
#         self.name = name
#         self.height = height
#         self.weight = weight


# x = Agent('steve', 6, 170)
# print(x.name)
# x.weight = 160  # Updated weight for agent
# print(x.weight)


# class Dog():

#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age

#     def calculate_human_age(self):
#         return self.age * 7


# Hans = Dog("Hans", "German Shepard", 7)

# print(Hans.calculate_human_age())


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def greet(self):
        print(f"Hi! My name is {self.name} and I am a {self.species}")


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")

    def sound(self):
        print("Wuff")


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Cat")

    def sound(self):
        print("Meow")


print(Cat.sound(self))
