#basic exaample of pydantic
from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str= "dipsan" #default values
    age:Optional[int] = None #optional values

new_student={'age':'32'}  # we input age in string format to check if pydantic can coerce it to int
print(new_student)
print(type(new_student))

student=Student(**new_student) 
print(student.name)
print(student.age)
