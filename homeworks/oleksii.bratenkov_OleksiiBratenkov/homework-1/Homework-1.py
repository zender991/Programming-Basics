
print ("Hello! Can I ask you a few questions?")
name = input("What is your name? ")
city = input ("Where are you live? ")
age = int(input("What is your age? "))
answer = ("Hello, %s from %s, why you only %i ?" %(name, city, age))
print(answer)
file = open ("answers.txt", "w")
file.write(answer)
file.close()
