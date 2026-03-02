# math.py

import math
import random

# Built-in functions
print("Min:", min(5, 2, 8))
print("Max:", max(5, 2, 8))
print("Abs:", abs(-10))
print("Round:", round(3.14159, 2))
print("Power:", pow(2, 3))

# math module
print("Square root:", math.sqrt(16))
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.8))
print("Sin:", math.sin(math.pi / 2))
print("Pi:", math.pi)
print("E:", math.e)

# random module
print("Random float:", random.random())
print("Random integer:", random.randint(1, 10))

items = ["Ali", "Islam", "Omar"]
print("Random choice:", random.choice(items))

random.shuffle(items)
print("Shuffled list:", items)