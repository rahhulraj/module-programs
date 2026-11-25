#1. Extract Numbers
#A shopping application stores product details.
#text = "Pen 10, Book 50, Bag 250, Pencil 15"
#Task: Extract all numbers from the given text.

import re
text="Pen 10, Book 50, Bag 250, Pencil 15"
result=re.findall(r'\d+',text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#2. Extract All Words
#A sentence is stored in a text-processing application.
#text = "Python is a popular programming language"
#Task: Extract all words and display them as a list.

import re
text="Python is a popular programming language"
result=re.split('\s',text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#3. Find Whitespace Characters
#text = "Learning Python is very interesting"
#Task: Extract all whitespace characters using re.findall().

import re
text="Learning Python is very interesting"
result=re.findall('\s', text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#4. Extract Uppercase Letters
#text = "WELCOME to PYTHON Programming"
#Task: Extract all uppercase letters.

import re
text="WELCOME to PYTHON Programming"
result=re.findall('[A-Z]',text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#5. Extract Lowercase Letters
#text = "HELLO Welcome TO Programming"
#Task: Extract all lowercase letters.

import re
text="HELLO Welcome TO Programming"
result=re.findall('[a-z]',text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#6. Find Special Characters
#A username contains different special characters.
#username = "student@123#python!"
#Task: Extract all special characters.

import re
username="student@123#python!"
result=re.findall('[~!@#$%^&_.]',username)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

"""
import re
username="student@123#python!"
result=re.findall('[^a-zA-Z0-9]',username)
print(result)
print(".........-------------------.............................-------------------................")
"""

#7. Extract Only Alphabets
#text = "Python123 Java456 Django789"
#Task: Extract only alphabetic groups.

import re
text="Python123 Java456 Django789"
result=re.findall('[a-zA-Z]+',text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#8. Extract Individual Digits
#text = "Room number 205 has 3 chairs and 12 tables"
#Task: Extract every individual digit.

import re
text="Room number 205 has 3 chairs and 12 tables"
result=re.findall(r'\d',text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#Level 2 – Intermediate
#9. Extract Complete Numbers
#text = "There are 25 students, 5 teachers and 3 classrooms"
#Task: Extract complete numbers instead of individual digits.

import re
text="There are 25 students, 5 teachers and 3 classrooms"
result=re.findall(r'\d+',text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#10. Extract Words Starting with Uppercase
#text = "Ravi studies Python with Anu and David"
#Task: Extract only words that start with uppercase letters.

import re
text="Ravi studies Python with Anu and David"
result=re.findall('[A-Z][a-z]*', text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#11. Separate Alphabets and Numbers
#text = "ABC123 XYZ456 PQR789"
#Task:
#- Extract alphabetic groups.
#- Extract numeric groups.
#- Display both separately.

import re
text="ABC123 XYZ456 PQR789"
alphabets=re.findall(r'[A-Z]+', text)
numbers=re.findall(r'\d+', text)
print("Alphabets:",alphabets)
print("Numbers:",numbers)
print("-------------------------------------------------------------------------------------------------------------")


#12. Extract Words with at Least Three Characters
#text = "I am learning Python and Java"
#Task: Extract words containing at least three characters.

import re
text="I am learning Python and Java"
result=re.findall('[a-zA-Z][a-zA-Z][a-zA-Z]+',text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#13. Extract Consecutive Special Characters
#text = "Hello@@World!!! Python###Programming"
#Task: Extract consecutive groups of special characters.

import re
text="Hello@@World!!! Python###Programming"
result=re.findall('[~!@#$%^&_.]+', text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#14. Extract Numbers Starting with 9
#text = "9876 8765 9123 7654 9988"
#Task: Extract only numbers beginning with 9.

import re
text="9876 8765 9123 7654 9988"
result=re.findall(r'9\d+', text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")


#15. Extract Words Ending with 'n'
#text = "Python Java C C# Django Kotlin Ruby"
#Task: Extract words ending with the letter n.

import re
text="Python Java C C# Django Kotlin Ruby"
result=re.findall('[a-zA-Z]*n', text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")

#16. Find Words Containing 'oo'
#text = "book food school moon notebook"
#Task: Extract all words containing the character sequence oo.

import re
text="book food school moon notebook"
result=re.findall(r'[a-zA-Z]*oo[a-zA-Z]*', text)
print(result)
print("-------------------------------------------------------------------------------------------------------------")