# create student dictionary list
students = [
  {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
  {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
  {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
]


# function to list student position and name
def list_names(arg1:list):
    for i, student in enumerate(students):
        print(f'{i+1}:', student['name'])


# function to add a new student
def get_new_student() -> dict:
    new_student = {}
    new_student['name'] = input("What is the student's name? ")
    new_student['hometown'] = input("What is the student's home town? ")
    new_student['favorite_food'] = input("What is the student's favorite food? ")
    return new_student


# prompt user to add, view, or quit; keep prompting until quit
do_quit = False
while not do_quit:
    user_action = input(f"Would you like to 'add' a new student, 'view' a student, or 'quit'? ")
    if user_action.lower() == 'add':
        # call function to collect student details, then add to students list
        new_student = get_new_student()
        students.append(new_student)
    elif user_action.lower() == 'view':
        # list students, prompt user to pick one by index/position
        list_names(students)
        picked_student = int(input(f"Which student would you like to view (1-{len(students)})? "))
        student_details = input(f"Would you like to see {students[picked_student-1]['name']}'s hometown ('h') or favorite food ('f')? ")
        if student_details.lower() == 'h':
            print(f"{students[picked_student-1]['name']}'s hometown is {students[picked_student-1]['hometown']}")
        elif student_details.lower() == 'f':
            print(f"{students[picked_student-1]['name']}'s favorite food is {students[picked_student-1]['favorite_food']}")
        else:
            print("that's not a valid option.  Please restart.")
    elif user_action.lower() == 'quit':
        print("OK, good bye!")
        do_quit = True
    else:
        print("That's not a valid option.")
