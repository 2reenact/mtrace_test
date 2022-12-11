import sys
import pandas as pd

def find(data, arr):
	for i in arr:
		if i[0] == data:
			return arr.index(i)
	return -1

print(sys.argv)
dis = list()

df = pd.read_csv(sys.argv[1], sep=' ', names=['idx', 'paddr', 'vaddr']);

for i in df['paddr']:
	idx = find(i, dis)
	if idx > -1:
		dis[idx][1] += 1
	else:
		dis.append([i, 1])

df = pd.DataFrame(dis)
df.to_csv(sys.argv[2], sep=',')
