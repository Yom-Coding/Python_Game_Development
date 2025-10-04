file = open("numbers.txt", "r")

n = file.read()

print(n)

n = n.split("\n")

print(n)


total = sum(n)

(print("The sum of all numbers is:", total))
