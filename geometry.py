from random import randint

class Point:
    '''point object'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rect):
        if (
            rect.point0.x < self.x < rect.point1.x 
            and rect.point0.y < self.y < rect.point1.y
            ):
            return(True)
        else:
            return(False)

    def distance_from_point(self, point):
        dist = ( ((self.x - point.x)**2) + 
                 ((self.y - point.y)**2) ) ** 0.5
        return(dist)


class Rectangle:
    '''rectangle object'''

    def __init__(self, point0, point1):
        self.point0 = point0
        self.point1 = point1

    def area(self):
        width = self.point1.x - self.point0.x
        height = self.point1.y - self.point0.y
        return(width * height)


# Create rectangle object
rectangle = Rectangle(
                Point(randint(0,9), randint(0,9)),
                Point(randint(10,19),randint(10,19))
                )


# print rectangle coords
print ("Rectangle Coordinates: [{},{}] and [{},{}]".format(
        rectangle.point0.x,
        rectangle.point0.y,
        rectangle.point1.x,
        rectangle.point1.y)
        )


# get user point and area data
user_point = Point(float(input("Guess X: ")),
                   float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))


# print the game result
print("Your point was inside rectangle: {}".format(
        user_point.falls_in_rectangle(rectangle)))
print("Your area was off by: {}".format(rectangle.area() - user_area))