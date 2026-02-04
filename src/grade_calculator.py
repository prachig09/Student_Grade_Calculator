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


def main():
    marks = []
    print("Enter marks for 5 subjects (0–100 only):")

    for i in range(5):
        while True:
            try:
                mark = float(input(f"Subject {i + 1}: "))

                if mark < 0 or mark > 100:
                    print(" Error: Marks must be between 0 and 100")
                    continue

                marks.append(mark)
                break

            except ValueError:
                print(" Error: Please enter a valid number")

    avg = calc_avg(marks)
    result = grade(avg)

    print("\nAverage Marks:", avg)
    print("Grade:", result)


if __name__ == "__main__":
    main()
