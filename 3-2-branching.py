side1=int(input())
side2=int(input())
side3=int(input())

check1=(side1+side2)>side3
check2=(side2+side3)>side1
check3=(side1+side3)>side2

if((check1 and check2 )and check3):
    if((side1==side2) and (side2==side3)):
        print("equilateral")
    elif(side1==side2 or side2==side3 or side1==side3):
      print("isosceles")
    else:
        print("scalene")

else:
    print("impossible")
