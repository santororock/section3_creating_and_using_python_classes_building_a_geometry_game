class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rect):
        if (
            rect.lowleft.x < self.x < rect.upright.x 
            and rect.lowleft.y < self.y < rect.uprright.y
            ):
            return(True)
        else:
            return(False)

    def distance_from_point(self, point):
        dist = ( ((self.x - point.x)**2) + 
                 ((self.y - point.y)**2) ) ** 0.5
        return(dist)


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
