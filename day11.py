import sys

d = {}
for i, l in enumerate(sys.stdin):
	for j, ch in enumerate(l):
		d[i,j] = int(ch == 'L')

#Part 1
p1 = d.copy()
new = {0:0}
delta = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
while new:
	new.clear()
	for (i,j), v in p1.items():
		two_c = v and sum(p1.get((i+di, j+dj), 0) == 2 for di,dj in delta)

		if v == 1 and two_c == 0:
			new[i,j] = 2
		if v == 2 and two_c >= 4:
			new[i,j] = 1
	
	p1.update(new)

print([*p1.values()].count(2))

#Part 2
p2 = d.copy()
new = {0:0}
while new:
	new.clear()
	for (i,j), v in p2.items():
		if not v: continue
		
		ci,cj = i,j

		two_c = 0
		for di,dj in delta:
			i,j = ci,cj
			while (i+di, j+dj) in p2 and not (p2[i+di,j+dj] % 2):
				if p2[i+di, j+dj] == 2:
					two_c += 1
					break
				i += di
				j += dj

		if v == 1 and two_c == 0:
			new[ci,cj] = 2
		if v == 2 and two_c >= 5:
			new[ci,cj] = 1

	p2.update(new)
	
print([*p2.values()].count(2))
