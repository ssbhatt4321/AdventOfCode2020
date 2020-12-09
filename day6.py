import sys

union_cnt = 0
intersect_cnt = 0
ls = []
for l in sys.stdin.readlines() + ['\n']:
	if l == '\n':
		union = set(ls[0]).union(*ls)
		union_cnt += len(union)

		intersect = set(ls[0]).intersection(*ls)
		intersect_cnt += len(intersect)

		ls.clear()
	else:
		ls.append(l[:-1])

print(union_cnt)
print(intersect_cnt)
