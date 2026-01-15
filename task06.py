path_input = "input/numbers.txt"
path_output = "output/output06.txt"

with open(path_input) as input_file :
    numbers = input_file.readlines()
    nums = list(filter(lambda x: x % 2 != 0, map(lambda x: int(x), numbers)))


with open(path_output, "w") as output_file :
    odd_nums = map(lambda x: str(x) + "\n", nums)
    output_file.writelines(odd_nums)
    

