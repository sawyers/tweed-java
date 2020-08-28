# function / subroutines


def function(n):
    print(n)


function(47)


def function(n=1):
    print(n)


function()


def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def list_primes():
    for n in range(100):
        if isprime(n):
            print(n, end=" ", flush=True)
    print()


n = 5
if isprime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

list_primes()


class Duck:
    sound = "Quack"
    walking = "Walks"

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)


def main():
    donald = Duck()  # the object is donald
    donald.quack()
    donald.walk()


if __name__ == "__main__":
    main()


a = 8
b = 9
x = f"seven {a:<9} {b:>9}"
print(x)

a = 8
b = 9
x = f"seven {a:<09} {b:>09}"
print(x)

# -----------------

# minimalist lang
# ==, != ,etc
# and or not
# is / is not
# in / not in

hungry = True
x = "Feed the bear" if hungry else "Do not feed the bear"
print(x)

if False:
    print("if true")
elif True:
    print("elif true")
else:
    print("neither")

# function / subroutines


def function(n):
    print(n)


function(47)


def function(n=1):
    print(n)


function()


def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def list_primes():
    for n in range(100):
        if isprime(n):
            print(n, end=" ", flush=True)
    print()


n = 5
if isprime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

list_primes()


class Duck:
    sound = "Quack"
    walking = "Walks"

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)


def main():
    donald = Duck()  # the object is donald
    donald.quack()
    donald.walk()


if __name__ == "__main__":
    main()
