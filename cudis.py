import sys
import pandas as pd
import threading

def getAddrIdx(data, arr):
	for i in arr:
		if i[0] == data:
			return arr.index(i)
	return -1

def worker(wid, arr, count, res):
	start = int(wid * count)
	offset = 0
	while offset < count:
		entry = arr[start + offset].split(" ")
		hexaddr = entry[1]
		addr = int(hexaddr, base=16)
		i = getAddrIdx(hexaddr, res)
		if i > -1:
			res[i][1] += 1
		else:
			res.append([hexaddr, addr, 1])
		offset += 1

if __name__ =="__main__":
	nworkers = 1
	batch = 800000

	if len(sys.argv) < 3:
		print("Too few arguments")
	if len(sys.argv) > 3:
		nworkers = int(sys.argv[3])
		batch = int(batch / nworkers) * nworkers
	if len(sys.argv) > 4:
		batch = int(sys.argv[4])
		batch = int(batch / nworkers) * nworkers

	print("*******************************************")
	print("                  CUDIS")
	print()
	print("\tInput Filename: " + sys.argv[1])
	print("\tOutput Filename: " + sys.argv[2])
	print("\tNum of Worker: " + str(nworkers))
	print("\tBatch Size: " + str(batch))
	print()

	result = list()
	reslist = list()
		
	print(" Open Target File: " + sys.argv[1])
	filein = open(sys.argv[1], "r")

	print(" Map...")
	for i in range(nworkers):
		reslist.append([])

	loop = 1
	linein1 = filein.readlines(batch)
	linein2 = []
	while len(linein1) != 0 or len(linein2) != 0:
		w = list()
		if len(linein1) != 0:
			print("\tLoop" + str(loop) + ": " + str(len(linein1)) + " lines start...")
			batchlen = len(linein1)
			for i in range(nworkers):
				w.append(threading.Thread(target=worker, args=(i, linein1, batchlen/nworkers, reslist[i],)))
			for i in range(nworkers):
				w[i].start()
			linein2 = filein.readlines(batch)
			for i in range(nworkers):
				w[i].join()
			linein1 = []
		else:
			print("\tLoop" + str(loop) + ": " + str(len(linein2)) + " lines start...")
			batchlen = len(linein2)
			for i in range(nworkers):
				w.append(threading.Thread(target=worker, args=(i, linein2, batchlen/nworkers, reslist[i],)))
			for i in range(nworkers):
				w[i].start()
			linein1 = filein.readlines(batch)
			for i in range(nworkers):
				w[i].join()
			linein2 = []
		loop += 1
	filein.close()

	print()
	print(" Reduce...")
	for i in range(nworkers):
		print("\tWorker" + str(i + 1) +"...")
		for entry in reslist[i]:
			hexaddr = entry[0]
			refcnt = entry[2]
			i = getAddrIdx(hexaddr, result)
			if i > -1:
				result[i][2] += refcnt
			else:
				result.append(entry)
	
	print()
	print(" Write Output File: " + sys.argv[2] + "...")
	print("\tConvert to DataFrame...")
	df = pd.DataFrame(result)
	print("\tWrite")
	df.to_csv(sys.argv[2], sep=',')
	print(" Done")
	print()
	print("*******************************************")

