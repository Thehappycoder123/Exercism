def legit(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a + b >= c and b + c >= a and a + c >= b and a > 0 and b > 0 and c > 0
def equilateral(sides):
    if sides[0] == sides[1] == sides[2]:
        equilateral_test = True
    else:
        equilateral_test = False
    return equilateral_test and legit(sides)

def isosceles(sides):
    if sides[0] == sides[1] == sides[2] or sides[1] == sides[2] or sides[0] == sides[1] or sides[0] == sides[2]:
        isosceles_test = True
    else:
        isosceles_test = False
    return isosceles_test and legit(sides)


def scalene(sides):
    if sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        scalene_test = True
    else:
        scalene_test = False
    return scalene_test and legit(sides)

