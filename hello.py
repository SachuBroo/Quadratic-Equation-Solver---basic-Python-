a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

quadratic_equation = f"{a}x^2 + {b}x + {c} = 0"

if a == 0:
    print("The value of a can't be zero!!!")
else:
    determinant = b**2 - 4*a*c

    if determinant > 0:
        root1 = (-b+(determinant**0.5))/(2*a)
        root2 = (-b-(determinant**0.5))/(2*a)
    elif determinant < 0:
        root1 = (-b/(2*a)) + (abs(determinant)**0.5)/(2*a)*1j
        root2 = (-b/(2*a)) - (abs(determinant)**0.5)/(2*a)*1j

    elif determinant == 0:
        root1 = root2 = -b/(2*a)
    else:
        print("Invalid input")

    print(f"The roots of the quadratic equation {quadratic_equation} are: {root1} and {root2}")