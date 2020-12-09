import sys

sep = 25
ss = sys.stdin.readlines()

#Part 1
d = [*map(int, ss[:sep])]
i = sep
while True:
	n = int(ss[i])
	if all(n - nn not in d or n - nn == nn for nn in d):
		print(n)
		tar = n
		break
	
	d = d[1:] + [n]
	i += 1

#Part 2
d = [*map(int,ss)]
s = 0
e = 2
t = 0
while t != tar:
	if t < tar:
		e += 1
	elif t > tar:
		s += 1
	t = sum(d[s:e])
print(max(d[s:e]) + min(d[s:e]))
