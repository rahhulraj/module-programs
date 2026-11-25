#LEVEL 3: ADVANCED (multi-step programs, debugging, simulations)
#A1. Bug Hunt [Error handling (all modules)] [8 marks]
#cenario: A junior developer wrote the five statements below. Each one fails or behaves unexpectedly. Treat them
#as independent snippets.
#Task:
#1. Name the exception raised (or the wrong behaviour) for each snippet.
#2. Explain why it happens and write the corrected code.
"""
import math, random, statistics
scores = [88, 92, 75, 64]
# (a)
result = random.shuffle(scores)
print(result[0])
# (b)
print(math.factorial(5.5))
# (c)
print(math.sqrt(-4))
# (d)
print(statistics.mean([]))
# (e)
print(random.choice([]))
"""
"""
import math,random,statistics
scores=[88,92,75,64]
# (a) 
random.shuffle(scores)
print(scores[0])
# (b)
print(math.factorial(5))
# (c)
print(math.sqrt(4))
# (d)
print(statistics.mean(scores))
# (e)
print(random.choice(scores))

#A2. Class Performance Report [statistics (all functions)] [8 marks]
#Scenario: A teacher has the marks of 10 students: [88, 92, 75, 64, 92, 81, 70, 92, 58, 85]. She wants a complete
#performance report.
#Task:
#1. Print the mean, median, mode, median_low and median_high.
#2. Print the standard deviation rounded to 2 decimals.
#3. A new student scored 95. Calculate the z-score: (95 - mean) / stdev, rounded to 2 decimals.
#4. Count how many students scored within one standard deviation of the mean (between mean - stdev and mean
#+ stdev).

import statistics
marks=[88,92,75,64,92,81,70,92,58,85]
mean=statistics.mean(marks)
median=statistics.median(marks)
mode=statistics.mode(marks)
low=statistics.median_low(marks)
high=statistics.median_high(marks)
sd=statistics.stdev(marks)
z=(95-mean)/sd
print("MEAN :",mean)
print("MEDIAN :",median)
print("MODE :",mode)
print("LOW MEDIAN :",low)
print("HIGH MEDIAN :",high)
print("STANDARD DEVIATION :",round(sd,2))
print("Z-SCORE :",round(z,2))
count=0
for mark in marks:
    if mean-sd<=mark<=mean+sd:
        count=count+1
print("Students within one standard deviation:",count)

#A3. Safe Calculator [math + statistics + exceptions] [8 marks]
#Scenario: You are building a calculator app. It must never crash, even if the user types bad input.
#Task:
#1. Write safe_factorial(n), safe_sqrt(x) and safe_mean(data) using try / except.
#2. Each function returns the real answer, or a friendly message on error.
#3. Test with: safe_factorial(5), safe_factorial(-3), safe_factorial(5.5), safe_sqrt(-4), safe_sqrt(81), safe_mean([]),
#safe_mean([4, 6]).





#A4. Estimating Pi (Monte Carlo) [random.random() + math] [8 marks]
#Scenario: Imagine throwing darts at a 1 x 1 square that contains a quarter circle of radius 1. The fraction of darts
#landing inside the quarter circle is about pi / 4.
#Task:
#1. Generate 100,000 random points (x, y) using random.random().
#2. A point is inside if math.sqrt(math.pow(x, 2) + math.pow(y, 2)) <= 1.
#3. Estimate pi = 4 x (points inside / total points).
#4. Compare with math.pi and print the percentage error.
#5. What happens to accuracy if you use 100 points instead?

import random
import math
total=100000
inside=0
for i in range(total):
    x=random.random()
    y=random.random()
    distance=math.sqrt(math.pow(x,2)+math.pow(y,2))
    if distance<=1:
        inside=inside+1
pi_value=4*inside/total
error=abs(pi_value-math.pi)/math.pi*100
print("ESTIMATED PI :",pi_value)
print("ACTUAL PI :",math.pi)
print("PERCENTAGE ERROR :",round(error,2),"%")

"""
#A5. Tiling a Room [ceil + sqrt + pow] [8 marks]
#Scenario: A room is 7.5 m long and 4.2 m wide. It will be covered with square tiles of side 0.5 m. Each tile costs
#Rs 35. The contractor adds 10% extra tiles for breakage (rounded up).
#Task:
#1. Use math.ceil() to find the tiles needed along the length and along the width, then the total.
#2. Add 10% extra and round UP again to get the number to buy.
#3. Calculate the total cost.
#4. Use math.sqrt() and math.pow() to find the room's diagonal length, rounded to 2 decimals.

import math
length=7.5
width=4.2
tile=0.5
price=35
length_tiles=math.ceil(length/tile)
width_tiles=math.ceil(width/tile)
total_tiles=length_tiles*width_tiles
extra_tiles=math.ceil(total_tiles*0.10)
buy_tiles=total_tiles+extra_tiles
cost=buy_tiles*price
diagonal=math.sqrt(math.pow(length,2)+math.pow(width,2))
print("TILES ALONG LENGTH :",length_tiles)
print("TILES ALONG WIDTH :",width_tiles)
print("TOTAL TILES :",total_tiles)
print("EXTRA TILES :",extra_tiles)
print("TILES TO BUY:",buy_tiles)
print("TOTAL COST: RS",cost)
print("ROOM DIAGONAL:",round(diagonal, 2),"m")


#A6. Raffle and Dice Simulator [random + statistics (combined)] [8 marks]
#Scenario: A fair organiser runs two activities. (1) A dice game where each player rolls two dice and adds them. (2)
#A raffle among 10 participants: Anu, Ben, Chitra, Dev, Esha, Farah, Gopal, Hari, Isha, Jose.
#Task:
#1. Simulate 1000 rolls of two dice (sum of two randint(1, 6) values) and print the mean, median, mode and
#stdev (2 decimals).
#2. Shuffle the participants and take the first 3 as raffle winners.
#3. Use random.choice() to pick one bonus winner from the remaining 7.
#4. Predict approximately what mean and mode you expect for the dice sums.

import random
import statistics
# Dice simulation
rolls=[]
for i in range(1000):
    dice1=random.randint(1, 6)
    dice2=random.randint(1, 6)
    total=dice1+dice2
    rolls.append(total)
print("MEAN :",round(statistics.mean(rolls), 2))
print("MEDIAN :",statistics.median(rolls))
print("MODE :",statistics.mode(rolls))
print("STANDARD DEVIATION :",round(statistics.stdev(rolls), 2))
# Raffle
names = ["Anu", "Ben", "Chitra", "Dev", "Esha","Farah", "Gopal", "Hari", "Isha", "Jose"]
random.shuffle(names)
winners=names[:3]
print("RAFFLE WINNERS :",winners)
remaining = names[3:]
bonus = random.choice(remaining)
print("BONUS WINNER :",bonus)
