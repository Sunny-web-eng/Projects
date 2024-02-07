from collections import defaultdict
from common import sub_fac_data, students_data

failed_students = set()
for roll_no, data in students_data.items():
    for sub_id, marks in data["marks"].items():
        if marks < 35:
            failed_students.add(roll_no)

failed_subs = defaultdict(list)

stu_totals = []


for roll_no, data in students_data.items():
    if roll_no not in failed_students:
        stu_totals.append((roll_no, sum(data["marks"].values())))

roll_no, total_marks = max(stu_totals, key=lambda x: x[1])

print(
    f"student with max marks is {roll_no}: {students_data[roll_no]['name']} - {total_marks}"
)
