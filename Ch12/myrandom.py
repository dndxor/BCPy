from random import *

def random_color() :
    r = random()
    g = random()
    b = random()
    return (r, g, b)

def random_xy() :
    x = randint(-500, 500)
    y = randint(-400, 300)
    return (x, y)

def random_radius() :
    return(randint(80, 130))
