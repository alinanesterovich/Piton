def is_year_leap(year):
    return year % 4 == 0


result = is_year_leap(2020)
print(f"год {2020}: {result}")