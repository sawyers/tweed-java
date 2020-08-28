#! /usr/bin/env python3
# loops
# while or for loop

secret = "swordfish"
pw = ""

while pw != secret:
    pw = input("Whats the password? ")  # nosec

animals = ("bear", "bunny", "dog", "cat")

for pet in animals:
    print(pet)

for pet in range(5):
    print(pet)

# additional controls, continue, break, else
# continue goes to next item
# break exists loop early
# else run if loop runs normally
# use in while or for loops

secret = "swordfish"
pw = ""
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt:
        break
    if count == 3:
        continue
    pw = input(f"{count}:  Whats the password? ")  # nosec
else:
    auth = True

print("authorized" if auth else "lock system")

animals = ("bear", "bunny", "dog", "cat")

for pet in animals:
    if pet == "dog":
        continue
    if pet == "cat":
        break
    print(pet)
else:
    print("you have seen them all")
