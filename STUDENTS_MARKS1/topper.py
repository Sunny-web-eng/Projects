from collections import defaultdict
from common import students_data, sub_fac_data

sub_failed = defaultdict(list)
for roll_no, data in students_data.items():
    for sub_id, marks in data['marks'].items():
        if marks == 100:
            sub_failed[sub_id].append(roll_no)

# subject wise toppers

print("-------------------")
for sub_id, roll_nums in sub_failed.items():
    print(f"{sub_fac_data[sub_id]['name']} ({len(roll_nums)})")
    print("-------------------")
    for roll_no in roll_nums:
        print(students_data[roll_no]['name'])
    print("-------------------")