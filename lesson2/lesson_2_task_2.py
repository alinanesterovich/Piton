def is_year_leap(year):
    return "Да" if year % 4 == 0 else "Нет"


num = int(input("Введите число: "))
result = is_year_leap(num)
print(f"Делится ли на четыре {num}? - {result}")
