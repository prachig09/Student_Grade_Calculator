def calc_avg(marks):
    return sum(marks) / len(marks)


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


marks = [80, 85, 78, 90, 88]

avg = calc_avg(marks)
final_grade = grade(avg) 

print("Average:", avg)
print("Grade:", final_grade)
