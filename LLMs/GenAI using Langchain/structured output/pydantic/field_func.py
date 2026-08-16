from pydantic import BaseModel,EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str= "dipsan" #default values
    age:Optional[int] = None #optional values
    email: EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description="Student's cumulative grade point average") #gt means greater than and lt means less than

new_student={'age':32,'email':"dipsank@gmail.com", 'cgpa':8.5} 

student =Student(**new_student)

print(student.email) 
print(student.cgpa )
