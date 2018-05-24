# Write a function that computes the volume of a sphere given its radius.
print("# VOLUME OF A SPHERE\n")


def vol(rad):
    volume = (rad**3 * 3.141592) * (4/3)
    return "Volume of Sphere with radius {1} is = {0:1.5f} m3".format(volume, rad)


print(vol(2))
print(vol(8))
