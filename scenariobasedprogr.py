"""

#Python Practical Questions – Date, Time and Time Module
#Level: Beginner
#Type: Scenario-based programming questions
#Topics: datetime, date, time, timedelta, strftime(), strptime(), time module, sleep(), time(), ctime()
#These questions are designed to help students apply date and time concepts in real-life situations.
#Part 1: Date module Basic practical questions

#1. Employee Joining Date
#An employee joins a company today. Write a Python program to display the current date in the format 02-11-2026.
import datetime
datenow1=datetime.datetime.now()
print("THE EMPLOYEE JOINED DATE IS :",datenow1.strftime("%d-%m-%Y"))


#2. Student Registration
#A college wants to display the registration date of a student in three different formats:
#02/11/2026
#02 November 2026
#Monday, 02 November 2026

import datetime
datenow2=datetime.date.today()
print("THE REGISTRATION DATE IS :",datenow2.strftime("%d/%m/%Y"))
print("THE REGISTRATION DATE IS :",datenow2.strftime("%d %B %Y"))
print("THE REGISTRATION DATE IS :",datenow2.strftime("%A, %d %B %Y"))


#3. Birthday Reminder
#A user enters their date of birth in the format DD-MM-YYYY. Write a program to convert it into a date object and display 
# it as November 02, 2003.

import datetime
dob=input("Enter your date of birth (DD-MM-YYYY): ")
date=datetime.datetime.strptime(dob,"%d-%m-%Y")
print(date.strftime("%B %d,%Y"))


#4. Age Calculator
#A user enters their date of birth. Calculate and display their current age in years.

import datetime
dob=input("Enter your date of birth (DD-MM-YYYY): ")
dob=datetime.datetime.strptime(dob,"%d-%m-%Y").date()
today=datetime.date.today()
age=today.year-dob.year
if (today.month,today.day)<(dob.month,dob.day):
    age=age-1
print("Your age is:",age)

#5. Days Until Birthday
#A user enters their birthday. Write a program to calculate how many days are remaining until their next birthday.

import datetime
dob=input("Enter your date of birth (DD-MM-YYYY): ")
dob=datetime.datetime.strptime(dob,"%d-%m-%Y").date()
today=datetime.date.today()
birthday=datetime.date(today.year,dob.month,dob.day)
if birthday<today:
    birthday=datetime.date(today.year+1,dob.month,dob.day)
days=(birthday-today).days
print("Days remaining until birthday:",days)



#6. Library Membership
#A student registers for a library membership today. The membership is valid for 90 days. Display the membership expiry date.

import datetime
today=datetime.date.today()
expiry_date=today+datetime.timedelta(days=90)
print("Membership Starting Date:",today)
print("Membership Expiry Date:",expiry_date)


#7. Exam Countdown
#An examination is scheduled for 25 December 2026. Write a program to calculate how many days are remaining until the 
# examination.

from datetime import date
today = date.today()
exam_date = date(2026,12,25)
remaining_days = (exam_date - today).days
print("Days remaining until examination:",remaining_days)


#8. Attendance Record
#A college wants to display the current day, month, year and weekday separately.

import datetime
x=datetime.datetime.now()
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%Y"))
print(x.strftime("%w"))


#Part 2: Time module – Practical questions
#9. Digital Clock
#Write a Python program that continuously displays the current time in HH:MM:SS format. Refresh the display every second.

import time
from datetime import datetime
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)

"""



#10. OTP Verification
#A website generates an OTP. The user has 30 seconds to enter it. Write a program that waits for 30 seconds and then displays 
# OTP Expired.

import time
print("OTP Generated. You have 30 seconds to enter it.")
time.sleep(30)
print("OTP Expired")




#11. Online Examination Timer
#A student gets 10 minutes to complete an examination. Write a program that displays the remaining time every second until the 
# timer reaches zero.






#12. Traffic Signal System
#Green – 15 seconds
#Yellow – 5 seconds
#Write a Python program to simulate this traffic signal using the time module.







#13. Food Delivery Waiting Time
#A food delivery application needs to display a message every 5 seconds while the customer waits. Display Your order is being prepared... 
# three times.






#14. Website Loading Simulation
#When a user opens a website, display the following messages with a 2-second delay between each message:
#Connecting to server...
#Loading website...
#Fetching data...
#Website loaded successfully!








#15. Stopwatch
#Write a Python program that records the starting time when the user starts a task and calculates the total time taken when the user 
# finishes it.


