from fastapi import FastAPI
from fastapi.params import Query, Path
from typing import Optional
from pydantic import BaseModel
import uuid

# Create an instance of FastAPI
app = FastAPI()

# Create a class that inherits from BaseModel
class User(BaseModel):
    id: str = str(uuid.uuid4())
    student_name: str
    student_age: int
    student_location: str
    student_country: str
    student_email: str

# Create a dictionary to store the students
students_repo = {
    "Stanley": {
        "id": str(uuid.uuid4()),
        "student_name": "Sunday Stanley",
        "student_age": 20,
        "student_location": "London",
        "student_country": "United Kingdom",
        "student_email": "sundayobinna@gmail.com",
    },
    "Ade": {
        "id": str(uuid.uuid4()),
        "student_name": "Jane Ade",
        "student_age": 22,
        "student_location": "Paris",
        "student_country": "France",
        "student_email": "ade@gmail.com",
    },
    "Bola": {
        "id": str(uuid.uuid4()),
        "student_name": "John Bola",
        "student_age": 20,
        "student_location": "London",
        "student_country": "United Kingdom",
        "student_email": "Bola@gmail.com",
    },
    "Blessing": {
        "id": str(uuid.uuid4()),
        "student_name": "Smith Blessing",
        "student_age": 22,
        "student_location": "Paris",
        "student_country": "France",
        "student_email": "Blessing@gmail.com",
    },
    "Chika Nwanne": {
        "id": str(uuid.uuid4()),
        "student_name": "Chika Ike",
        "student_age": 30,
        "student_location": "London",
        "student_country": "United Kingdom",
        "student_email": "chika@gmail.com",
    },
    "Chinwe": {
        "id": str(uuid.uuid4()),
        "student_name": "Chinwe Nmeri",
        "student_age": 22,
        "student_location": "Paris",
        "student_country": "France",
        "student_email": "chinwe@gmail.com",
    },
}

# Create a route to get all the students
@app.get("/")
async def homepage():
    return students_repo

# Create a route to get a specific student
@app.get("/students/{student_name}")
async def get_student(student_name: str = Path(..., title="The name of the student you want to get", description="The name of the student you want to get", example="Stanley")):
    if student_name in students_repo:
        return students_repo[student_name]
    return {"message": "Student not found"}

# Create a route to create a new student
@app.post("/createstudent")
async def create_new_student(user: User) -> dict:
    if user.student_name in students_repo:
        return {"message": "Student already exists"}
    else:
        user.id = str(uuid.uuid4())
        students_repo[user.student_name] = user.dict()
        return students_repo

# Create a route to update a student    
@app.put("/updatestudent/{student_name}")
async def update_student(user: User, student_name: str = Path(..., title="The name of the student you want to update", description="The name of the student you want to update", example="Stanley")) -> dict:
    if student_name in students_repo:
        students_repo[student_name] = user.dict()
        return students_repo
    else:
        return {"message": "Student not found"}


 # Create a route to delete a student   
@app.delete("/deletestudent/{student_name}")
async def delete_student(student_name: str = Path(..., title="The name of the student you want to delete", description="The name of the student you want to delete", example="Stanley")) -> dict:
    if student_name in students_repo:
        del students_repo[student_name]
        return {"message": f"{student_name} has been deleted and the new list of students is {list(students_repo.keys())}"}
    else:
        return {"message": "Student not found"}
