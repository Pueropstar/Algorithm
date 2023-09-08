from sys import stdin

input = stdin.readline


N = int(input())

dict_student = {}

arr_year =[]
arr_yong_month = []
arr_yong_day = []


for i in range(N):
    name, day, month, year = input().split()
    
    dict_student[name] = {
        "day" : int(day),
        "month" : int(month),
        "year" : int(year)
    }
    arr_year.append(int(year))

arr_old_month = []
arr_old_day = []

old_year = sorted(arr_year)[0] #늙은넘
yong_year = sorted(arr_year)[-1] #젊은넘

dict_keys = list(dict_student.keys())
for i in dict_keys:
    if dict_student.get(i)["year"]==old_year:
        arr_old_month.append(dict_student.get(i)["month"])
    if dict_student.get(i)["year"]==yong_year:
        arr_yong_month.append(dict_student.get(i)["month"])
    

old_month = sorted(arr_old_month)[0]
yong_month = sorted(arr_yong_month)[-1]

for i in dict_keys:
    if dict_student.get(i)["month"] == old_month:
        arr_old_day.append(dict_student.get(i)["day"])
    if dict_student.get(i)["year"]==yong_year:
        arr_yong_day.append(dict_student.get(i)["day"])

old_day = sorted(arr_old_day)[0]
yong_day = sorted(arr_yong_day)[-1]

oldest_man = ""
yongest_man = ""
for i in dict_keys:
    if dict_student.get(i)["year"] == yong_year and dict_student.get(i)["month"] == yong_month and dict_student.get(i)["day"] == yong_day:
        yongest_man = i
    if dict_student.get(i)["year"] == old_year and dict_student.get(i)["month"] == old_month and dict_student.get(i)["day"] == old_day:
        oldest_man = i

print(yongest_man)
print(oldest_man)