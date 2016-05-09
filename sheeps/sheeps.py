from sets import Set

__file_name = 'A-small-practice'

input = open(__file_name + '.in', 'r').read().splitlines()
input.pop(0)  # removing first element of array containing number of input lines

output = open(__file_name + '.out', 'w')

def split_by_digits(i_num):
    digits = []
    loop_again = i_num / 10.0 > 0
    while loop_again:
        loop_again = i_num / 10 > 0
        digits.append(i_num % 10)
        i_num = i_num / 10
    return digits

case = 0
for line in input:
    num_set = Set([])
    i = 1
    num = int(line)
    if num == 0:
        output.write("Case #" + str(case) + ": INSOMNIA\n")
        continue
    while len(num_set) < 10:
        digits = split_by_digits(num * i)
        for digit in digits:
            num_set.add(digit)
        i += 1
    case += 1
    output.write("Case #" + str(case) + ": " + str(num * (i - 1)) + '\n')

