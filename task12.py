input_fayil = 'Input/students.txt'
output_fayil = 'Output/output12.txt'


with open(input_fayil) as f:
    content = f.readline()

    result = len(content)

with open(output_fayil, 'w') as f:
    f.write(str(result))