# math operators
# + - * /
# // integer division
# % remainder
# ** exponent
# - Unary negative
# + unary positive

x = 5
y = 3
z = x + y
print(f"result is {z}")
print(f"result is {x + y}")
print(f"result is {x / y}")
print(f"result is {x // y}")
print(f"result is {x % y}")
z = -z
print(f"result is {z}")
z = +z
print(f"result is {z}")

# bitwise
# & and
# | or
# ^ Xor
# << shift left
# >> shift right

x = 0x0A
y = 0x02
z = x & y

print(f"(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}")
print(f"(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}")

z = x | y

print(f"(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}")
print(f"(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}")

z = x ^ y

print(f"(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}")
print(f"(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}")

z = x << y

print(f"(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}")
print(f"(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}")

# comparison
# <, >, <=, ==, >=

x = 42
y = 73

if x < y:
    print("true")
else:
    print("false")

if x > y:
    print("true")
else:
    print("false")

if x <= y:
    print("true")
else:
    print("false")


print("true") if x >= y else print("false")
print("true") if x == y else print("false")
print("true") if x != y else print("false")

# Bool
# and, or, not, in, not in, is, is not

a = True
b = False
x = ("bear", "bunny", "tree", "sky", "rain")
y = "bear"

print("true") if a and b else print("false")
print("true") if a or b else print("false")
print("true") if not b else print("false")
print("true") if y in x else print("false")
print("true") if "leaf" in x else print("false")
print("true") if "tree" in x else print("false")
if y is x[0]:
    print("true")
else:
    print("false")
print(id(y))
print(id(x[0]))
if y is not x[1]:
    print("true")
else:
    print("false")

# precedence
# exponents to bool or; chart in python docs
