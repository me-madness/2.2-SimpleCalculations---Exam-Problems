work_days_in_months = int(input())
money_for_day = float(input())
dolars = float(input())

work_days_for_one_year = ((work_days_in_months * 12) + (work_days_in_months *2.5)) * money_for_day
tax = work_days_for_one_year * 0.25
clear_money = work_days_for_one_year - tax
total = clear_money * dolars
levs_for_day = total / 365
print(round(levs_for_day, 2))