input_file = 'input/students.txt'
output_file = 'Output/output18.txt'
input_user = input('Ism: ')

with open(input_file) as f:
    content = f.readlines()
    content = [name[:-1].lower() for name in content]

result = 'Mavjud'
if input_user.lower() not in content:
    result = 'Mavjud emas'

with open(output_file, 'w') as f:
    f.write(result)