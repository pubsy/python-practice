__file_name = 'B-large-practice'

input = open(__file_name + '.in', 'r').read().splitlines()
input.pop(0)  # removing first element of array containing number of input lines

output = open(__file_name + '.out', 'w')

line_num = 1
for line in input:
    if line == '-':
        output.write('Case #' + str(line_num) + ': 1\n')
        line_num += 1
        continue

    if line == '+':
        output.write('Case #' + str(line_num) + ': 0\n')
        line_num += 1
        continue

    count = 0
    for i in range(1, len(line)):
        if line[i] != line[i - 1]:
            count += 1
    if line[len(line) - 1] == '-':
        count += 1
    output.write('Case #' + str(line_num) + ': ' + str(count) + '\n')
    line_num += 1


