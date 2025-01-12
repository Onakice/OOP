day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def day_of_year(day, month, year):
    if is_leap(year):
        day_in_month[1] = 29
    return sum(day_in_month[:month-1]) + day

def day_in_year(year):
    if is_leap(year):
        return 366
    return 365

def date_diff(date1, date2):
    d1, m1, y1 = date1.split('-')
    d2, m2, y2 = date2.split('-')

    diff_date = 0

    diff_date += day_in_year(int(y1)) - day_of_year(int(d1),int(m1),int(y1)) +1

    for year in range(int(y1)+1, int(y2)):
        diff_date += day_in_year(year)
        # print(diff_date)

    diff_date += day_of_year(int(d1),int(m1),int(y1))

    return diff_date

print(date_diff('25-12-1999', '9-3-2000'))
print(date_diff('1-1-2018', '1-1-2020'))
