import pandas as pd

dis = dict()

df = pd.read_csv(r'm3_r_app', sep=' ', names=['idx', 'paddr', 'vaddr']);

for i in df['paddr']:
	if dis.get(i) == None:
		dis[i] = 0
	else:
		dis[i] = dis[i] + 1

df = pd.DataFrame([dis])
df.to_csv('dis_m3_r_app.csv', sep=',')
