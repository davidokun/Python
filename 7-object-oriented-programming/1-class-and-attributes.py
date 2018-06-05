# Creation of a Class
class Dog:

    # Constructor like
    def __init__(self, breed, name, age, spots):

        # Create/Assign an attribute
        self.breed = breed
        self.name = name
        self.age = age
        self.spots = spots


# Instantiation
my_dog = Dog(breed='Huskie', name='Sammy', age=4, spots=True)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.age)
print(my_dog.spots)
