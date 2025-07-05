print("Welcome to the  Student Data Oraganizer! ")

all_students = []

while True:
    print("Select an option: ")
    print("1. add a student")
    print("2. Display All student")
    print("3. Update student Information")
    print("4. Delete student")
    print("5. Display Subject offered")
    print("6. exit")

    choice = int(input("Enter your choice : "))

    match choice :
        case 1 : 
            print("Enter a student detail : ")
            id = int(input("Enter student ID : "))
            name = (input("Enter student name : "))
            age = int(input("Enter your age : "))
            grade = (input("Enter student grade : "))

            student = {"id": id, "name": name, "age": age, "grade": grade}
            all_students.append(student)

            print("Student added successfully!")

        case 2 :
            print("All Students: ")
            for stu in all_students:
                print(stu)
        case 3 :
            update_id = int(input("Enter a student ID : "))
            for stu in all_students:
                if stu["id"] == update_id:
                    print("Student found:", stu)
                    stu["name"] = input("Enter new name: ")
                    stu["age"] = int(input("Enter new age: "))
                    stu["grade"] = input("Enter new grade : ")
                    print("Student updated successfully!")
                    break
        case 4 :
            delete_id = int(input("Enter a student ID : "))
            for bye in all_students:
                if bye["id"] == delete_id:
                    print("Student found:", bye)
                    all_students.remove(bye)
                    print("Student deleted successfully!")
                    break
        case 5 :
            print("Subject offered : ")
        case 6 :
            print("exit")
            break
        case _ :
            print("Invalid") 