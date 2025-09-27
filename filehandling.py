#open file
f=open("file.txt","w")

#Write in it
f.write("Hello my name is Yom \n")

f.write("I am 14 Years Old \n")

#Close File
f.close()

#Open File Again
f=open("file.txt","r")

q=f.read()

print(q)

f.close()

#open file
f=open("file.txt","a")

#Write in it
f.write("Hello my name is Yom \n")

f.write("I am 14 Years Old")

#Close File
f.close()