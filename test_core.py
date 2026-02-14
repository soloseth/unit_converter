import pytest
from core import convert


def test_kg_to_lb():
    result = convert(1, "kg", "lb")
    assert round(result, 5) == 2.20462


def test_lb_to_kg():
    result = convert(1, "lb", "kg")
    assert round(result, 6) == 0.453592


def test_m_to_ft():
    result = convert(1, "m", "ft")
    assert round(result, 5) == 3.28084


def test_invalid_conversion():
    with pytest.raises(ValueError):
        convert(10, "kg", "ml")
