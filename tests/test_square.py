import pytest

from src.square import Square
from src.rectangle import Rectangle
from src.triangle import Triangle
from src.circle import Circle


@pytest.mark.parametrize(
    ("side", "perimeter"),
    [(4, 16), (1.6, 6.4)],
    ids=["Perimeter integer", "Perimeter float"],
)
def test_square_perimeter_parameters(side, perimeter):
    squar = Square(side)
    assert squar.get_perimeter() == perimeter


@pytest.mark.parametrize(
    ("side", "area"), [(5, 25), (4.4, 19.36)], ids=["Area integer", "Area float"]
)
def test_square_area_parameters(side, area):
    squar = Square(side)
    assert squar.get_area() == pytest.approx(area, 0.001)


@pytest.mark.parametrize("side", [0, -2], ids=["Zero value", "Negative value"])
def test_square_invalid_parameters(side):
    with pytest.raises(ValueError):
        Square(side)


def test_invalid_other_figure():
    with pytest.raises(ValueError):
        Square(4).add_area(5)


def test_add_area_of_other_figure():
    squar = Square(4)
    assert squar.add_area(Rectangle(3, 4)) == 28
    assert squar.add_area(Triangle(3, 4, 5)) == 22
    assert squar.add_area(Circle(2)) == pytest.approx(28.566, 0.001)
