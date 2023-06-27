grade = input()

point = 0

dict ={
    'A' : 4.0,
    'B' : 3.0,
    'C' : 2.0,
    'D' : 1.0,
    'F' : 0.0
}

point += dict[grade[0]]

if '+' in grade:
    point +=0.3
elif '-' in grade:
    point -= 0.3

print(point)