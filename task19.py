import csv 

input_fayil = 'Input/grades.csv'
output_fayil = 'Output/output19.txt'

with open(input_fayil) as csv_file:
    reader = csv.DictReader(csv_file, fieldnames=['Name', 'Subject', 'Grade'])
    next(reader)  

    for row in reader:
        print(row)