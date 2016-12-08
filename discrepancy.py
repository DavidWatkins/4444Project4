from itertools import chain, combinations, islice
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result    
    for elem in it:
        result = result[1:] + (elem,)
        yield result

# p = powerset([0.07, 0.08, 0.09, 0.1, 0.21, 0.44])
# p = powerset([0.32, 0.17, 0.16, 0.08, 0.13, 0.11])
# p = powerset([0.13, 0.14, 0.19, 0.2, 0.21, 0.13])
# p = powerset([0.03, 0.13, 0.11, 0.15, 0.24, 0.34])
d = 0.02/5
p = powerset([0.02, 0.064+d, 0.124+d, 0.184+d, 0.24+d, 0.348+d])
totals = []

for e in p:
	totals.append(sum(e))


max_diff = 0
max_pair = 0
totals.sort()
for pair in window(totals):
	if abs(pair[1] - pair[0]) > max_diff:
		print(pair)
		max_diff = abs(pair[1] - pair[0])
		max_pair = pair

print(max_diff/2, max_pair)