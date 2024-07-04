from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Sides should be positive values!")
        self.side_a = length
        self.side_b = width

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2
