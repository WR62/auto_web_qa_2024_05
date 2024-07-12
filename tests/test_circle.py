import pytest

from src.circle import Circle


@pytest.mark.parametrize(
    ("radius", "perimeter"),
    [(4, 25.132), (1.6, 10.053)],
    ids=["Perimeter integer", "Perimeter float"],
)
def test_circle_perimeter_parameters(radius, perimeter):
    circ = Circle(radius)
    assert circ.get_perimeter() == pytest.approx(perimeter, 0.001)


@pytest.mark.parametrize(
    ("radius", "area"), [(5, 78.539), (4.4, 60.821)], ids=["Area integer", "Area float"]
)
def test_circle_area_parameters(radius, area):
    circ = Circle(radius)
    assert circ.get_area() == pytest.approx(area, 0.001)


@pytest.mark.parametrize("radius", [0, -2], ids=["Zero value", "Negative value"])
def test_circle_invalid_parameters(radius):
    with pytest.raises(ValueError):
        Circle(radius)
