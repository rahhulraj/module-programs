#1. Student Details
#Create a Python dictionary containing a student's name, age, course, and marks. Convert the dictionary into JSON format and display the result.

import json
studentdetails={"name":"John","age":22,"course":"Python","marks":90}
result=json.dumps(studentdetails)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------")

#2. JSON Student Data
#Consider the following JSON data:
#student = '{"name":"Anu","age":22,"course":"Python","mark":85}'
#Convert this JSON data into a Python object and display the student's name, course, and mark.

import json
student='{"name":"Anu","age":22,"course":"Python","mark":85}'
data=json.loads(student)
print("Name:",data["name"])
print("Course:",data["course"])
print("Mark:",data["mark"])
print("-----------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------")

#3. Product Information
#Create a dictionary containing:
#Product name
#Price
#Category
#Stock
#Convert it into JSON format so that there are no unnecessary spaces between keys, values, and items.

import json
product={"product_name":"Laptop","price":65000,"category":"Electronics","stock":20}
result=json.dumps(product,separators=(',',':'))
print(result)
print("-----------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------")

#4. Employee Details
#Create a nested dictionary containing an employee's personal details and job details. Convert it into a properly formatted
#  JSON string with 4 levels of indentation.

import json
employee={
    "personal_details":{"name":"Robert","age":35,"address":"America"},
    "job_details":{"department":"IT","salary":50000,"position":"Developer"}
}
result=json.dumps(employee,indent=4)
print(result)
print("-----------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------")

#5. Sorted Employee Data
#Create a dictionary containing the following information:
#salary
#name
#department
#employee_id
#age
#Convert the dictionary into JSON format with the keys arranged in alphabetical order.

import json
employee={"salary":40000,"name":"Steve","department":"HR","employee_id":101,"age":33}
result=json.dumps(employee,sort_keys=True)
print(result)