print("GEO CALCULATION\n1.TRIANGLE\n2.RECTANGLE\n3.CIRCLE\n4.EXIT")
choice=int(input("enter your choice\n"))
match choice:
    case 1:
        print("Triangle case executed!!")
        print("1.Area\n2.side\n3.exit")
        ip=int(input("enter your choice\n"))
        match ip:
            case 1:
                print("area of triangle is :")
            case 2:
                print("side of square is:")
            case 3: 
                print("exit from triangle")
            case _ :
                print("invalid choice for triangle opreation")

    case 2:
        print("Rectangle case executed!!")
        print("1.Area\n2.perimeter\n3.exit")
        ip=int(input("enter your choice\n"))
        if ip==1:
            print("area of rectangle is")
            #l*b
            len=int(input("enter length\n"))
            bre=int(input("enter breadth\n"))
            area=len*bre
            print("area of rectangle is",area)
        elif ip==2:
           print("perimeter of rectangle is")
        elif ip==3:
           print("exit from rectangle")
           
    case 3:
        print("Cicle case executed!!")
        print("1.Area\n2.Diameter\n3.Radius\n4.exit")
        ip=int(input("enter your choice\n"))
        if ip==1:
          print("area of circle is:")
          #pi*r*r
          r=int(input("enter radius\n"))
          area=3.14*r*r
          print("area of circle is:",area)
        elif ip==2:
              print("diameter of circle is:")

              r=int(input("enter radius\n"))
              diameter=2*r
              print("diameter of circle is:",diameter)
        elif ip==3:
            print("radius of circle is:")
            r=int(input("enter radius\n"))
            print("radius of circle is:",r)
    case 4:
        print("exit")