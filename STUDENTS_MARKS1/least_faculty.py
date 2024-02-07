
from collections import defaultdict
from common import sub_fac_data, students_data

sub_failed = defaultdict(list)
for roll_no, data in students_data.items():
    for sub_id, marks in data['marks'].items():
        if marks < 35:
            sub_failed[sub_id].append(roll_no)

# faculty with most number of failures

sub_id = max(sub_failed, key=lambda x: len(sub_failed[x]))
print(f"{sub_fac_data[sub_id]['name']} - { sub_fac_data[sub_id]['faculty_name']}")