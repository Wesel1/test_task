import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from datetime import date

from services import DeadlineService


service = DeadlineService()


class Event(BaseModel):
    event_date: date


class Answer(BaseModel):
    deadline: date
    reminders: list[date]


app = FastAPI()


@app.get('/')
def home():
    return {"status": "ok"}

@app.post("/calculate", response_model=Answer)
def calculate_deadlines(request: Event):
    deadline = service.calculate_deadline(event_date=request.event_date)
    reminders = service.get_reminder_dates(deadline=deadline)
    return Answer(deadline=deadline, reminders=reminders)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)