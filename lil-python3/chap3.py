a = 8
b = 9
x = f"seven {a:<9} {b:>9}"
print(x)

a = 8
b = 9
x = f"seven {a:<09} {b:>09}"
print(x)

# -----------------

x = 7
print(f"x is {x}")
print(type(x))

x = 7 / 3
print(f"x is {x}")
print(type(x))

x = 7 // 3
print(f"x is {x}")
print(type(x))

x = 7 % 3
print(f"x is {x}")
print(type(x))

# precision vs accuracy
x = 0.1 + 0.1 + 0.1 - 0.3
print(f"x is {x}")
print(type(x))

from decimal import *

a = Decimal(".10")
b = Decimal(".30")
x = a + a + a - b
print(f"x is {x}")
print(type(x))

# --- Bools

x = True
print(f"x is {x}")
print(type(x))

x = 0
print(f"x is {x}")
print(type(x))

print("True") if x else print("False")

# list is mutable []
# tuple is not ()

x = range(5)
for i in x:
    print(i)

x = range(5, 10)
for i in x:
    print(i)

x = range(5, 50, 5)
for i in x:
    print(i)

# dict is a key value { key: value}

x = {"one": 1, "two": 2}
for k, v in x.items():
    print("k: {}, v:{}".format(k, v))

x = (1, "two", 3.0, [4, "four"], 5)
print(f"x is {x}")
print(type(x))
print(type(x[1]))
print("true") if isinstance(x, tuple) else print("false")
