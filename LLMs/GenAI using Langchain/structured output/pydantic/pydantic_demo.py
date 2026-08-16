#basic exaample of pydantic
from pydantic import BaseModel

class Student(BaseModel):
    name: str

new_student={'name': "dipsan kadariyaa"}
#new_student= {'name':32} #this will throw an error because name is expected to be a string but we are passing an integer
print(type(new_student))

student=Student(**new_student) 
print(student)
print(type(student))