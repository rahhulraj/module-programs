#Regular Expression Module
#Practice Tasks - Beginner, Intermediate and Advanced

#1. re.findall()
#Returns a list containing all non-overlapping matches.

#1.1 BEGINNER
#Print a list of all matches of the text "ab" in the string.
#GIVEN
#txt = "abracadabra, abacus, cab"
#EXPECTED OUTPUT
#['ab', 'ab', 'ab', 'ab']

import re
txt="abracadabra, abacus, cab"
print(re.findall("ab",txt))
print("-----------------------------------------------------------------------------------------------------------------")

#1.2 INTERMEDIATE
#Extract all the numbers (as strings) from the text.
#GIVEN
#txt = "Order 101 shipped on 12 June, 2 items cost 450 rupees"
#EXPECTED OUTPUT
#['101', '12', '2', '450']

import re
txt = "Order 101 shipped on 12 June, 2 items cost 450 rupees"
print(re.findall(r"\d+",txt))
print("-----------------------------------------------------------------------------------------------------------------")

#1.3 ADVANCED
#Extract all e-mail addresses from the text.
#GIVEN
#txt = "Contact: anu@smec.in, ravi.k@mail.com or support@tech.co.in"
#EXPECTED OUTPUT
#['anu@smec.in', 'ravi.k@mail.com', 'support@tech.co.in']

import re
txt = "Contact: anu@smec.in, ravi.k@mail.com or support@tech.co.in"
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Za-z]+"
print(re.findall(pattern, txt))
print("-----------------------------------------------------------------------------------------------------------------")

#2. re.search()
#Returns a Match object if there is a match anywhere in the string, otherwise None.

#2.1 BEGINNER
#Find the first white-space character and print its position.
#GIVEN
#txt = "Python is fun"
#EXPECTED OUTPUT
#Position: 6

import re
txt="Python is fun"
result=re.search("\s",txt)
if result:
    print("Position:",result.start())
print("-----------------------------------------------------------------------------------------------------------------")

#2.2 INTERMEDIATE
#Search for "Spain". If found, print its start and end positions using span(); otherwise print "No match".
#GIVEN
#txt = "The rain in Spain"
#EXPECTED OUTPUT
#(12, 17)

import re
txt="The rain in Spain"
result=re.search("Spain",txt)
if result:
    print(result.span())
else:
    print("No match")
print("-----------------------------------------------------------------------------------------------------------------")

#2.3 ADVANCED
#For every text in the list, find the first 4-digit year. Print the year and its start position, or "No year" if there is
#none.
#GIVEN
#texts = ["Founded in 1998, renamed in 2015", "No dates here"]
#EXPECTED OUTPUT
#1998 11
#No year

import re
texts=["Founded in 1998, renamed in 2015", "No dates here"]
for txt in texts:
    result=re.search("\d{4}", txt)
    if result:
        print(result.group(),result.start())
    else:
        print("No year")
print("-----------------------------------------------------------------------------------------------------------------")

#3. re.match()
#Matches a pattern only at the beginning of the string.

#3.1 BEGINNER
#Use re.match() to check whether the string starts with "hello". Print "Yes" or "No".
#GIVEN
#txt = "hello world"
#EXPECTED OUTPUT
#Yes

import re
txt="hello world"
result=re.match("hello",txt)
if result:
    print("Yes")
else:
    print("No")
print("-----------------------------------------------------------------------------------------------------------------")

#3.2 INTERMEDIATE
#Run both re.match() and re.search() for "hello" on the text and print both results. Observe the difference.
#GIVEN
#txt = "say hello"
#EXPECTED OUTPUT
#None
#<re.Match object; span=(4,9), match='hello'>

import re
txt = "say hello"
print(re.match("hello",txt))
print(re.search("hello",txt))
print("-----------------------------------------------------------------------------------------------------------------")


#3.3 ADVANCED
#Using re.match(), print only the items that begin with one digit followed by one or more letters.
#GIVEN
#words = ["7up", "apple", "9lives", "x1"]
#EXPECTED OUTPUT
#7up
#9lives

import re
words=["7up", "apple", "9lives", "x1"]
for word in words:
    if re.match("[0-9][A-Za-z]+",word):
        print(word)
