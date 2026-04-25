from glob import translate

from services import DeadlineService
from datetime import datetime, date

def trans(a: str) -> date:
    return datetime.fromisoformat(a).date()

test_class = DeadlineService()

test_data = trans("2025-05-07")
res = test_class.calculate_deadline(test_data)
assert res == trans("2025-05-14"), f"Ожидалось - 2025-05-14, получилось - {res}"

test_data_2 = trans("2026-03-07")
res_1 = test_class.calculate_deadline(test_data_2)
assert res_1 == trans("2026-03-11"), f"Ожидалось - 2026-03-11, получилось - {res}"

test_list = ['2025-05-13', '2025-05-07', '2025-04-29', '2025-04-18', '2025-03-27']
res_reminds = test_class.get_reminder_dates(res)
assert res_reminds == [trans(i) for i in test_list], f'Даты напоминаний не сходятся'

one_hundred_percent_wrong_day = datetime.fromisoformat("2026-05-09")
check = test_class.wrong_day(one_hundred_percent_wrong_day)
assert check == True, f"Праздник определен не правильно"

print("✅ Все тесты пройдены успешно! ✅")