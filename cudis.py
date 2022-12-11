import sys
import pandas as pd

print(sys.argv)
dis = dict()

df = pd.read_csv(sys.argv[1], sep=' ', names=['idx', 'paddr', 'vaddr']);

for i in df['paddr']:
	if dis.get(i) == None:
		dis[i] = 0
	else:
		dis[i] = dis[i] + 1

df = pd.DataFrame([dis])
df.to_csv(sys.argv[2], sep=',')
