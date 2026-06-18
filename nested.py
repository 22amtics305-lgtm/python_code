x=[[10,20],[11.2,12.3],"hi",90]
#print 12.3
print(x)
print(x[1])
print(x[1][1])
print(x[2])

for i in x:
    if type(i)==list: #[]==listt []true
        for j in i:#[10,20] [11.2,12.3]
         print(j)
         continue
        print(i)
print("--------------------")
#student id and marks
x = [[101, "Ram", 98],
    [102, "Sita", 88],
    [103, "Ramu", 78],
    [104, "Gita", 99]]
while True:
    print("SMS\n1.Add\n2.View\n3.Update\n4.Delete\n5.Topper\n6.Exit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            ip=int(input("Hom many student you want to add\n"))
            for i in range(ip):
                id=int(input("Enter your id:\n"))
                name=input("Enter your name:\n")
                marks=input("Enter your marks:\n")
                x.append([id,name,marks])
                print(f"x{i+1} added")
        case 2:
            for i  in x:
                print(i)
        case 3:
             sid = int(input("Enter your id:\n"))
             for i in x:
                 if sid == i[0]:
                     print("1.updated marks\n2.update name\n3.all details\n4.exit")
                     choice=int(input("Enter your choice:"))
                 if choice ==1:
                     ex_marks=i[2]
                     new_marks=int(input("Enter new marks to update:\n"))
                     i[2]=new_marks
                     print(f"{ex_marks}updated to {new_marks}marks")
                 elif choice == 2:
                     ex_name = i[1]
                     new_name = input("Enter new name to update:\n")
                     i[1] = new_name
                     print(f"{ex_name} updated to {new_name}")
                 elif choice == 3:
                     print(f"Current Details -> ID: {i[0]}, Name: {i[1]}, Marks: {i[2]}")
                 elif choice == 4:
                       print("Exit.")
        case 4:
            sid = int(input("Enter your id:\n"))
            for i in x:
                if sid == i[0]:
                     print("1.delete marks\n2.delete name\n3.all details\n4.exit")
                     choice=int(input("Enter your choice:"))
                     elif
        case 5:
            pass
        case 6:
            pass