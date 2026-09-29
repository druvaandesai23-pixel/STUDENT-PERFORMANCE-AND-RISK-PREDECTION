import csv
import os

FILE_NAME = "student_data.csv"

# Exam max marks
CAT1_MAX = 50
CAT2_MAX = 50
TERM_MAX = 100

PASS_PERCENT = 40.0
RISK_PERCENT = 50.0


def get_marks(subject_name, max_marks):
    while True:
        try:
            score = float(input(f"Enter {subject_name} marks (out of {max_marks}): "))
            if 0 <= score <= max_marks:
                return score
            print(f"Marks must be between 0 and {max_marks}.")
        except ValueError:
            print("Please enter a valid number.")


def enter_data():
    students = []
    print("\n--- Student Entry ---")
    while True:
        name = input("\nStudent Name (or press Enter to stop): ").strip()
        if not name:
            if students:
                break
            print("Please enter at least one student's data.")
            continue

        cat1 = get_marks("CAT 1", CAT1_MAX)
        cat2 = get_marks("CAT 2", CAT2_MAX)
        term_end = get_marks("Term End", TERM_MAX)

        students.append({
            "name": name,
            "cat1": cat1,
            "cat2": cat2,
            "term_end": term_end
        })
    return students


def save_csv(students):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "CAT1", "CAT2", "TermEnd"])
        for s in students:
            writer.writerow([s["name"], s["cat1"], s["cat2"], s["term_end"]])
    print(f"\nData saved in {FILE_NAME}")


def load_csv():
    if not os.path.exists(FILE_NAME):
        return []

    students = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append({
                    "name": row["Name"],
                    "cat1": float(row["CAT1"]),
                    "cat2": float(row["CAT2"]),
                    "term_end": float(row["TermEnd"])
                })
        return students
    except Exception as e:
        print("Error reading CSV file:", e)
        return []


def process_and_display(students):
    print("\n" + "=" * 45)
    print("RESULTS SUMMARY")
    print("=" * 45)

    passed_count = 0
    correct_pred = 0
    special_cases = []

    for s in students:
        c1_pct = (s["cat1"] / CAT1_MAX) * 100
        c2_pct = (s["cat2"] / CAT2_MAX) * 100
        term_pct = (s["term_end"] / TERM_MAX) * 100
        cat_avg = (c1_pct + c2_pct) / 2
        total_pct = ((s["cat1"] + s["cat2"] + s["term_end"]) / (CAT1_MAX + CAT2_MAX + TERM_MAX)) * 100

        # Pass conditions
        passed = c1_pct >= PASS_PERCENT and c2_pct >= PASS_PERCENT and term_pct >= PASS_PERCENT
        predicted_pass = cat_avg >= RISK_PERCENT

        if passed:
            passed_count += 1

        # Accuracy calculation
        if (predicted_pass and term_pct >= PASS_PERCENT) or (not predicted_pass and term_pct < PASS_PERCENT):
            correct_pred += 1

        # Passed CATs but failed Term End
        if c1_pct >= PASS_PERCENT and c2_pct >= PASS_PERCENT and term_pct < PASS_PERCENT:
            special_cases.append((s["name"], cat_avg, term_pct))

        print(f"\nName: {s['name']}")
        print(f"  CAT1: {c1_pct:.1f}% | CAT2: {c2_pct:.1f}% | CAT Avg: {cat_avg:.1f}%")
        print(f"  Term End: {term_pct:.1f}% | Total: {total_pct:.1f}%")
        print(f"  Status: {'PASS' if passed else 'FAIL'} | Risk Prediction: {'PASS' if predicted_pass else 'FAIL'}")

    total = len(students)
    print("\n" + "=" * 45)
    print(f"Total Students: {total}")
    print(f"Passed: {passed_count} | Failed: {total - passed_count}")
    print(f"Prediction Accuracy: {(correct_pred / total) * 100:.1f}%")

    if special_cases:
        print("\nPassed CATs but failed Term End:")
        for name, avg, term in special_cases:
            print(f" - {name} (CAT Avg: {avg:.1f}%, Term End: {term:.1f}%)")


def main():
    students = []
    if os.path.exists(FILE_NAME):
        choice = input("Previous data found. Load it? (y/n): ").strip().lower()
        if choice == 'y':
            students = load_csv()

    if not students:
        students = enter_data()
        save_csv(students)

    process_and_display(students)


if __name__ == "__main__":
    main()
