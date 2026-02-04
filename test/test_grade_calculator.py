import pytest


from grade_calculator import calc_avg, grade


def test_calc_avg():
    marks = [80, 90, 70, 85, 75]
    assert calc_avg(marks) == 80


def test_average_requires_five_subjects():
    with pytest.raises(ValueError):
        calc_avg([80, 90, 70])


@pytest.mark.parametrize(
    "average, expected_grade",
    [
        (95, "A+"),
        (90, "A+"),
        (80, "A"),
        (75, "A"),
        (65, "B"),
        (60, "B"),
        (55, "C"),
        (50, "C"),
        (45, "Fail"),
        (30, "Fail"),
    ],
)
def test_grade(average, expected_grade):
    assert grade(average) == expected_grade
