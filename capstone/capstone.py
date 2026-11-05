def student_activity_counts(records):
    activity_dict = {}
    student_dict = {}

    for record in records:
        student_dict[record[0]] = student_dict.get(record[0], 0)+1
        activity_dict[record[1]] = activity_dict.get(record[1], 0)+1

    return activity_dict, student_dict


def count_student_records(records, student_id):
    count = 0
    if not len(records):
        return 0
    if records[0][0] == student_id:
        count += 1

    return count + count_student_records(records[1:], student_id)


def analyze_records(records):
    activity, student = student_activity_counts(records)

    most_active_student = sorted(
        student.items(), key=lambda x: (-x[1], x[0]))[0][0]

    return student, activity, most_active_student


def main():

    records = [
        ("ST01", "Python"),
        ("ST02", "HTML"),
        ("ST01", "Python"),
        ("ST03", "CSS"),
        ("ST02", "HTML"),
        ("ST01", "JavaScript"),
        ("ST03", "CSS"),
        ("ST01", "Python"),
        ("ST02", "JavaScript"),
        ("ST02", "Python")
    ]

    student, activity, most_active = analyze_records(records)
    print(
        f"student_counts = {student}\nactivity_counts = {activity}\nmost_active_student = {most_active}")
    print(count_student_records(records, "ST01"))
    print(count_student_records(records, "ST02"))
    print(count_student_records(records, "ST99"))
    print(count_student_records([], "ST01"))


if __name__ == "__main__":
    main()
