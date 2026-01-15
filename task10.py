input_fayil = 'Input/numbers.txt'
output_fayil = 'Output/output10.txt'

with open(input_fayil) as f:
    content = f.readlines()

result = sorted(
    content,
    key= lambda num: int(num)
                    
)
result = ''.join(result)
with open(output_fayil, 'w') as f:
    f.write(result)