friends = ["Rolf", "Jen", "Anne"]

for friend in friends:
    print(friend)

for friend in friends :
    print(f"{friend} is my friend.")

#####################################################################################

grades = [35, 65, 75, 85, 90]
total = 0

for grade in grades :
    total += grade
print("Total of grades: " + str(total))
avg_grades = total/len(grades)
print("Average of grades: " + str(avg_grades))

total = sum(grades)
print("Total of grades: " + str(total))
print("Average of grades: " + str(avg_grades))

###########################################################################

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in elements :
    print("Hello World!")

for index in range(10) :
    print(index)

for index in range(5, 10, 4) :
    print(index)

##########################################################################################

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Jen", "grade": 95},
    {"name": "Charlie", "grade": 80},
    {"name": "Anne", "grade": 85},
]

for student in students :
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has grade of {grade}")

#############################################################################

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 85}

for student, attendance in student_attendance.items():
    print(f"{student} has attendance of {attendance} percentage.")

for name in student_attendance:
    print(name)

for attendance in student_attendance.values():
    print(attendance)

#########################################################################################

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lectures")]

for name, age, profession in people:
    print(f"Name : {name}, Age: {age}, Profession: {profession}")

for name in student_attendance :
    print(name)

for attendance in student_attendance.values():
    print(attendance)

#######################################################################################

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
# using break keyword - breaks the loop
for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        break
    print(f"This car is {status}")
    print("Shipping new car to customer.")
else:
    print("All cars built successfully. No faulty cars!")

###########################################################################################

# using continue keyword - skips the current loop and continues to the next one
for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue
    print(f"This car is {status}")
    print("Shipping new car to customer.")

##########################################################################################

for x in range(1,101):
    print(x)

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

########################################################################################
# printing prime numbers from 1 to 10

for n in range(2, 10) :
    for x in range(2, n):
        if n % 2 == 0 :
            print(f"{n} equals {x} * {n//x}")
            break
    else :
        print(f"{n} is a prime number.")