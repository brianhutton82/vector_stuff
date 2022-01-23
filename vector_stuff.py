import math
from os import system as sys

def get_vector():
    vector_string = input('enter each component of the vector separated by a space: ')
    vector = vector_string.split()
    for i in range(len(vector)):
        vector[i] = int(vector[i])
    return vector

def dot_product(u,v):
    result = 0
    for i in range(len(u)):
        result += (u[i] * v[i])
    return result

def magnitude(vector):
    return math.sqrt(dot_product(vector, vector))


def theta(u,v):
    return round(math.acos(dot_product(u,v) / (magnitude(u) * magnitude(v))) * (180 / math.pi))

print("vector u:")
u = get_vector()
print("vector v:")
v = get_vector()

print("u = {0}".format(u))
print("v = {0}".format(v))

print("||u|| = {0}".format(magnitude(u)))
print("||v|| = {0}".format(magnitude(v)))

print("the angle between u & v = {0} degrees".format(theta(u,v)))
