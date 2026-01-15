input_file = 'Input/numbers.txt'
input_file_obj = open(input_file)
content = input_file_obj.read()

numbers = content.split()
numbers = [int(num) for num in numbers] 
result = sum(numbers)
output_file = 'Output/output2.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(result))