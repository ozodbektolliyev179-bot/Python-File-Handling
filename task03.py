input_file = 'Input/numbers.txt'
fayil = open(input_file).read().split()

nums = list(map(lambda x: int(x), fayil))
m_max = max(nums)

print(m_max)
