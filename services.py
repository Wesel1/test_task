from datetime import datetime, timedelta, date
import holidays


class DeadlineService():
    def __init__(self):
        self.ru_holidays = holidays.Russia()

    def calculate_deadline(self, event_date: str) -> str:
        deadline = datetime.fromisoformat(event_date).date()
        i = 0
        while i < 3:
            deadline += timedelta(days=1)
            if not self.wrong_day(deadline):
                i += 1
        return str(deadline)


    def get_reminder_dates(self, deadline: str) -> list[str]:
        date_reminders = []
        tuple_reminders = (1, 3, 7, 14, 30)
        for i in tuple_reminders:
            deadline_copy = datetime.fromisoformat(deadline).date()
            count = 0
            while count < i:
                deadline_copy -= timedelta(days=1)
                if not self.wrong_day(deadline_copy):
                    count += 1
            date_reminders.append(str(deadline_copy))
        return date_reminders


    def wrong_day(self, day: date) -> True | False:
        is_holiday = day in self.ru_holidays
        is_weekend = day.weekday() > 4

        return is_holiday or is_weekend