import math

def quadratic_solver(a, b, c):
    # Обчислює дискримінант
    discriminant = b**2 - 4*a*c

    # Якщо дискримінант менше 0, корені відсутні у множині дійсних чисел
    if discriminant < 0:
        return "Корені відсутні в множині дійсних чисел"
    elif discriminant == 0:
        # Якщо дискримінант рівний 0, є один корінь
        root = -b / (2*a)
        return (root,)
    else:
        # Якщо дискримінант більше 0, є два корені
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
