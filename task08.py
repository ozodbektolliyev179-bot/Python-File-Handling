input_file = 'Input/numbers.txt'
output_file = 'Output/output08.txt'

with open(input_file) as f:
    content = f.readlines()

result = list(filter(
    lambda num: int(num) % 5 == 0,
    content
))
result = ''.join(result)

with open(output_file, 'w') as f:
    f.write(result)