import sys
from collections import defaultdict

outer_bags = defaultdict(list)
inner_bags = defaultdict(list)

for l in sys.stdin:
	if " no " not in l:
		target, inner = l.split(" bags contain ")
		inner = inner.split(', ')
		
		
		#Part 1	
		for bag in inner:
			color = ' '.join(bag.split()[1:-1])
			outer_bags[color].append(target)
	
		#Part 2
		inner_bags[target] = [bag[:bag.rfind(' ')].split(' ', 1) for bag in inner]


#Part 1
vis = set()
l = ['shiny gold']
while l:
	a = l.pop()
	if a in vis:
		continue
	vis.add(a)

	l.extend(outer_bags[a])
print(len(vis) - 1)

#Part 2
vals = defaultdict(int)
def val(b):
	vals[b] = vals[b] or sum(int(num) * (val(col) + 1) for num, col in inner_bags[b])
	return vals[b]
print(val('shiny gold'))
