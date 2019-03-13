import sys
fname = "Act_File_Map_9.csv"
f = open(fname, "r")
l = f.readlines()

fname2 = "corrected_"+fname
with open(fname2, "w") as f2:
	s = "Act_Name, Year, File_Name,\n"
	f2.write(s)
	for i in range (1,len(l),1):
		print(l[i])
		segs = (l[i].strip('\n')).split(',')
		print(segs)
		
		if(len(segs) ==  0):
			s += "\t,\t,\t"
		if(len(segs) > 0):
			s = segs[0] + ","
		if(len(segs)==1):
			s += "\t,\t"
		if(len(segs)>1):
			s += segs[1] + ",\t"
		if(len(segs)>2):
			for j in range(2,len(segs), 1):
				s += segs[j]
				s += "\t"

		print(len(segs))
		print("here ssis s : ", s)
		f2.write(s)
		f2.write("\n")
		# sys.exit()

