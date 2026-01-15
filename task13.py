input_fayil = 'Input/students.txt'
output_fayil = 'Output/output13.txt'

with open(input_fayil) as f:
    content = f.readlines()


    result = ''.join(sorted(content))

with open(output_fayil, 'w') as f:
    f.write(result)
    