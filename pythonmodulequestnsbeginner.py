#B1. Tile Shop [math.pow()] [2 marks]
#Scenario: A shop sells square floor tiles. One tile has a side of 12 cm.
#Task:
#1. Use math.pow() to calculate the area of one tile.
#2. Print the result as: Area of tile: ...
#3. Is the value returned an int or a float?

import math
area=math.pow(12,2)
print("AREA OF TILE :",area)
print(type(area))
print("---------------------------------------------------------------------")

#B2. Flour Bags [math.floor()] [2 marks]
#Scenario: A baker has 47.8 kg of flour and sells it only in full 1 kg bags.
#Task:
#1. Use math.floor() to find how many full bags can be packed.
#2. Print: Full bags: ...

import math
bags=math.floor(47.8)
print("FULL BAGS :", bags)
print("---------------------------------------------------------------------")

#B3. School Trip [math.ceil()] [2 marks]
#Scenario: 130 students are going on a trip. Each bus can carry 40 students.
#Task:
#1. Use math.ceil() to find the number of buses required.
#2. Why can't we just use normal division (130 / 40)?

import math
buses=math.ceil(130/40)
print("BUS REQUIRED :",buses)
print("---------------------------------------------------------------------")

#B4. Photo Queue [math.factorial()] [2 marks]
#Scenario: 5 friends stand in a line for a group photo. The number of different orders is 5! (5 factorial).
#Task:
#1. Use math.factorial() to find the number of possible arrangements.
#2. Print: Arrangements: ...

import math
result=math.factorial(5)
print("ARRANGEMENTS :",result)
print("---------------------------------------------------------------------")

#B5. Work Hours [math.modf()] [2 marks]
#Scenario: An employee worked 7.75 hours today.
#Task:
#1. Use math.modf() to split the value into its fractional and whole parts.
#2. Convert the fractional part to minutes and print: 7 hours and 45 minutes
#3. Which part does modf() return first?

import math
fraction,whole=math.modf(7.75)
minutes=int(fraction*60)
print(whole,"HOURS and",minutes,"MINUTES")
print("---------------------------------------------------------------------")

#B6. Square Garden [math.sqrt()] [2 marks]
#Scenario: A square garden has an area of 144 square metres. The owner wants to buy fencing for one side.
#Task:
#1. Use math.sqrt() to find the length of one side.
#2. Print: Side length: ...

import math
side=math.sqrt(144)
print("SIDE LENGTH :",side)
print("---------------------------------------------------------------------")

#B7. Circular Pond [math.pi] [2 marks]
#cenario: A circular pond has a radius of 5 metres.
#Task:
#1. Use the math.pi constant to calculate the area (pi x r x r).
#2. Print the area.

import math
r=5
area=math.pi*r*r
print("AREA :",area)
print("---------------------------------------------------------------------")

#B8. Lucky Draw [random.choice()] [2 marks]
#Scenario: A shop runs a lucky draw. Participants: Anu, Ben, Chitra, Dev, Esha.
#ask:
#1. Store the names in a list.
#2. Use random.choice() to pick one winner and print: Winner: ...

import random
names=["Anu","Ben","Chitra","Dev","Esha"]
winner=random.choice(names)
print("WINNER :",winner)
print("---------------------------------------------------------------------")

#B9. Board Game Dice [random.randint()] [2 marks]
#Scenario: You are building a board game and need to simulate rolling a six-sided die.
#Task:
#1. Use random.randint() to simulate one roll.
#2. Print: You rolled: ...
#3. What are the smallest and largest values possible?

import random
roll=random.randint(1,6)
print("YOU ROLLED:",roll)
print("---------------------------------------------------------------------")

#B10. Discount Coupon [random.random()] [2 marks]
#Scenario: A mobile app shows a random 'luck score' to every user after login.
#Task:
#1. Import the function using from random import random.
#2. Print one random float.
#3. Between which two values does it lie? Can it equal 1.0?

from random import random
num=random()
print("RANDOM VALUE IS :",num)
print("---------------------------------------------------------------------")

#B11. Music Playlist [random.shuffle()] [2 marks]
#Scenario: A music app has the playlist: ["Song A", "Song B", "Song C", "Song D", "Song E"]. The user taps the
#Shuffle button.
#Task:
#1. Print the playlist before shuffling.
#2. Use random.shuffle() to shuffle it, then print it again.
#3. Does shuffle() create a new list or change the original?

import random
songs=["Song A","Song B","Song C","Song D","Song E"]
print("BEFORE SHUFFLE :",songs)
random.shuffle(songs)
print("AFTER SHUFFLE :",songs)
print("---------------------------------------------------------------------")

#B12. Class Test Results (Part 1) [statistics.mean()] [2 marks]
#Scenario: Marks of 7 students in a test: [72, 85, 90, 65, 85, 78, 92]. This data is used in Questions B12 to B15.
#Task:
#1. Use statistics.mean() to find the average mark.
#2. Print: Average: ...

import statistics
marks=[72,85,90,65,85,78,92]
avg=statistics.mean(marks)
print("AVERAGE :",avg)
print("---------------------------------------------------------------------")

#B13. Class Test Results (Part 2) [statistics.median()] [2 marks]
#Scenario: Use the same marks: [72, 85, 90, 65, 85, 78, 92].
#Task:
#1. Use statistics.median() to find the middle mark.
#2. First sort the list by hand and say which value is in the middle.

import statistics
marks=[72,85,90,65,85,78,92]
middle=statistics.median(marks)
print("MIDDDLE MARK IS :",middle)
print("---------------------------------------------------------------------")

#B14. Class Test Results (Part 3) [statistics.mode()] [2 marks]
#Scenario: Use the same marks: [72, 85, 90, 65, 85, 78, 92].
#Task:
#1. Use statistics.mode() to find the most frequent mark.
#2. How many students scored that mark?

import statistics
marks=[72,85,90,65,85,78,92]
modeis=statistics.mode(marks)
print("MODE :",modeis)
print("---------------------------------------------------------------------")

#B15. Class Test Results (Part 4) [statistics.stdev()] [2 marks]
#Scenario: Use the same marks: [72, 85, 90, 65, 85, 78, 92]. The teacher wants to know how spread out the marks are
#Task:
#1. Use statistics.stdev() to find the standard deviation.
#2. Print it rounded to 2 decimal places.

import statistics
marks=[72,85,90,65,85,78,92]
result=statistics.stdev(marks)
print("STANDARD DEVIATION :",round(result,2))
print("---------------------------------------------------------------------")

#B16. Shoe Sizes [median_low() / median_high()] [2 marks]
#cenario: A shop sold shoes of these sizes today: [6, 8, 7, 9, 5, 10].
#Task:
#1. Find the normal median using statistics.median().
#2. Find the low and high medians using median_low() and median_high().
#3. Which of the three values is NOT an actual shoe size in the list?

import statistics
sizes=[6,8,7,9,5,10]
print("MEDIAN :",statistics.median(sizes))
print("LOW MEDIAN:",statistics.median_low(sizes))
print("HIGH MEDIAN:",statistics.median_high(sizes))
print("---------------------------------------------------------------------")