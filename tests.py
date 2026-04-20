from services import DeadlineService
from datetime import datetime

test_class = DeadlineService()

test_data = "2025-05-07"
res = test_class.calculate_deadline(test_data)
assert res == "2025-05-14", f"Ожидалось - 2025-05-14, получилось - {res}"

test_data_2 = "2026-03-07"
res_1 = test_class.calculate_deadline(test_data_2)
assert res_1 == "2026-03-11", f"Ожидалось - 2026-03-11, получилось - {res}"

res_reminds = test_class.get_reminder_dates(res)
assert res_reminds == ['2025-05-13', '2025-05-07', '2025-04-29', '2025-04-18', '2025-03-27'], f'Даты напоминаний не сходятся'

one_hundred_percent_wrong_day = datetime.fromisoformat("2026-05-09")
check = test_class.wrong_day(one_hundred_percent_wrong_day)
assert check == True, f"Праздник определен не правильно"

print("✅ Все тесты пройдены успешно! ✅")