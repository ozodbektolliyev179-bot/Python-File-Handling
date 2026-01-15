input_fayil = 'Input/numbers.txt'
output_fayil = 'Output/output09.txt'

with open(input_fayil) as f:
    content = f.readlines()

result = list(filter(   
    lambda num: f'{len(num)}',
    content
))
result = '\n'.join(result)

with open(output_fayil, 'w') as f:
    f.write(result)