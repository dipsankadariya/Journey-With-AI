#basic exaample of pydantic
from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str= "dipsan" #default values
    age:Optional[int] = None #optional values

new_student={'age':32}
print(new_student)
print(type(new_student))

student=Student(**new_student) 
print(student.name)
print(student.age)

student_dict=dict(student) #converting pydantic model to dictionary
print(student_dict['name'])
student_json=student.model_dump_json() #converting pydantic model to json