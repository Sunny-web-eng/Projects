from collections import defaultdict
from common import students_data, sub_fac_data

sub_failed = defaultdict(list)
for roll_no, data in students_data.items():
    for sub_id, marks in data['marks'].items():
        if marks < 35:
            sub_failed[sub_id].append(roll_no)

# print(sub_failed)
s_id = int(input("Enter subject ID [1-5]:"))

print("-------------------")
for sub_id, roll_nums in sub_failed.items():
    print(f"{sub_fac_data[sub_id]['name']} ({len(roll_nums)})")
    print("-------------------")
    for roll_no in roll_nums:
        print(students_data[roll_no]['name'])
    print("-------------------")


