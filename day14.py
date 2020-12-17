import sys
from collections import defaultdict

def apply_mask1(m, d):
	return int(''.join(b[b[0] == 'X'] for b in zip(m, f'{d:036b}')),2)

def apply_mask2(m, l):
	addr = [''.join(b[b[0] == '0'] for b in zip(m, f'{l:036b}'))]
	for i, c in enumerate(m):
		if c == 'X':
			addr = [add[:i] + d + add[i+1:] for add in addr for d in ('0','1')]
	return map(int, addr)

d1 = defaultdict(int)
d2 = defaultdict(int)
mask = 0
for l in sys.stdin:
	if l.startswith('mask'):
		mask = l[l.index('= ') + len('= '):]
	else:
		loc = int(l[l.index('[') + 1 : l.index(']')])
		val = int(l[l.index('= ') + len('= '):])

		d1[loc] = apply_mask1(mask, val)
		for add in apply_mask2(mask, loc):
			d2[add] = val


print(sum(d1.values()))
print(sum(d2.values()))