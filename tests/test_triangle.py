import pytest

from src.triangle import Triangle


def test_triangle_integer():
    trian = Triangle(3, 4, 5)
    assert trian.get_perimeter() == 12
    assert trian.get_area() == 6.0


def test_triangle_float():
    trng = Triangle(1.5, 2.7, 3.1)
    assert trng.get_perimeter() == pytest.approx(7.3)
    assert trng.get_area() == pytest.approx(2.024, 0.001)


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "perimeter", "area"),
    [(2, 5, 6, 13, 4.683), (3.4, 5.6, 2.7, 11.7, 3.359)],
    ids=["integer", "float"],
)
def test_triangle_parameters(side_a, side_b, side_c, perimeter, area):
    trng = Triangle(side_a, side_b, side_c)
    assert trng.get_perimeter() == perimeter
    assert trng.get_area() == pytest.approx(area, 0.001)


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [(2, 0, 6), (3.4, -2, 2.7)],
    ids=["Zero value", "Negative value"],
)
def test_triangle_negative_parameters(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
