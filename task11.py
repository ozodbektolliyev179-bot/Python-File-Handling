input_fayil = 'Input/students.txt'
output_fayil = 'Output/output11.txt'


with open(input_fayil) as f:
    content = f.read()

with open(output_fayil, 'w') as f:
    f.write(content)