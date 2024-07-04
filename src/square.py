from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Square Side should be positive value")
        super().__init__(side, side)
