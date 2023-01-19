#q1
grade = int(input("enter marks"))
if grade < 25:
    print("F")
elif 25 <= grade < 45:
    print("E")
elif 45 <= grade < 50:
    print("D")
elif 50 <= grade < 60:
    print("C")
elif 60 <= grade < 80:
    print("B")
elif 80 <= grade <= 100:
    print("A")

else:
    print("enter a valid grade")


#q2
year = int(input("enter year"))
if (year) % 4 == 0 and (year)% 100 == 0 and (year) % 400 != 0 or (year)%4!=0 and (year)%100!=0 and (year)%400!=0:
    leap_year = False
else:
    leap_year = True
if leap_year==True:
    print("leao year")
else:
    print("not a leap year")

#q3
import random
question_count = 0
list = [1,2,3,4,5,6,7,8,9]
num = [9,8,7,6,5,4,3,2,1]
while question_count < 10:
    a = random.choice(list)
    b = random.choice(num)
    print(a, "x", b)
    answer = int(input("enter answer"))
    if answer == int(a)*int(b):
        print("good")
    else:
        print("think harder, its", int(a)*int(b))
    question_count += 1


#q4
x = 200
for i in range(x):
    if i%5==2 and i%6==3 and i%7==2:
        print(i)