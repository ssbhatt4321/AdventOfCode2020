import sys
from math import e, pi

pos1 = complex()
dir1 = complex(1)

pos2 = complex()
dir2 = complex(10,1)
for l in sys.stdin:
	c = l[0]
	n = int(l[1:])

	if c == 'N':
		pos1 += -1j * n
		dir2 += 1j * n
	if c == 'S':
		pos1 += 1j * n
		dir2 += -1j * n
	if c == 'E':
		pos1 += 1 * n
		dir2 += 1 * n
	if c == 'W':
		pos1 += -1 * n
		dir2 += -1 * n
	if c == 'L':
		dir1 *= e ** (-n * pi/180 * 1j)
		dir2 *= e ** (n * pi/180 * 1j)
	if c == 'R':
		dir1 *= e ** (n * pi/180 * 1j)
		dir2 *= e ** (-n * pi/180 * 1j)
	if c == 'F':
		pos1 += dir1 * n
		pos2 += dir2 * n

print(round(abs(pos1.real) + abs(pos1.imag)))
print(round(abs(pos2.real) + abs(pos2.imag)))