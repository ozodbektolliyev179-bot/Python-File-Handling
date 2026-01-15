fay_input = 'Input/numbers.txt'
input_file = open(fay_input).read().split()

nams = list(map(lambda x: int(x), input_file))

average = sum(nams) / len(nams)
print(average)