from datetime import date

import pytest

from services import DeadlineService


@pytest.fixture
def service():
    return DeadlineService()


def test_wrong_day_returns_false_for_business_day(service):
    assert service.wrong_day(date(2025, 6, 4)) is False


def test_wrong_day_returns_true_for_non_business_days(service):
    assert service.wrong_day(date(2025, 6, 7)) is True
    assert service.wrong_day(date(2025, 1, 1)) is True


def test_calculate_deadline_without_skipped_days(service):
    result = service.calculate_deadline(event_date=date(2025, 6, 2), days=3)

    assert result == date(2025, 6, 5)


def test_calculate_deadline_skips_weekend(service):
    result = service.calculate_deadline(event_date=date(2025, 6, 5), days=3)

    assert result == date(2025, 6, 10)


def test_calculate_deadline_skips_russian_holidays(service):
    result = service.calculate_deadline(event_date=date(2025, 6, 10), days=3)

    assert result == date(2025, 6, 17)


def test_get_reminder_dates_returns_expected_business_days(service):
    reminders = service.get_reminder_dates(deadline=date(2025, 6, 16))

    assert reminders == [
        date(2025, 6, 11),
        date(2025, 6, 9),
        date(2025, 6, 3),
        date(2025, 5, 23),
        date(2025, 4, 25),
    ]
