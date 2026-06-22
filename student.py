students = []

while True:

    print("\n1.Add Student")
    print("2.View Students")
    print("3.Total & Percentage")
    print("4.Subject Topper")
    print("5.Subject Lowest")
    print("6.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter Name: ")
        java = int(input("Enter Java Marks: "))
        python = int(input("Enter Python Marks: "))
        eng = int(input("Enter English Marks: "))

        students.append([name, java, python, eng])

        print("Student Added Successfully")

    elif choice == 2:

        print("\nStudent Details")

        for i in students:
            print(i)

    elif choice == 3:

        print("\nTotal and Percentage")

        for i in students:

            total = i[1] + i[2] + i[3]
            per = total / 3

            print(f"Name: {i[0]}")
            print(f"Total: {total}")
            print(f"Percentage: {per:.2f}")
            print()

    elif choice == 4:

        java_top = max(students, key=lambda x: x[1])
        py_top = max(students, key=lambda x: x[2])
        eng_top = max(students, key=lambda x: x[3])

        print("\nTopper Students")
        print("Java Topper:", java_top[0], java_top[1])
        print("Python Topper:", py_top[0], py_top[2])
        print("English Topper:", eng_top[0], eng_top[3])

    elif choice == 5:

        java_low = min(students, key=lambda x: x[1])
        py_low = min(students, key=lambda x: x[2])
        eng_low = min(students, key=lambda x: x[3])

        print("\nLowest Students")
        print("Java Lowest:", java_low[0], java_low[1])
        print("Python Lowest:", py_low[0], py_low[2])
        print("English Lowest:", eng_low[0], eng_low[3])

    elif choice == 6:

        print("Thank You")
        break

    else:
        print("Invalid Choice")

