def calc_avg(marks):
    if len(marks) != 5:
        raise ValueError("Exactly 5 subject marks are required")
    return sum(marks) / 5


def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
