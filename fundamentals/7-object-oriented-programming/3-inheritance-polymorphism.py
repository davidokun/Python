print('## Inheritance \n')


class Animal:

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


my_animal = Animal()

my_animal.who_am_i()
my_animal.eat()


class Dog(Animal):  # Inheriting from Animal class

    def __init__(self):
        Animal.__init__(self)  # Call Animal 'constructor?'
        print('Dog created')

    def who_am_i(self):  # Overriding method from parent class
        print('I am a Dog')

    def bark(self):  # New method on Dog
        print('Woof!!')


my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()

print('\n## Polymorphism \n')


class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says woof!')


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says meow!')


niko = Dog('Niko')
felix = Cat('Felix')
niko.speak()
felix.speak()

print('###')

for pet in [niko, felix]:
    print(type(pet))
    pet.speak()

print('###')


def pet_speak(new_pet):
    new_pet.speak()


pet_speak(niko)
pet_speak(felix)


print('# Abstract Class')


class Animal:  # Abstract Class

    def __init__(self, name):
        self.name = name

    def speak(self):  # Abstract method
        raise NotImplementedError('Subclass must implement this abstract method')


class Cow(Animal):  # Inherit from Animal

    def speak(self):  # Implement speak() method from Animal
        print(self.name + ' says hello')


my_cow = Cow('Beatrix')
my_cow.speak()
