#basic exaample of pydantic
from pydantic import BaseModel

class Student(BaseModel):
    name: str= "dipsan" #default values

new_student={}

print(type(new_student))

student=Student(**new_student) 
print(student.name)