print("-----------------------------------------------------------------------------------------------------------------")

#4. re.split()
#Returns a list where the string has been split at each match.

#4.1 BEGINNER
#Split the text at each white-space character.
#GIVEN
#txt = "The rain in Spain"
#EXPECTED OUTPUT
#['The', 'rain', 'in', 'Spain']

import re
txt="The rain in Spain"
result=re.split("\s",txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

#4.2 INTERMEDIATE
#Split the text wherever there is a comma, a semicolon or a space.
#GIVEN
#txt = "apple,banana;cherry orange"
#EXPECTED OUTPUT
#['apple', 'banana', 'cherry', 'orange']

import re
txt = "apple,banana;cherry orange"
print(re.split(r"[,; ]", txt))
print("-----------------------------------------------------------------------------------------------------------------")


#4.3 ADVANCED
#Split the timestamp at -, space and colon, then convert every part to an integer and print the list.
#GIVEN
#stamp = "2024-11-09 10:45:30"
#EXPECTED OUTPUT
#[2024, 11, 9, 10, 45, 30]

import re
stamp="2024-11-09 10:45:30"
parts=re.split("[- :]",stamp)
result=[int(part) for part in parts]
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

#5. re.sub()
#Replaces one or many matches with a string.

#5.1 BEGINNER
#Replace every white-space character with an underscore (_).
#GIVEN
#txt = "The rain in Spain"
#EXPECTED OUTPUT
#The_rain_in_Spain

import re
txt="The rain in Spain"
result=re.sub(r"\s", "_", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

#5.2 INTERMEDIATE
#Hide the phone number by replacing every digit with #.
#GIVEN
#txt = "Call 98765 now"
#EXPECTED OUTPUT
#Call ##### now

import re
txt="Call 98765 now"
result=re.sub(r"\d", "#",txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

#5.3 ADVANCED
#Clean the text: remove leading and trailing spaces, and replace every run of spaces inside with a single
#space.
#GIVEN
#txt = " Python is fun "
#EXPECTED OUTPUT
#Python is fun

import re
txt="     Python       is      fun    "
result=re.sub(r"\s+", " ",txt).strip()
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 6. re.compile()
# Compiles a pattern once so it can be reused.

# 6.1 BEGINNER
# Compile the pattern "ai" and use it to find all matches in the text.
# GIVEN
# txt = "The rain in Spain"
# EXPECTED OUTPUT
# ['ai', 'ai']

import re
txt = "The rain in Spain"
pattern = re.compile(r"ai")
result = pattern.findall(txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 6.2 INTERMEDIATE
# Compile a pattern for numbers once, and use it on both strings.
# GIVEN
# a = "Room 12, Floor 3"
# b = "Bus 405 and Bus 77"
# EXPECTED OUTPUT
# ['12', '3']
# ['405', '77']

import re
a="Room 12, Floor 3"
b="Bus 405 and Bus 77"
pattern=re.compile(r"\d+")
print(pattern.findall(a))
print(pattern.findall(b))
print("-----------------------------------------------------------------------------------------------------------------")

# 6.3 ADVANCED
# Compile a pattern for a valid time (1 or 2 digit hour, colon, minutes 00 to 59).
# Print each item with "valid" or "invalid".
# GIVEN
# times = ["11:45", "9:75", "23:59", "7:60"]
# EXPECTED OUTPUT
# 11:45 valid
# 9:75 invalid
# 23:59 valid
# 7:60 invalid

import re
times=["11:45", "9:75", "23:59", "7:60"]
pattern=re.compile(r"^(?:[01]?\d|2[0-3]):[0-5]\d$")
for time in times:
    if pattern.fullmatch(time):
        print(time, "valid")
    else:
        print(time, "invalid")
print("-----------------------------------------------------------------------------------------------------------------")


# 7. . (dot) - Any character
# Matches any single character except a newline.

# 7.1 BEGINNER
# Find a sequence that starts with "he", followed by any two characters, and an "o".
# GIVEN
# txt = "hello planet"
# EXPECTED OUTPUT
# ['hello']

import re
txt="hello planet"
result=re.findall(r"he..o", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 7.2 INTERMEDIATE
# Find all 3-letter words that start with "c" and end with "t".
# GIVEN
# txt = "cat cut cot cart cit"
# EXPECTED OUTPUT
# ['cat', 'cut', 'cot', 'cit']

import re
txt = "cat cut cot cart cit"
result = re.findall(r"\bc.t\b", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 7.3 ADVANCED
# Find all dates in the form dd?mm?yyyy, where the separator can be any single character.
# GIVEN
# dates = "12/05/2024, 13-06-2023, 1/2/2020"
# EXPECTED OUTPUT
# ['12/05/2024', '13-06-2023']

import re
dates = "12/05/2024, 13-06-2023, 1/2/2020"
result = re.findall(r"\b\d{2}.\d{2}.\d{4}\b", dates)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 8. ^ - Starts with
# Checks whether the string starts with the given pattern.

# 8.1 BEGINNER
# Check if the string starts with "hello" and print
# "Yes, the string starts with 'hello'" or "No match".
# GIVEN
# txt = "hello planet"
# EXPECTED OUTPUT
# Yes, the string starts with 'hello'

import re
txt = "hello planet"
result = re.search(r"^hello", txt)
if result:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")
print("-----------------------------------------------------------------------------------------------------------------")

# 8.2 INTERMEDIATE
# Print only the names that start with the letter "A".
# GIVEN
# names = ["Anil", "Binu", "Asha", "Ravi"]
# EXPECTED OUTPUT
# Anil
# Asha

import re
names = ["Anil", "Binu", "Asha", "Ravi"]
for name in names:
    if re.match(r"^A", name):
        print(name)
print("-----------------------------------------------------------------------------------------------------------------")

# 8.3 ADVANCED
# From the list of URLs, collect the secure ones (starting with https://)
# into a list. Print the list and its length.
# GIVEN
# urls = ["https://a.com", "http://b.com", "ftp://c.com", "https://d.org"]
# EXPECTED OUTPUT
# ['https://a.com', 'https://d.org']
# 2

import re
urls = [
    "https://a.com",
    "http://b.com",
    "ftp://c.com",
    "https://d.org"
]
secure = []
for url in urls:
    if re.match(r"^https://", url):
        secure.append(url)
print(secure)
print(len(secure))
print("-----------------------------------------------------------------------------------------------------------------")

# 9. * - Zero or more occurrences
# The preceding character can appear 0, 1 or many times.

# 9.1 BEGINNER
# Find a sequence that starts with "he", followed by 0 or more characters,
# and an "o". Notice how many matches you get.
# GIVEN
# txt = "heo helo hello"
# EXPECTED OUTPUT
# ['heo helo hello']

import re
txt = "heo helo hello"
result = re.findall(r"he.*o", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 9.2 INTERMEDIATE
# Find an "a" followed by zero or more "b" characters.
# GIVEN
# txt = "a ab abb abbb"
# EXPECTED OUTPUT
# ['a', 'ab', 'abb', 'abbb']

import re
txt = "a ab abb abbb"
result = re.findall(r"ab*", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 9.3 ADVANCED
# Print all HTML tags using the greedy pattern <.*>
# and then the lazy pattern <.*?>.
# Compare the two results.
# GIVEN
# html = "<b>bold</b> and <i>italic</i>"
# EXPECTED OUTPUT
# ['<b>bold</b> and <i>italic</i>']
# ['<b>', '</b>', '<i>', '</i>']

import re
html = "<b>bold</b> and <i>italic</i>"
print(re.findall(r"<.*>", html))
print(re.findall(r"<.*?>", html))
print("-----------------------------------------------------------------------------------------------------------------")

# 10. + - One or more occurrences
# The preceding character must appear at least once.

# 10.1 BEGINNER
# Find a sequence that starts with "he", followed by 1 or more characters,
# and an "o".
# GIVEN
# txt = "ho heo helo hello"
# EXPECTED OUTPUT
# ['heo helo hello']

import re
txt = "ho heo helo hello"
result = re.findall(r"he.+o", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 10.2 INTERMEDIATE
# Find every run of one or more "a" characters.
# GIVEN
# txt = "baaad cab aa"
# EXPECTED OUTPUT
# ['aaa', 'a', 'aa']

import re
txt = "baaad cab aa"
result = re.findall(r"a+", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 10.3 ADVANCED
# Extract all hashtags (a # followed by letters or digits).
# GIVEN
# txt = "Loving #Python and #regex101 today #AI"
# EXPECTED OUTPUT
# ['#Python', '#regex101', '#AI']

import re
txt = "Loving #Python and #regex101 today #AI"
result = re.findall(r"#[A-Za-z0-9]+", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 11. ? - Zero or one occurrence
# The preceding character is optional.

# 11.1 BEGINNER
# Find a sequence that starts with "he", followed by 0 or 1 character,
# and an "o".
# GIVEN
# txt = "heo helo hello"
# EXPECTED OUTPUT
# ['heo', 'helo']

import re
txt = "heo helo hello"
result = re.findall(r"he.?o", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 11.2 INTERMEDIATE
# Match both spellings: "color" and "colour".
# GIVEN
# txt = "color colour colr"
# EXPECTED OUTPUT
# ['color', 'colour']

import re
txt = "color colour colr"
result = re.findall(r"colou?r", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 11.3 ADVANCED
# Extract all numbers, whole or decimal.
# GIVEN
# txt = "Prices: 45, 12.5, 100.75, 3"
# EXPECTED OUTPUT
# ['45', '12.5', '100.75', '3']


import re
txt = "Prices: 45, 12.5, 100.75, 3"
result = re.findall(r"\d+(?:\.\d+)?", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 12. {} - Exact number of occurrences
# Specifies exactly how many times (or between how many times) a pattern repeats.

# 12.1 BEGINNER
# Find a sequence that starts with "he", followed by exactly 2 characters,
# and an "o".
# GIVEN
# txt = "helo hello"
# EXPECTED OUTPUT
# ['hello']

import re
txt = "helo hello"
result = re.findall(r"he..o", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 12.2 INTERMEDIATE
# Find all 4-digit numbers.
# GIVEN
# txt = "Years 1998 and 2015 had 123 items"
# EXPECTED OUTPUT
# ['1998', '2015']

import re
txt = "Years 1998 and 2015 had 123 items"
result = re.findall(r"\b\d{4}\b", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 12.3 ADVANCED
# Print only the valid 10-digit mobile numbers
# (the first digit must be 6, 7, 8 or 9).
# GIVEN
# nums = ["9876543210", "1234567890", "98765", "8123456789"]
# EXPECTED OUTPUT
# 9876543210
# 8123456789

import re
nums = [
    "9876543210",
    "1234567890",
    "98765",
    "8123456789"
]
pattern = r"^[6-9]\d{9}$"
for num in nums:
    if re.fullmatch(pattern, num):
        print(num)
print("-----------------------------------------------------------------------------------------------------------------")

# 13. $ - Ends with
# Checks whether the string ends with the given pattern.

# 13.1 BEGINNER
# Check if the string ends with "planet" and print
# "Yes, the string ends with 'planet'" or "No match".
# GIVEN
# txt = "hello planet"
# EXPECTED OUTPUT
# Yes, the string ends with 'planet'

import re
txt = "hello planet"
result = re.search(r"planet$", txt)
if result:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")
print("-----------------------------------------------------------------------------------------------------------------")

# 13.2 INTERMEDIATE
# Print only the file names that end with ".py".
# GIVEN
# files = ["a.py", "b.txt", "c.py", "d.pyc"]
# EXPECTED OUTPUT
# a.py
# c.py

import re
files = ["a.py", "b.txt", "c.py", "d.pyc"]
for file in files:
    if re.search(r"\.py$", file):
        print(file)
print("-----------------------------------------------------------------------------------------------------------------")

# 13.3 ADVANCED
# Print the strings that start with a letter AND end with a digit.
# GIVEN
# items = ["abc1", "1abc", "ab", "x9y9"]
# EXPECTED OUTPUT
# abc1
# x9y9

import re
items = ["abc1", "1abc", "ab", "x9y9"]
pattern = r"^[A-Za-z].*\d$"
for item in items:
    if re.search(pattern, item):
        print(item)
print("-----------------------------------------------------------------------------------------------------------------")


# 14. | - Either or
# Matches either the pattern on the left or the pattern on the right.

# 14.1 BEGINNER
# Check if the string contains either "falls" or "stays".
# Print the list of matches and a message.
# GIVEN
# txt = "The rain in Spain falls mainly in the plain!"
# EXPECTED OUTPUT
# ['falls']
# Yes, there is at least one match!

import re
txt = "The rain in Spain falls mainly in the plain!"
result = re.findall(r"falls|stays", txt)
print(result)
if result:
    print("Yes, there is at least one match!")
else:
    print("No match")
print("-----------------------------------------------------------------------------------------------------------------")


# 14.2 INTERMEDIATE
# Find all occurrences of "cat" or "dog".
# GIVEN
# txt = "I have a cat and a dog, no bird"
# EXPECTED OUTPUT
# ['cat', 'dog']

import re
txt = "I have a cat and a dog, no bird"
result = re.findall(r"cat|dog", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 14.3 ADVANCED
# Print only the image files that end with .jpg or .png.
# GIVEN
# files = ["a.jpg", "b.gif", "c.png", "d.jpg.bak"]
# EXPECTED OUTPUT
# a.jpg
# c.png

import re
files = ["a.jpg", "b.gif", "c.png", "d.jpg.bak"]
pattern = r"\.(jpg|png)$"
for file in files:
    if re.search(pattern, file):
        print(file)
print("-----------------------------------------------------------------------------------------------------------------")


# 15. [ ] Sets and ranges
# A set is a group of characters inside square brackets with a special meaning:
# [arn], [a-n], [0-9], [0-5][0-9], [a-zA-Z].

# 15.1 BEGINNER
# Find all lower-case vowels in the text.
# GIVEN
# txt = "Regular Expression"
# EXPECTED OUTPUT
# ['e', 'u', 'a', 'e', 'i', 'o']

import re
txt = "Regular Expression"
result = re.findall(r"[aeiou]", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 15.2 INTERMEDIATE
# Find all two-digit numbers between 00 and 59.
# GIVEN
# txt = "Scores: 72, 15, 48, 99"
# EXPECTED OUTPUT
# ['15', '48']

import re
txt = "Scores: 72, 15, 48, 99"
result = re.findall(r"\b[0-5][0-9]\b", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")

# 15.3 ADVANCED
# A password is "strong" if it has at least one upper-case letter,
# one lower-case letter and one digit.
# Print each password with its result.
# GIVEN
# pwds = ["Python123", "python", "PYTHON9", "Py1"]
# EXPECTED OUTPUT
# Python123 strong
# python weak
# PYTHON9 weak
# Py1 strong

import re
pwds = ["Python123", "python", "PYTHON9", "Py1"]
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).+$"
for pwd in pwds:
    if re.search(pattern, pwd):
        print(pwd, "strong")
    else:
        print(pwd, "weak")
print("-----------------------------------------------------------------------------------------------------------------")


# 16. [^ ] Negated sets
# A caret at the start of a set returns a match for any character EXCEPT
# those listed.

# 16.1 BEGINNER
# Find all characters that are not "a" or "n".
# GIVEN
# txt = "banana"
# EXPECTED OUTPUT
# ['b']

import re
txt = "banana"
result = re.findall(r"[^an]", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")


# 16.2 INTERMEDIATE
# Extract only the letters (everything that is not a digit)
# and join them into one string.
# GIVEN
# txt = "a1b2c3"
# EXPECTED OUTPUT
# abc

import re
txt = "a1b2c3"
result = re.findall(r"[^0-9]", txt)
print("".join(result))
print("-----------------------------------------------------------------------------------------------------------------")


# 16.3 ADVANCED
# Remove every character that is not a letter from the text.
# GIVEN
# txt = "H3ll0 W0r1d!"
# EXPECTED OUTPUT
# HllWrd

import re
txt = "H3ll0 W0r1d!"
result = re.sub(r"[^A-Za-z]", "", txt)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")
