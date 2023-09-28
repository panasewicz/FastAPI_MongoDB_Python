from fastapi import FastAPI
import db, models

app = FastAPI()

@app.get("/")
def root():
    return {"message": "HI"}

@app.get("/allStudents")
def get_all():
    data = db.all()
    return {"data": data}

@app.post("/createStudent")
def create(data:models.students):
    id = db.create(data)
    return {"inserted": True, "inserted_id": id}

@app.post("/createMessage")
def create2(data:models.message):
    id = db.create2(data)
    return {"inserted": True, "inserted_id": id}

@app.get("/message_date/{id}")
def get_student(id:str):
    data = db.get_student(id)
    #data = list(data)
    return {"Dane Studenta": data}

@app.delete("/deleteStudent")
def delete(name:str):
    data = db.delete(name)
    return {"deleted": True, "deleted_count": data}

@app.put("/update")
def update(name:str, data:models.students):
    data = models.students(name=data.name, lastname = data.lastname)
    data = db.update(data)
    return {"updated": True, "updated_count": data}

@app.get("/get/{studentId, name, lastname}")
def get_messages(studentId:str, name:str, lastname:str):
    data = db.get_all_messages(studentId, name, lastname)
    return {"Wiadomości Studenta": data}








