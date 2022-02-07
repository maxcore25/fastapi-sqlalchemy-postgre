from typing import Optional
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from schemas import CreateJobRequest
from sqlalchemy.orm import Session
from database import get_db
from models import Job

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=origins,
    allow_headers=origins,
)


@app.post("/")
def create(details: CreateJobRequest, db: Session = Depends(get_db)):
    to_create = Job(
        title=details.title,
        description=details.description
    )
    db.add(to_create)
    db.commit()
    return {
        'success': True,
        'created_id': to_create.id
    }


@app.get("/")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Job).filter(Job.id == id).first()


@app.delete("/")
def delete(id: int, db: Session = Depends(get_db)):
    db.query(Job).filter(Job.id == id).delete()
    db.commit()
    return {'success': True}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')

    # Or use terminal command: uvicorn main:app --reload
