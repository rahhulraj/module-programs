#LEVEL 2: INTERMEDIATE (combining functions, real-life logic)
#I1. Savings Account [math.pow() + math.ceil()] [5 marks]
#Scenario: Rahul deposits Rs 10,000 in a bank that gives 5% compound interest per year. Amount after n years =
#P x (1 + r)^n.
#Task:
#1. Use math.pow() to find the amount after 3 years.
#2. Print it rounded to 2 decimal places.
#3. Use math.ceil() to print the amount rounded UP to the next whole rupee.

import math
P=10000
r=0.05
n=3
amount=P*math.pow(1+r,n)
print("AMOUNT :",round(amount,2))
print("ROUNDED UP AMOUNT :",math.ceil(amount))

#I2. Online Store Pagination [math.ceil() + math.floor()] [5 marks]
#Scenario: An online store has 95 products and shows 10 products per page.
#Task:
#1. Use math.ceil() to find the total number of pages.
#2. Use math.floor() to find how many pages are completely full.
#3. Calculate how many products are on the last page.

import math
products=95
per_page=10
pages=math.ceil(products/per_page)
full_pages=math.floor(products/per_page)
last_page= products%per_page
print("TOTAL PAGES :",pages)
print("FULL PAGES :",full_pages)
print("PRODUCTS ON LAST PAGE :", last_page)
print("---------------------------------------------------------------------------------------")
#I3. Delivery Distance [math.sqrt() + math.pow()] [5 marks]
#Scenario: A delivery rider starts at map point (1, 2) and must reach the customer at (4, 6). Distance =
#sqrt((x2-x1)^2 + (y2-y1)^2).
#Task:
#1. Write a program using math.pow() and math.sqrt() to calculate the straight-line distance.
#2. Print: Distance: ... units

import math
x1,y1=(1,2)
x2,y2=(4,6)
print("START POINT IS ",(x1,y1))
print("REACH CUSTOMER POINT IS ",(x2,y2))
sub1=x2-x1
sub2=y2-y1
result=math.pow(sub1,2)+math.pow(sub2,2)
distance=math.sqrt(result)
print("DISTANCE :", last_page,"UNITS")
print("---------------------------------------------------------------------------------------")


#I4. Splitting a Bill [math.modf()] [5 marks]
#Scenario: A restaurant bill is Rs 249.75. The billing software must show rupees and paise separately.
#Task:
#1. Use math.modf() to separate the whole and fractional parts.
#2. Convert the fractional part to paise (multiply by 100 and round).
#3. Print: Rupees: 249, Paise: 75

import math
bill=249.75
fraction,integer=math.modf(bill)
rupees=int(integer)
paise=round(fraction*100)
print("RUPEES :",rupees)
print("PAISE :",paise)
print("---------------------------------------------------------------------------------------")

#I5. Exam Hall Seating [math.factorial() + math.modf()] [5 marks]
#Scenario: 6 students must be seated in a row. A supervisor checks one seating arrangement every 0.5 seconds
#and wants to check all of them.
#Task:
#1. Use math.factorial() to find the number of arrangements.
#2. Find the total checking time in seconds.
#3. Convert it into minutes using division, and use math.modf() to split it into whole minutes and leftover seconds.

import math
students=6
arrangements=math.factorial(students)
seconds=arrangements*0.5
minutes=seconds/60
fraction,integr=math.modf(minutes)
leftoverseconds=fraction*60
print("ARRANGEMENTS :",arrangements)
print("TOTAL SECONDS:",seconds)
print("TIME :",int(integr),"MINUTES and",int(leftoverseconds),"SECONDS")
print("---------------------------------------------------------------------------------------")

#I6. Lottery Ticket [random.shuffle()] [5 marks]
#Scenario: A lottery draws 6 DIFFERENT numbers from 1 to 49.
#Task:
#1. Create a list of numbers 1 to 49 (hint: list(range(1, 50))).
#2. Use random.shuffle() and list slicing to pick the first 6 numbers.
#3. Print them in sorted order.
#4. Why is shuffle() safer here than calling randint() six times?

import random
numbers=list(range(1,50))
random.shuffle(numbers)
lottery=numbers[1:7]
lottery.sort()
print("LOTTERY NUMBERS :",lottery)
print("---------------------------------------------------------------------------------------")

#I7. Dice Statistics [random.randint() + statistics] [5 marks]
#Scenario: A game developer wants to check whether the dice in her game is fair by rolling it 20 times.
#Task:
#1. Use a loop and random.randint(1, 6) to store 20 rolls in a list.
#2. Print the list.
#3. Print the mean, median and mode of the rolls.
#4. For a fair die, roughly what mean do you expect?

import random
import statistics
rolls=[]
for i in range(20):
    num=random.randint(1,6)
    rolls.append(num)
print("DICE ROLLS :",rolls)
print("MEAN :",statistics.mean(rolls))
print("MEDIAN :",statistics.median(rolls))
print("MODE :",statistics.mode(rolls))
print("---------------------------------------------------------------------------------------")

#I8. Salary Report [mean / median / median_low / median_high] [5 marks]
#Scenario: A small company has 6 employees with monthly salaries (Rs): [12000, 15000, 18000, 22000, 40000,
#90000].
#Task:
#1. Calculate the mean, median, median_low and median_high.
#2. Which measure best represents a 'typical' salary? Explain in one sentence

import statistics
salary=[12000,15000,18000,22000,40000,90000]
print("MEAN :",statistics.mean(salary))
print("MEDIAN :",statistics.median(salary))
print("LOW MEDIAN :",statistics.median_low(salary))
print("HIGH MEDIAN :",statistics.median_high(salary))