from datetime import date

import pytest

from services import DeadlineService


@pytest.fixture
def service():
    return DeadlineService()


@pytest.mark.parametrize(
    "input_date, expected",
    [
        (date(2025, 6, 4), False),  # среда
        (date(2025, 6, 7), True),   # суббота
        (date(2025, 1, 1), True),   # Новый год
    ]
)
def test_wrong_day(service, input_date, expected):
    assert service.wrong_day(input_date) == expected


def test_calculate_deadline_without_weekend(service):
    result = service.calculate_deadline(
        event_date=date(2025, 6, 2),
        days=3,
    )

    assert result == date(2025, 6, 5)


def test_calculate_deadline_with_weekend(service):
    result = service.calculate_deadline(
        event_date=date(2025, 6, 5),
        days=3,
    )

    assert result == date(2025, 6, 10)


def test_calculate_deadline_zero_days(service):
    result = service.calculate_deadline(
        event_date=date(2025, 6, 2),
        days=0,
    )

    assert result == date(2025, 6, 2)


def test_get_reminder_dates_count(service):
    reminders = service.get_reminder_dates(
        deadline=date(2025, 6, 16)
    )

    assert len(reminders) == 5


def test_get_reminder_dates_exact_values(service):
    reminders = service.get_reminder_dates(
        deadline=date(2025, 6, 16)
    )

    expected = [
        date(2025, 6, 11),
        date(2025, 6, 9),
        date(2025, 6, 3),
        date(2025, 5, 23),
        date(2025, 4, 25),
    ]
    assert reminders == expected


def test_reminders_are_before_deadline(service):
    deadline = date(2025, 6, 16)

    reminders = service.get_reminder_dates(deadline)

    assert all(reminder < deadline for reminder in reminders)


def test_reminders_order(service):
    reminders = service.get_reminder_dates(
        deadline=date(2025, 6, 16)
    )

    assert reminders[0] > reminders[1] > reminders[2] > reminders[3] > reminders[4]





#     "reminders": [
#     "2025-06-11",
#     "2025-06-09",
#     "2025-06-03",
#     "2025-05-23",
#     "2025-04-25"
#   ]