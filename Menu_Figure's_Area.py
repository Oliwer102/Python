import math

#figure space

def rectangleArea(a,b):
    if (a <= 0):
        return "Rectangle cannot have side length <= 0"

    if (b <= 0):
        return "Rectangle cannot have side length <= 0"
    return a * b

def squareArea(a):
    if ( a <= 0):
        return "Square cannot have side length <= 0"

    return a * a

def triangleArea(a ,h):
    if (a <= 0):
        return "The base of the triangle cannot be <= 0"

    if (h <= 0):
        return "triangle's height cannot be <= 0"

    return (a * h) / 2

def trapezeArea(a , b , h):
    if (a <= 0):
        return "The base of the trapeze cannot be <= 0"

    if (b <= 0):
        return "The base of the trapeze cannot be <= 0"

    if (h <= 0):
        return "Trapeze's height cannot be <= 0"

    return ((a + b) * h) / 2

def circleArea(r):
    if (r <= 0):
        return "Circle's radius cannot be <= 0"

    return math.pi * r * r

print("Welcome, Choose your program.")
print("1: Rectangle area."
      "\n2: Square area."
      "\n3: Triangle area."
      "\n4: Trapeze area."
      "\n5: Circle area.")

choise = input("Chose one.")

if (choise == "1"):
    print("Rectangle need two arguments a and b.")
    print("Rectangle area = ", rectangleArea(int(input("Write first argument:")), (int(input("Write second argument:")))))

elif (choise == "2"):
    print("Square need one argument.")
    print("Square area = ", squareArea(int(input("Write your argument:"))))

elif (choise == "3"):
    print("Triangle need two argument a and h.")
    print("Triangle area = ",
          triangleArea(int(input("Write base length."))
          , int(input("Write height's length"))))

elif (choise == "4"):
    print("Trapeze need three arguments.")
    print("Trapeze area = ",
          trapezeArea(int(input("Write first base length")),
                      int(input("Write second base length")),
                      int(input("write hight's length"))))

elif (choise == "5"):
    print("Circle area need one argument")
    print("Circle area = ",
          squareArea(int(input("Write radius's length."))))
