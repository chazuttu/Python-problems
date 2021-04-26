#Usando el módulo gráfico , escriba un programa recursivo para mostrar una curva de Hilbert.
import turtle
import operator


D = 180
STARTING_POINTS = [(-D,D), (-D,-D), (D,-D), (D,D)]
COLORS = ["yellow", "blue", "purple", "green", "red", "violet"]*2


def main():
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    for level in range(6):
        t.color(COLORS[level])
        t.speed((level+1)*1.8)
        points = make_level_n_points(level+1)
        connect_points(t, points)
    screen.exitonclick()


def make_level_n_points(n):
    if n == 1:
        return STARTING_POINTS
    else:
        points = []
        for sublist in chop_up_to_4s(make_level_n_points(n-1), n-1):
            points = points + make_16_points_outof_4(sublist)
        return points


def chop_up_to_4s(list, n):
   
    sublists = []
    num_sublists = 4**(n-1)
    for i in range(num_sublists):
        sublists.append(list[4*i: 4*i + 4])
    return sublists

def make_16_points_outof_4(four_points):
    
    sixteen_points = []
    for corner in range(1,5):
        sixteen_points = sixteen_points + make_corner_points(four_points, corner)
    return sixteen_points

def make_corner_points(four_points, corner):
    
    center = find_center(four_points)
    smaller_four_points = []
    for point in four_points:
        smaller_four_points.append((i/2.0 for i in tuple(map(operator.add, point, center))))
    shifted_points= []
    shift_direction = tuple(map(operator.sub, four_points[corner-1], center))
    for point in smaller_four_points:
        shifted_points.append(tuple(map(operator.add, shift_direction, point)))
    rotated_points = []
    if corner == 1:
       
        rotated_points.append(shifted_points[0])
        rotated_points.append(shifted_points[3])
        rotated_points.append(shifted_points[2])
        rotated_points.append(shifted_points[1])
    elif corner == 4:
    
        rotated_points.append(shifted_points[2])
        rotated_points.append(shifted_points[1])
        rotated_points.append(shifted_points[0])
        rotated_points.append(shifted_points[3])
    else:
        rotated_points = shifted_points
    return rotated_points

def find_distance(four_points):
    x1 = four_points[0][0]
    y1 = four_points[0][1]
    x2 = four_points[1][0]
    y2 = four_points[1][1]
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def find_center(points):
    center_x = 0
    center_y = 0
    for point in points:
        center_x += point[0]
        center_y += point[1]
    return (center_x/4.0, center_y/4.0)

def connect_points(t, points):
    t.up()
    t.goto(points[0])
    t.down()
    for point in points:
        t.goto(point)


if __name__ == "__main__":
    main()
    
    #programa recursivo para mostrar una curva de Hilbert.