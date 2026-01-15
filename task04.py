fay_input = 'input/numbers.txt'
fayil = open(fay_input).read().split()

nams = list(filter(lambda x: int(x) % 2 == 0,map(lambda x: int(x), fayil)))
print(nams)