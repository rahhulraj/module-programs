#1. Create a program to calculate the average, median, and mode of students' marks.

import statistics
n=int(input("ENTER THE NUM OF SUBJECT :"))
marks=list()
for i in range(n):
    mark=int(input("ENTER THE MARK :"))
    marks.append(mark)
avg=statistics.mean(marks)
med=statistics.median(marks)
mod=statistics.mode(marks)
print("Average:",avg)
print("Median:",med)
print("Mode:",mod)

#2. Given the monthly sales of a shop, display the average sale and identify the highest and lowest values.

import statistics
n=int(input("ENTER THE NUM OF SALES :"))
sales=list()
for i in range(n):
    sale=int(input("ENTER THE SALE :"))
    sales.append(sale)
avg=statistics.mean(sales)
high=max(sales)
low=min(sales)
print("Average Sale:",avg)
print("Highest Sale:",high)
print("Lowest Sale:",low)


#3. Write a program to calculate the standard deviation of employee salaries.

import statistics

n=int(input("ENTER THE NUM OF SALARIES :"))
salaries=list()
for i in range(n):
    salary=int(input("ENTER THE SALE :"))
    salaries.append(salary)
#salaries=[25000, 30000, 35000, 40000, 45000]
sd=statistics.stdev(salaries)
print("Standard Deviation:",sd)


#4. Compare the average marks of two classes and display which class performed better.

import statistics

#class1=[80,75,90,85,70]
#class2=[85,90,95,80,88]

n=int(input("ENTER THE NUM OF SUBJECTS IN CLASS1 :"))
m=int(input("ENTER THE NUM OF SUBJECTS IN CLASS2 :"))
class1=list()
for i in range(n):
    mark1=int(input("ENTER THE MARK OF CLASS 1 :"))
    class1.append(mark1)
class2=list()
for j in range(m):
    mark2=int(input("ENTER THE MARK OF CLASS 2 :"))
    class2.append(mark2)
avg1=statistics.mean(class1)
avg2=statistics.mean(class2)
print("Class 1 Average:",avg1)
print("Class 2 Average:",avg2)
if avg1>avg2:
    print("Class 1 performed better")
elif avg2>avg1:
    print("Class 2 performed better")
else:
    print("Both classes performed equally")


#5. Create a program that analyzes the heights of students and displays the mean, median, and most common height.

import statistics
#studentlist=[150,160,155,160,165,170,160]

n=int(input("ENTER THE NUM OF STUDENTS :"))
studentlist=list()
for i in range(n):
    studentheight=int(input("ENTER THE HEIGHT OF STUDENTS :"))
    studentlist.append(studentheight)
mean=statistics.mean(studentlist)
median=statistics.median(studentlist)
mode=statistics.mode(studentlist)
print("Mean Height:",mean)
print("Median Height:",median)
print("Most Common Height:",mode)