class Dog:

    species = 'Mammal'  # Class object attribute. Same for any instance of a class

    def __init__(self, name, age, breed):
        self.breed = breed
        self.name = name
        self.age = age

    # Methods
    def bark(self, number):
        print('Woof!! My name is {} and the number is {}'.format(self.name, number))


my_dog = Dog('Dante', 3, 'Huskie')

print(my_dog.name)
print(my_dog.age)
print(my_dog.breed)
print(my_dog.species)

my_dog.bark(5)


class Circle:

    pi = 3.141516  # Like static attribute

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi  # Calling with class name

    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)

print('Circumference is {}'.format(my_circle.get_circumference()))
print('Area is {}'.format(my_circle.area))
