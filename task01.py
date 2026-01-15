input_file = 'Input/numbers.txt'
input_file_obj = open(input_file)
content = input_file_obj.read()


numbers = content.split()

result = numbers
output_file = 'Output/output1.txt'
output_file_obj = open(output_file, 'w')
output_file_obj.write(str(result))