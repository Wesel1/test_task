from datetime import timedelta, date
import holidays


class DeadlineService:
    def __init__(self):
        self.ru_holidays = holidays.Russia()
        self.tuple_reminders = (1, 3, 7, 14, 30)

    def calculate_deadline(self, event_date: date, days: int) -> date:
        deadline = event_date
        i = 0
        while i < days:
            deadline += timedelta(days=1)
            if not self.wrong_day(deadline):
                i += 1
        return deadline

    def get_reminder_dates(self, deadline: date) -> list[date]:
        date_reminders = []
        for i in self.tuple_reminders:
            deadline_copy = deadline
            count = 0
            while count < i:
                deadline_copy -= timedelta(days=1)
                if not self.wrong_day(deadline_copy):
                    count += 1
            date_reminders.append(deadline_copy)
        return date_reminders

    def wrong_day(self, day: date) -> True | False:
        is_holiday = day in self.ru_holidays
        is_weekend = day.weekday() > 4

        return is_holiday or is_weekend
