# q1
a = input("enter string")
a.split()
if " " not in a:
    print(len(a))
else:
    spaces = a.count(" ")
    print(int(spaces) + 1)

# q2
month_numbers = {
    "jan": "1",
    "feb": "2",
    "march": "3",
    "april": "4",
    "may": "5",
    "june": "6",
    "july": "7",
    "august": "8",
    "september": "9",
    "october": "10",
    "november": "11",
    "december": "12",
}
day = (input("enter day"))
month = input("enter month")
year = input("enter year")

if month == "feb" and int(day) == 29 and int(year) % 4 == 0 and int(year) % 400 == 0:
    day = 1
    month = "march"
elif 1 <= int(day) <= 30:
    day = int(day) + 1
elif month == "feb" and int(day) == 28 and int(year) % 4 == 0 and int(year) % 400 == 0:
    day = 29
    month = "feb"
elif month == "feb" and int(day) == 29 and int(year) % 4 == 0 and int(year) % 400 != 0:
    print("invalid date")
elif month == "feb" and int(day) == 28 and int(year) % 4 == 0 and int(year) % 400 != 0:
    day = 1
    month = "march"
elif (month=="jan" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october") and int(day) == 31:
    day = 1
    a = (month_numbers[month])
    month = int(a) + 1
elif (month=="april" or month=="june" or month=="september" or month=="november") and int(day)==30:
    day = 1
    b = (month_numbers[month])
    month = int(b) + 1
elif month=="december" and int(day)==31:
    day = 1
    month = "1"
    year = int(year) + 1
elif 1<=int(day)<=30:
    day = int(day) + 1
elif int(day)>31:
    print("error")
else:
    print("invalid date")
print("the next date is ", day, "/" + (month_numbers[month]) + "/", year)



# q3
list = []
while True:
    value = (input("enter num"))
    if value=='':
        break
    list.append(value)
squares = []
while len(list)>0:
    a = list[0]
    b = int(a) * int(a)
    list.remove(a)
    squares.append((int(a),b))
print(squares)



# q4
grade_remarks = {
    int("4"): "your grade is D, poor performance",
    int("5"): "your grade is C, below average performance",
    int("6"): "your grade is c+, average performance",
    int("7"): "your grade is B, good performance",
    int("8"): "your grade is B+, very good performance",
    int("9"): "your grade is A, excellent performance",
    int("10"): "your grade is A+, outstanding performance",
}
grade = int(input("enter your grade"))
if 4 <= grade <= 10:
    print(grade_remarks[grade])
else:
    print("invalid grade")



# q5
list = ["A","B","C","D","E","F","G","H","I","J","K"]
while len(list)>=1:
    print(list)
    list.pop()


# q7
n1 = 0
n2 = 1
count = 0
terms = int(input("enter the number of terms"))
num = []
if terms==0:
    print("enter a positive integer")
elif terms==1:
    print("0")
elif terms==2:
    print(n1,n2)
else:
    while count < terms:
        print(n1)
        nth = n1 +n2
        n1=n2
        n2=nth
        count += 1
        num.append(n1)
print(num)
total = 0
x = 0
while x in range(0,len(num)):
    total = total + num[x]
    x += 1
print(total/(terms+1))

