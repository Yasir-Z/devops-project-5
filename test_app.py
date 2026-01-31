import pytest
from app import add_numbers


def test_add_numbers_success():
    """Test that valid integers return the correct sum."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0


def test_add_numbers_type_error():
    """Test that non-integers raise a TypeError."""
    with pytest.raises(TypeError):
        add_numbers("1", 2)  # type: ignore
