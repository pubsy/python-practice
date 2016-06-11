import sys

array = [13, 3, 25, 20, -7, 12, 5, -22, 15, 4, 7, -10, 11]

min = sys.maxint
max = -sys.maxint - 1
for a in array:
    if a <= min:
        min = a
    if a >= max:
        max = a

diff = max - min

posArray = [False] * (diff + 1)

for a in array:
    posArray[a - min] = True

i = 0
while i < len(posArray):
    if posArray[i]:
        print(i + min)
    i += 1