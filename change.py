import fileinput
import sys
searchExp="10056298"
i=1
for line in fileinput.input("fuzzy-search.json", inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,str(i))
            i+=1
        sys.stdout.write(line)
