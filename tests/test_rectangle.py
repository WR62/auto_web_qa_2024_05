import pytest

from src.rectangle import Rectangle


@pytest.mark.parametrize(
    ("side_a", "side_b", "perimeter"),
    [(4, 5, 18), (4.4, 1.6, 12)],
    ids=["Perimeter integer", "Perimeter float"],
)
def test_rectangle_perimeter_parameters(side_a, side_b, perimeter):
    rct = Rectangle(side_a, side_b)
    assert rct.get_perimeter() == perimeter


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [(4, 5, 20), (4.4, 1.6, 7.04)],
    ids=["Area integer", "Area float"],
)
def test_rectangle_area_parameters(side_a, side_b, area):
    rct = Rectangle(side_a, side_b)
    assert rct.get_area() == pytest.approx(area, 0.001)


@pytest.mark.parametrize(
    ("side_a", "side_b"), [(2, 0), (3.4, -2)], ids=["Zero value", "Negative value"]
)
def test_rectangle_invalid_parameters(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
