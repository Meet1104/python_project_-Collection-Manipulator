students = []

while True:
    print("\nWelcome to the Student Data Organizer!")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case '1': 
            print("\nEnter student details:")
            student_id = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ").split(",")

            student = {
                "id": student_id,
                "name": name,
                "age": age,
                "grade": grade,
                "dob": dob,
                "subjects": [s.strip() for s in subjects]
            }

            students.append(student)
            print("\nStudent added successfully!")

        case '2':   
            if not students:
                print("\nNo students found.")
            else:
                print("\n--- Display All Students ---")
                for s in students:
                    print(f"Student ID: {s['id']} | Name: {s['name']} | "
                          f"Age: {s['age']} | Grade: {s['grade']} | "
                          f"Subjects: {', '.join(s['subjects'])}")

        case '3':   
            sid = int(input("\nEnter Student ID to update: "))
            found = False

            for s in students:
                if s['id'] == sid:
                    s['name'] = input("New Name: ")
                    s['age'] = int(input("New Age: "))
                    s['grade'] = input("New Grade: ")
                    s['dob'] = input("New Date of Birth (YYYY-MM-DD): ")
                    s['subjects'] = input("New Subjects (comma-separated): ").split(",")
                    s['subjects'] = [sub.strip() for sub in s['subjects']]
                    print("\nStudent information updated successfully!")
                    found = True
                    break

            if not found:
                print("\nStudent not found.")

        case '4':  
            sid = int(input("\nEnter Student ID to delete: "))
            found = False

            for s in students:
                if s['id'] == sid:
                    students.remove(s)
                    print("\nStudent deleted successfully!")
                    found = True
                    break

            if not found:
                print("\nStudent not found.")

        case '5':   
            subject_set = set()

            for s in students:
                subject_set.update(s['subjects'])

            if subject_set:
                print("\nSubjects Offered:")
                for sub in subject_set:
                    print("-", sub)
            else:
                print("\nNo subjects available.")

        case '6':  
            print("\nThank you for using the Student Data Organizer!")
            break

        case _:
            print("\nInvalid choice. Please try again.")
