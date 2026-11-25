
#1. Develop a lottery system that generates six unique random numbers.

import random
numbers=list()
while len(numbers)<6:
    n=random.randint(1,49)
    if n not in numbers:
        numbers.append(n)
print("LOTTERY NUMBERS ARE :",numbers)

#2. Create a dice game where two dice are rolled and the total is displayed.

import random
dice1=random.randint(1,6)
dice2=random.randint(1,6)
total=dice1+dice2
print("FIRST DICE :",dice1)
print("SECOND DICE :",dice2)
print("TOTAL :",total)

#3. Write a program to randomly select a student from a class list.

import random
#students=["Rahul Raj","Neymar","Messi","Yamal","Cristiano Ronaldo","Mbappe","Sunil chhehtri"]
n=int(input("ENTER THE NUM OF SUBJECT :"))
students=list()
for i in range(n):
    studentname=input("ENTER THE STUDENT NAME :")
    students.append(studentname)
student=random.choice(students)
print("Selected Student:",student)


#4. Generate a secure 8-character password using letters, numbers, and special characters.

import random
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$"
password=""
for i in range(8):
    password=password+random.choice(characters)
print("Password:",password)

#5. Create a rock-paper-scissors game where the computer makes a random choice.

import random
choices=["ROCK","PAPER","SCISSORS"]
computer=random.choice(choices)
user=input("Enter ROCK , PAPER or SCISSORS : ")
print("Computer:",computer)
if user==computer:
    print("TIE...NEXT")
elif user=="ROCK" and computer=="SCISSORS":
    print("YOU WIN..!")
elif user=="PAPER" and computer=="ROCK":
    print("YOU WIN..!")
elif user=="SCISSORS" and computer=="PAPER":
    print("YOU WIN..!")
elif user in choices:
    print("COMPUTER WINS....-_-")
else:
    print("INVALID CHOICE")