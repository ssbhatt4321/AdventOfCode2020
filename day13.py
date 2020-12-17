import sys

#https://stackoverflow.com/a/59505761
def linear_congruence(a, b, m):
	if b == 0:
		return 0

	if a < 0:
		a = -a
		b = -b

	b %= m
	a = a%m or m

	return (m * linear_congruence(m, -b, a) + b) // a

ss = sys.stdin.readlines()
t = int(ss[0])
ts = [(i, int(n)) for i,n in enumerate(ss[1].split(',')) if n != 'x']

#Part 1
ans = min((n - t%n, n) for _, n in ts)
print(ans[0] * ans[1])

#Part 2
for i,(ind, n) in enumerate(ts):
	ts[i] = (-ind, n)

while len(ts) > 1:
	r1, m1 = ts.pop()
	r2, m2 = ts.pop()

	x1 = linear_congruence(m1,1,m2)
	x2 = linear_congruence(m2,1,m1)
	
	t = (r2*m1*x1 + r1*m2*x2) % (m1*m2)
	ts.append((t, m1*m2))
print(ts[0][0])