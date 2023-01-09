import sys
import pandas as pd
import threading
import os.path
import math

def printProgressBar (iteration, total):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(35 * iteration // total)
    bar = '*' * filledLength + ' ' * (35 - filledLength)
    print(f'\r [{bar}] {percent}%', end = "\r")
    if iteration == total: 
        print()

def worker(wid, arr, offset, count, res):
	i = 0
	while i < count:
		entry = arr[offset + i].split(" ")
		if opc >= 0 and int(entry[0]) != opc:
			i += 1
			continue
		hexaddr = entry[1][0:(len(entry[1])-1)]
		if hexaddr in res:
			res[hexaddr] += 1
		else:
			res[hexaddr] = 1
		i += 1

def convBytes(size):
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if size < 1024.0:
			return "%.1f %s" % (size, x)
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
	else:
		return int(sizestr)

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
	numbatch = int(math.ceil(filesize / batch))
	filesize = convBytes(filesize)

	print("***************************************")
	print("                CUDIS")
	print()
	print("\tInput Filename: " + sys.argv[1])
	print("\tOutput Filename: " + sys.argv[2])
	print("\tNum of Workers: " + str(nworkers))
	print("\tBatch Size: " + convBytes(batch))
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

	dlist = list()
		
	filein = open(sys.argv[1], "r")

	print(" Map...")
	for i in range(nworkers):
		dlist.append(dict())

	loop = 2
	linein1 = filein.readlines(batch)
	linein2 = []
	while len(linein1) != 0 or len(linein2) != 0:
		if loop <= numbatch:
			printProgressBar(loop, numbatch)

		w = []
		if len(linein1) != 0:
			batchlen = len(linein1)
			rest = batchlen % nworkers
			batchlen = int(batchlen / nworkers)
			minibatch = batchlen

			for i in range(nworkers):
				if i == nworkers - 1:
					minibatch += rest
				w.append(threading.Thread(target=worker, args=(i, linein1, i * batchlen,  minibatch, dlist[i],)))
			for i in range(nworkers):
				w[i].start()
			linein2 = filein.readlines(batch)
			for i in range(nworkers):
				w[i].join()
			linein1 = []

		else:
			batchlen = len(linein2)
			rest = batchlen % nworkers
			batchlen = int(batchlen / nworkers)
			minibatch = batchlen

			for i in range(nworkers):
				if i == nworkers - 1:
					minibatch += rest
				w.append(threading.Thread(target=worker, args=(i, linein2, i * batchlen,  minibatch, dlist[i],)))
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
	rdict = dict()
	for i in range(nworkers):
		printProgressBar(i + 1, nworkers)
		rdict.update(dlist[i])

	print()
	print(" Writing out File: " + sys.argv[2])

	result = list()	
	cnt = 0
	total_keys = len(rdict)
	for key in rdict.keys():
		printProgressBar(cnt, total_keys)
		result.append([key, int(key, base=16), rdict[key]])
		cnt += 1

	df = pd.DataFrame(result)
	df.to_csv(sys.argv[2], sep=',')
	print()
	print("***************************************")
	print()

