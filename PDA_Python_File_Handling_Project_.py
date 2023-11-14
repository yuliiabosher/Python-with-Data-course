# Section 1
my_list = []
for i in range(1, 11):
    my_list.append(i)
for i in my_list:
    print(i)
while len(my_list) > 0:
    my_list.pop(len(my_list) - 1)
print(my_list)

# Section 2
student_grades = {}
student_grades["Ellie"] = 85
student_grades["Jamie"] = 60
student_grades["Anne"] = 99
names = list(student_grades.keys())
grades = list(student_grades.values())
print(names, grades)
for i in range(0, len(grades)):
    print(f"{names[i]}: {grades[i]}")


def check_grade():
    input_name = input("write a student's name ")
    return student_grades.get(input_name, "the name does not exist")


print(check_grade())


# Section 3
def squares():
    squared_numbers = []
    for i in range(1, 11):
        sq_num = str(i**2)
        squared_numbers.append(sq_num)
    file_path = "squared_numbers.txt"
    f = open(file_path, "w")
    for i in squared_numbers:
        f.writelines(f"\n{i}")
    f.close()
    f = open("squared_numbers.txt", "r")
    print(f.read())


squares()


# Section 4
def to_do_list():
    def add_new_tasks():
        tasks = []
        while True:
            add_task = input("write a new task or type 'e' to exit ")
            if add_task == "e":
                break
            tasks.append(add_task)
        write_file = open("to_do_list.txt", "w")
        num = 0
        for i in tasks:
            num += 1
            write_file.writelines(f"\n{num}.{i}")
        write_file.close()

    def delete_tasks():
        remove_task_number = input("\nwrite a task number you would like to remove \n")
        read_file = open("to_do_list.txt", "r")
        rows = read_file.readlines()
        write_file = open("to_do_list.txt", "w")
        num = 0
        for i in rows:
            num += 1
            if rows.index(i) == int(remove_task_number):
                num -= 1
                continue
            elif rows.index(i) == 0:
                num -= 1
                write_file.writelines(f"\n")
                continue
            write_file.writelines(f"{num}.{i[2:]}")
        write_file.close()
        read_file.close()

    def append_new_tasks():
        read_file = open("to_do_list.txt", "r")
        write_file = open("to_do_list.txt", "a")
        rows = read_file.readlines()
        add_task = input("write a new task or type 'e' to exit ")
        if add_task == "e":
            read_file.close()
            write_file.close()
        else:
            index = len(rows)
            write_file.writelines(f"\n{index}.{add_task}")
            read_file.close()
            write_file.close()

    def display_menu():
        while True:
            print("\nPress 'w' to overwrite task(s)")
            print("Press 'd' to delete a task")
            print("Press 'a' to append a new task to a file")
            print("Press 'e' to exit the program")
            choice = input("\nChoose 'w', 'd', a' or 'e' ")
            if choice == "w":
                add_new_tasks()
            elif choice == "d":
                delete_tasks()
            elif choice == "a":
                append_new_tasks()
            elif choice == "e":
                print("\nExiting the program")
                break
            else:
                print(
                    "\nInvalid choice. Please enter a valid option ('w', 'd', 'a' or 'e').\n"
                )
            print("\nTo do list:")
            read_file = open("to_do_list.txt", "r")
            rows = read_file.readlines()
            for i in rows:
                print(i)
            if rows == ["\n"]:
                print("\nThe file is empty\n")
            read_file.close()

    display_menu()


to_do_list()
