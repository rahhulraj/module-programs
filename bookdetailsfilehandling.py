#Task 3: Read Book Details
#Create a text file named book.txt and write the following content into it:

#Book ID: B102
#Book Name: Python Programming
#Author: James Smith
#Publisher: Tech Publications
#Price: 650

#Requirements:
#1. Open the book.txt file in read mode ("r").
#2. Read the entire content of the file.
#3. Display the content using print().
#4. Close the file.
#5. Display whether the file is closed or not.

fileptr=open(r"C:\SMEC\filehandling\book.txt", "r")
content=fileptr.read()
print(content)
fileptr.close()
print("IS FILE CLOSED ? :", fileptr.closed)