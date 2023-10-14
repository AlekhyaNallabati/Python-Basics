"""
First class functions are the functions which we can assign to variables, and we can pass them in as arguments to other functions
"""
avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {             # assigning functions as a values
    "average": avg,
    "total": total,
    "top": top
}

students = [
    {"name": "Rolf", "grades": {90, 80, 75, 85, 76}},
    {"name": "Jen", "grades": {95, 87, 89, 78, 79}},
    {"name": "Charlie", "grades": {80, 65, 67, 75, 80}},
    {"name": "Anne", "grades": {85, 65, 85, 96, 80}},
]

for student in students:
    name = student["name"]
    grades = student["grades"]
    print(f"Student : {name}")
    operation = input("Enter 'average', 'total' or 'top' : ")
    Operation_function = operations[operation]
    print(Operation_function(grades))

