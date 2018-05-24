# Write a function that computes the volume of a sphere given its radius.
print("# VOLUME OF A SPHERE\n")


def vol(rad):
    volume = (rad**3 * 3.141592) * (4/3)
    return "Volume of Sphere with radius {1} is = {0:1.5f} m3".format(volume, rad)


print(vol(2))
print(vol(8))

# Write a function that checks whether a number is in a given range (inclusive of high and low)
print("\n# NUMBER IS IN RANGE\n")


def ran_check(num, low, high):
    if num in range(low, high + 1):
        return '{0} is in the range between {1} and {2}'.format(num, low, high)
    else:
        return '{0} is NOT in the range between {1} and {2}'.format(num, low, high)


print(ran_check(5, 2, 7))
print(ran_check(3, 1, 10))
print(ran_check(10, 1, 10))
print(ran_check(1, 1, 10))
print(ran_check(50, 15, 30))
print(ran_check(0, 15, 31))
