import re
from functools import reduce
# 1
# def sum_func(x, y):
#     return x + y
#
#
# def subtraction_func(x, y):
#     return x - y
#
#
# def get_operator(operator):
#     if operator == '+':
#         return sum_func
#     elif operator == '-':
#         return subtraction_func
#     else:
#         print('Unknown operator')
#
#
# sum_action_function = get_operator("+")
# print(sum_action_function(2, 3))  # 5
#
# sub_action_function = get_operator("-")
# print(sub_action_function(2, 3))  # -1
#
# print(get_operator("+")(2,3))

# 2

# DEFAULT_DISCOUNT = 0.05
#
# def get_discount_price_customer(price, customer):
#     discount = customer.get("discount", DEFAULT_DISCOUNT)
#     return price*(1-discount)
#
# print(get_discount_price_customer(100, {"name": "Boris", "discount": 0.15}))
# print(get_discount_price_customer(100, {"name": "Boris"}))

# 3
# def adder(val):
#     def inner(x):
#         return x + val
#     return inner
#
#
# two_adder = adder(2)
# print(adder(2)(2))
# print(two_adder(3)) # 5
# print(two_adder(5)) # 7
#
# three_adder = adder(3)
# print(three_adder(5))   # 8
# print(three_adder(-3))  # 0
#
# id(two_adder) == id(three_adder)    # False

# 4 кеш для декількох ітерацій
# def caching_fibonacci(n, cache = {}):
#     if n in cache:
#         print("Using cache")
#         return cache[n]
#     else:
#         def fibonacci(x):
#             if x == 0:
#                 return 0
#             elif x == 1:
#                 return 1
#             else:
#                 val = fibonacci(x-1) + fibonacci(x-2)
#                 cache[n] = val
#                 return val
#
#     return fibonacci(n)

# 5 кеш передзаповнений кожен раз
# def caching_fibonacci():
#     cache = {0:0, 1:1 , 2:1}
#     def fibonacci(n):
#         if n not in cache:
#             cache[n] = fibonacci(n-1) + fibonacci(n-2)
#         return cache[n]
#
#     return fibonacci
#
# print(caching_fibonacci()(5))

# 6 Карування
# def sum_func(x, y):
#     return x + y
#
# def sub_func(x, y):
#     return x - y
#
# OPERATIONS = {
#     '-': sub_func,
#     '+': sum_func
# }
#
# def get_handler(operator):
#     return OPERATIONS[operator]
#
# handler = get_handler('-')
# handler(2, 3)           # -1
#
# get_handler('+')(2, 3)  # 5

# 7 Карування
# def discount_price(discount):
#     def price(price):
#         return price * (1 - discount)
#
#     return price
#
# cost_15 = discount_price(0.15)
# cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)
#
# price = 100
# print(cost_15(price))
# print(cost_10(price))
# print(cost_05(price))

# 8 Декоратор
# def format_phone_number(func):
#     def inner(phone):
#         cleaned_phone = func(phone)
#         if len(cleaned_phone) == 10:
#             return f"+38{cleaned_phone}"
#         elif len(cleaned_phone) == 12:
#             return f"+{cleaned_phone}"
#
#     return inner
# @format_phone_number
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone
#
# print(sanitize_phone_number("    +(050)123-32-34"))

# 9 Декоратор
# def logged_func(func):
#     def inner(x, y):
#         print(f'Called with {x}, {y}')
#         result = func(x, y)
#         # print(f'Result: {result}')
#         return f"Result is {result}"
#     return inner
# @logged_func
# def complicated(x, y):
#     return x / y
#
# print(complicated(6, 3))

# 10 yield
# def interval_generator(x, y):
#     while x <= y:
#         yield x
#         x += 1


# five_to_ten_generator = interval_generator(5, 10)
#
# print(five_to_ten_generator)
# next(five_to_ten_generator) # 5
# next(five_to_ten_generator) # 6
# next(five_to_ten_generator) # 7
# next(five_to_ten_generator) # 8
# next(five_to_ten_generator) # 9
# next(five_to_ten_generator) # 10

# 11
# def logger(func):
#     def inner(*args):
#         sum = 0
#         for i in args:
#             sum += i
#         print(sum)
#         print(func(*args))
#
#     return inner
# @logger
# def func(*args):
#     mul = 1
#     for i in args:
#         mul = mul * i
#     return mul
#
# result = func(2, 3, 4)
# print(result)

# 12
# def first_second_counter():
#     while True:
#         yield 1
#         yield 2
#
# my_generation = first_second_counter()
# for _ in range(6):
#     print(next(my_generation))

# 13
# def odd_squares(limit):
#     for value in range(limit):
#         if value % 2:
#             yield pow(value, 2)
#
# limit = 15
#
# get_value = filter(lambda value: bool(value % 2), map(lambda x: pow(x, 2), list(range(limit))))
#
# for result in zip(get_value, odd_squares(limit)):
#     print(result[0], result[1])

#14 Генератор yield
# text = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
#
# def generator_numbers(string=""):
#     list_of_numbers = re.findall("\d+", string)
#     for number in list_of_numbers:
#         yield int(number)
#
# def sum_profit(string):
#     profit_generator = generator_numbers(string)
#
#     total_profit = sum(profit_generator)
#     return total_profit
#
# print(sum_profit(text))

#15
# name = ["dan", "jane", "steve", "mike"]
#
# def normal_name(list_name):
#     new_list_of_names = []
#     for i in map(lambda name: name.capitalize(), list_name):
#         new_list_of_names.append(i)
#     return new_list_of_names
#
# print(normal_name(name))

# 16
# list_of_contacts = [{"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False,}, {"name": "Allen Raymond", "email": "nulasdasdla.ante@gmail.com", "phone": "(992) 914-3792","favorite": False,}]
#
# def get_emails(list):
#     list_of_emails = []
#     for i in map(lambda dict: dict['email'], list):
#         list_of_emails.append(i)
#     return list_of_emails
#
# print(get_emails(list_of_contacts))

# 17
# payment = [100, -3, 400, 35, -100]
#
# def positive_values(list_payment):
#     final_list = []
#     for i in filter(lambda x: x>0, list_payment):
#         final_list.append(i)
#     return final_list
#
# print(positive_values(payment))

# 18
# list_of_contacts = [{"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False,}, {"name": "Allen Raymond", "email": "nulasdasdla.ante@gmail.com", "phone": "(992) 914-3792","favorite": True,}]
#
# def get_favorites(contacts):
#     list_of_favorites = []
#     for i in filter(lambda dict: dict["favorite"] is True, contacts):
#         list_of_favorites.append(i)
#     return list_of_favorites
#
# print(get_favorites(list_of_contacts))

# 19
# from functools import reduce
#
# result = reduce((lambda x, y: x * y), [1, 2, 3, 4], 5) # Число 5 це число, яке буде в першій ітерації братися за x
#
# print(result)

# 20
# payment = [1, -3, 4]
#
# def amount_payment(payment):
#     return reduce(lambda x, y: x+y, (y for y in payment if y>0), 0)
#
# print(amount_payment(payment))

list = [{'name': 'John', 'phone': '123'}, {'name': 'Smith', 'phone': '123453'}]

for user in list:
    if 'John' in user.values():
        print("True")
    else:
        print(False)