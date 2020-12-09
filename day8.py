import sys

d = [l.split() for l in sys.stdin.readlines()]
first_run = True

try:
	for comm in range(len(d)):
		if d[comm][0] in ('nop', 'jmp'):
			#Swap instructions for Part 2
			if not first_run:
				d[comm][0] = ['nop', 'jmp'][d[comm][0] == 'nop']

			i = 0
			t = 0
			vis = set()

			while i not in vis:
				vis.add(i)
				op, off = d[i]

				if op == 'acc':
					t += int(off)

				i += int(off) if op == 'jmp' else 1
			
			#Print acc value for Part 1
			if first_run:
				print(t)
				
			#Unswap instructions for Part 2
			if not first_run:
				d[comm][0] = ['nop', 'jmp'][d[comm][0] == 'nop']
			
			first_run = False
except:
	#Print acc value for Part 2
	#Error raised by out-of-bounds exception on loopless iteration
	print(t)
