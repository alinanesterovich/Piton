def is_year_leap(year):
    return year % 4 == 0


num = 2020
result = is_year_leap(num)
print(f"год {num}: {result}")