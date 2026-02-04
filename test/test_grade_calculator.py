import pytest
from src.grade_calculator import calc_avg, grade


def test_calc_avg_valid_input():
    marks = [80, 90, 70, 85, 75]
    assert calc_avg(marks) == 80


def test_calc_avg_all_high_marks():
    marks = [90, 95, 92, 88, 91]
    assert calc_avg(marks) == 91.2


def test_calc_avg_invalid_number_of_subjects():
    with pytest.raises(ValueError):
        calc_avg([80, 90, 70])


def test_grade_A_plus():
    assert grade(95) == "A+"


def test_grade_A():
    assert grade(78) == "A"


def test_grade_B():
    assert grade(65) == "B"


def test_grade_C():
    assert grade(52) == "C"


def test_grade_Fail():
    assert grade(40) == "Fail"
