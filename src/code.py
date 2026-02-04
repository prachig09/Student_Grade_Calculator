def calc_avg(marks):
    """
    Calculates average marks from a list of 5 subject marks.
    """
    if len(marks) != 5:
        raise ValueError("Exactly 5 subject marks are required")

    return sum(marks) / 5


def grade(average):
    """
    Returns grade based on average marks.
    """
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"


def main():
    marks = []

    print("Enter marks for 5 subjects:")
    for i in range(5):
        mark = float(input(f"Subject {i + 1}: "))
        marks.append(mark)

    avg = calc_avg(marks)
    grade = grade(avg)

    print(f"\nAverage Marks: {avg:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
