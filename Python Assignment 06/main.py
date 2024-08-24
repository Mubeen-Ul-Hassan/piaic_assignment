def longest_name(list):
    prev_item = len(list[0][1])
    name = list[0][1]
    for item in list:
        if prev_item < len(item[1]):
            prev_item = len(item[1])
            name = item[1]
    return name

def shortest_name(list):
    prev_item = len(list[0][1])
    name = list[0][1]
    for item in list:
        if prev_item > len(item[1]):
            prev_item = len(item[1])
            name = item[1]
    return name

def total_length(list):
    prev_item = 0
    for item in list:
        prev_item += len(item[1])
    return prev_item
    
def manage_student_database():
    students_database = []
    student_id = 1
    while True:
        student_name = str(input("Please enter student name ( or type 'stop' to finsh ): "))
        if student_name == 'stop':
            break
        else:
            if not any(student[1] == student_name for student in students_database):
                student_data = (student_id, student_name)
                students_database.append(student_data)
                student_id += 1
            else:
                print("This name is already in the list.")

    print("\nComplete list of Students (Tuples):")
    print(students_database)

    print("\nList of Students with IDs:")
    for student in students_database:
        print(f"ID: {student[0]}, Name: {student[1]}")

    print(f"\nTotal number of students: {len(students_database)}")
    print(f"Total length of all student name combined: {total_length(students_database)}")
    print(f"The student with the longest name is: {longest_name(students_database)}")   
    print(f"The student with the shortest name is: {shortest_name(students_database)}")


manage_student_database()
