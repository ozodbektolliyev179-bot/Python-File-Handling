input_file = 'Input/numbers.txt'
output_file = 'Output/output07.txt'
with open(input_file) as f:
    content = f.readlines()

result = list(map(
        lambda num: f'{int(num) ** 2}',
        content
))
result = '\n'.join(result)

with open(output_file, 'w') as f:
    f.write(result)
