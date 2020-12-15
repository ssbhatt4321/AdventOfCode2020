import sys

d = sorted([*map(int, sys.stdin)])

#Part 1
order = [0, *d, max(d) + 3]
diff = [order[i+1] - order[i] for i in range(len(order)-1)]
print(diff.count(1) * diff.count(3))

#Part 2
vals = {}
def dfs(end):
	if end in vals:
		return vals[end]
	if end <= 0:
		return end == 0
	if end not in d:
		return 0
	
	vals[end] = sum(dfs(end - i) for i in (1,2,3))
	return vals[end]

print(dfs(d[-1]))