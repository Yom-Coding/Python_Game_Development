file = open("numbers.txt", "r")

n = file.read()

print(n)

n = n.split("\n")

print(n)

total = 0
for x in n:
    total = total + int(x) 

(print("The sum of all numbers is:", total))
