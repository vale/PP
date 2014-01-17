#!/usr/bin/python2

#fname=raw_input("Wie heisst die Datei?")
fname="longtable.tex"
#foutname=raw_input("Outputdatei?")
foutname="shorttable.tex"
f=open(fname)
fstr=f.read()
f.close()
flist=fstr.splitlines()
flist=flist[::10]
shortlist=""
counter=0
for eintrag in flist:
	shortlist=shortlist+eintrag+"\n"
fout=open(foutname, "w")
fout.write(shortlist)
fout.close()
