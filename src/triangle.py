from src.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Side of triangle can't be negative")
        if (
            side_a >= (side_b + side_c)
            or side_b >= (side_a + side_c)
            or side_c >= (side_a + side_b)
        ):
            raise ValueError("Such triangle can't exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        half_perimeter = self.get_perimeter() / 2.0
        return math.sqrt(
            half_perimeter
            * (half_perimeter - self.side_a)
            * (half_perimeter - self.side_b)
            * (half_perimeter - self.side_c)
        )
