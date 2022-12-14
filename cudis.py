import sys
import pandas as pd

def find(data, arr):
	for i in arr:
		if i[0] == data:
			return arr.index(i)
	return -1

print(sys.argv)
dis = list()

print("Open the target file")
filein = open(sys.argv[1], "r")

print("Run")
linein = filein.readline()
while linein:
	entry = linein.split(" ")
	addr = int(entry[1], base=16)

	idx = find(addr, dis)
	if idx > -1:
		dis[idx][1] += 1
	else:
		dis.append([addr, 1])

	linein = filein.readline()
filein.close()

'''
for addr in df['paddr']:
	idx = find(addr, dis)
	if idx > -1:
		dis[idx][1] += 1
	else:
		dis.append([i, 1])
'''

print("Done")
df = pd.DataFrame(dis)
df.to_csv(sys.argv[2], sep=',')
