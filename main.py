import math

def quadratic_solver(a, b, c):
    
    discriminant = b**2 - 4*a*c

    
    if discriminant < 0:
        return "Корені відсутні в множині дійсних чисел"
    elif discriminant == 0:
       
        root = -b / (2*a)
        return (root,)
    else:
       
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
