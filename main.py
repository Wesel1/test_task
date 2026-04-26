import uvicorn
from fastapi import FastAPI, HTTPException
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


@app.post("/calculate", response_model=Answer)
def calculate_deadlines(request: Event):
    try:
        deadline = service.calculate_deadline(event_date=request.event_date, days=3)
        reminders = service.get_reminder_dates(deadline=deadline)
        return Answer(deadline=deadline, reminders=reminders)
    except:
        raise HTTPException(status_code=400)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)