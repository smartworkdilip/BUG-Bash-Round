from utils import validate_amount
def test_validate_negative_amount():
    assert validate_amount(-10) is False
def test_validate_zero_amount():
    assert validate_amount(0) is False
def test_validate_positive_amount():
    assert validate_amount(100) is True
