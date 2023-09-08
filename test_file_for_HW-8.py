from datetime import datetime, date, timedelta
#
# users_list = [
#             {
#                 "name": "John",
#                 "birthday": (datetime.now() + timedelta(days=5)).date(),
#             },
#             {
#                 "name": "Doe",
#                 "birthday": (datetime.now() + timedelta(days=6)).date(),
#             },
#             {"name": "Alice", "birthday": (datetime.now() + timedelta(days=3)).date()},
#         ]
#
#
# def get_birthdays_per_week(users):
#     birthdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
#     days_name = {
#         0: "Monday",
#         1: "Tuesday",
#         2: "Wednesday",
#         3: "Thursday",
#         4: "Friday",
#         5: "Monday",
#         6: "Monday",
#     }
#
#     current_date = datetime.now()
#     begin_of_week = current_date.date()
#     end_of_week = current_date.date().replace(day=current_date.day + 6)
#
#     current_year = current_date.year
#     print(current_year)
#     current_month = current_date.month
#     print(current_month)
#
#     for user in users:
#         birthday = user["birthday"]
#         if current_month == 12 and birthday.month == 1:
#             birthday.replace(year=current_year+1)
#         else:
#             birthday.replace(year=current_year)
#
#         if begin_of_week <= birthday <= end_of_week:
#             name_of_the_day = days_name[birthday.weekday()]
#             birthdays[name_of_the_day].append(user["name"])
#         else:
#             continue
#
#     new_birthdays = {}
#     for key, value in birthdays.items():
#         if len(value) > 0:
#             new_birthdays[key] = value
#
#     return new_birthdays
#
# print(users_list[0])
# print(users_list[1])
# print(users_list[2])
#
# xasd = datetime.today()
# print(xasd)
#
# print(get_birthdays_per_week(users_list))

current_date = date.today()
end_of_week = current_date.replace(day=(current_date.day + 6))
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(end_of_week)