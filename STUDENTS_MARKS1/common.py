import csv

with open('student_marks_data.csv', newline='\n') as f:
    reader = csv.DictReader(f)
    students_data = {}
    for data_dict in reader:
        data_dict['SubjectID'] = int(data_dict['SubjectID'])
        data_dict['Marks'] = int(data_dict['Marks'] )
        roll_no = data_dict['RollNo']

        if roll_no not in students_data:
            students_data[roll_no] = {
                                        'name': data_dict['Name'],
                                        'email': data_dict["Email"],
                                        'marks' : {data_dict['SubjectID']: data_dict['Marks']}}
        else:
            students_data[roll_no]['marks'][data_dict['SubjectID']] = data_dict['Marks']




with open('subject_faculty.csv', newline='\n') as f:
    reader = csv.DictReader(f)
    sub_fac_data = {}
    for data_dict in reader:
        sub_id = int(data_dict['SubjectID'])
        sub_fac_data[sub_id] = {'name': data_dict['SubName'], "faculty_name": data_dict['FacultyName']}


if __name__ == '__maain__':
    print(students_data)
    print(sub_fac_data)