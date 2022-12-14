import sys
import pandas as pd
import threading
import os.path

def getAddrIdx(data, arr):
	for i in arr:
		if i[0] == data:
			return arr.index(i)
	return -1

'''
def incRefAddr(addr, arr, entry):
	arrlen = len(arr)
	i = int(arrlen / 2)
	while arr[i][0] != addr:
'''		

def worker(wid, arr, count, res):
	start = int(wid * count)
	offset = 0
	while offset < count:
		entry = arr[start + offset].split(" ")
		offset += 1
		if opc >= 0 and entry[0] != opc:
			continue
		hexaddr = entry[1]
		addr = int(hexaddr, base=16)
		i = getAddrIdx(hexaddr, res)
		if i > -1:
			res[i][1] += 1
		else:
			res.append([hexaddr, addr, 1])

def convert_bytes(size):
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if size < 1024.0:
			return "%d %s" % (int(size), x)
		size /= 1024.0

def str2size(sizestr):
	batch = 1
	strlen = len(sizestr)
	lastchar = sizestr[strlen-1]

	if lastchar == 'K' or lastchar == "k":
		batch = 1024
	elif lastchar == 'M' or lastchar == "m":
		batch = 1024 * 1024
	elif lastchar == 'G' or lastchar == "g":
		batch = 1024 * 1024 * 1024

	if strlen == 2:
		batch = int(sizestr[0]) * batch
	else:
		batch = int(sizestr[0:strlen-1]) * batch

	return batch
		

if __name__ =="__main__":
	nworkers = 1
	batch = 800000
	opc = -1

	if len(sys.argv) < 3:
		print("Too few arguments")
	if len(sys.argv) > 3:
		nworkers = int(sys.argv[3])
		batch = int(batch / nworkers) * nworkers
	if len(sys.argv) > 4:
		batch = str2size(sys.argv[4])
		batch = int(batch / nworkers) * nworkers
	if len(sys.argv) > 5:
		opc = int(sys.argv[5])

	filesize = os.path.getsize(sys.argv[1])
	numbatch = int(filesize / batch)
	filesize = convert_bytes(filesize)

	print("****************************************")
	print("                CUDIS")
	print()
	print("\tInput Filename: " + sys.argv[1])
	print("\tOutput Filename: " + sys.argv[2])
	print("\tNum of Workers: " + str(nworkers))
	print("\tBatch Size: " + convert_bytes(batch))
	if opc == 0:
		print("\tCumulate Reads")
	elif opc == 1:
		print("\tCumulate Writes")
	elif opc == 2:
		print("\tCumulate Instructions")
	else:
		print("\tCumulate Write Trace")
	print()
	print("\tFilesize: " + filesize)
	print("\tNum of Batches: " + str(numbatch))
	print()

	result = list()
	reslist = list()
		
	print(" Open Target File: " + sys.argv[1])
	filein = open(sys.argv[1], "r")

	print(" Map...")
	for i in range(nworkers):
		reslist.append([])

	print("[", end="", flush=True)
	loop = 1
	linein1 = filein.readlines(batch)
	linein2 = []
	while len(linein1) != 0 or len(linein2) != 0:
		if loop % int(numbatch / 38) == 0:
			print("*", end="", flush=True)
		w = list()
		if len(linein1) != 0:
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
	print("]")
	filein.close()

	print()
	print(" Reduce...")
	print("[*", end="", flush=True)
	for i in range(nworkers):
		print("**", end="", flush=True)
		for entry in reslist[i]:
			hexaddr = entry[0]
			refcnt = entry[2]
			i = getAddrIdx(hexaddr, result)
			if i > -1:
				result[i][2] += refcnt
			else:
				result.append(entry)
	print("*]", end="", flush=True)
	
	print()
	print(" Write Output File: " + sys.argv[2] + "...")
	print("\tConvert to DataFrame...")
	df = pd.DataFrame(result)
	print("\tWrite")
	df.to_csv(sys.argv[2], sep=',')
	print(" Done")
	print()
	print("****************************************")

