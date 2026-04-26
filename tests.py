from services import DeadlineService
from datetime import datetime, date

def trans(a: str) -> date:
    return datetime.fromisoformat(a).date()

service = DeadlineService()

def test_feb28_2025():
    deadline = service.calculate_deadline(trans("2025-02-28"), 3)
    assert deadline == trans("2025-03-05"), f"Expected 2025-03-05, got {deadline}"

def test_mar6_2025():
    deadline = service.calculate_deadline(trans("2025-03-06"), 3)
    assert deadline == trans("2025-03-11"), f"Expected 2025-03-11, got {deadline}"

def test_monday_after_holiday():
    deadline = service.calculate_deadline(trans("2025-05-12"), 3)
    assert deadline == trans("2025-05-15"), f"Expected 2025-05-15, got {deadline}"

def test_reminder_dates():
    deadline = trans("2025-03-05")
    reminders = service.get_reminder_dates(deadline)
    expected = [
        "2025-03-04",
        "2025-02-28",
        "2025-02-24",
        "2025-02-13",
        "2025-01-22"
    ]
    assert reminders == [trans(i) for i in expected], f"Expected {expected}, got {reminders}"

if __name__ == "__main__":
    test_feb28_2025()
    test_mar6_2025()
    test_monday_after_holiday()
    test_reminder_dates()
    print("✅ Все тесты пройдены ✅")