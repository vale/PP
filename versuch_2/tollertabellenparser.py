#!/usr/bin/python2

fname=raw_input("Wie heisst die Datei?")
foutname=raw_input("Outputdatei?")
f=open(fname)
fstr=f.read()
f.close()
flist=fstr.splitlines()
flist=flist[::20]
roundlist=""
for eintrag in flist:
    a=eintrag.split()[0]
    a=a.split(",")[0]
    b=eintrag.split()[1]
    b=b.replace(",",".")
    b="%.2f"%float(b)
    b=b.replace(".",",")
    eintragb=a+"\t&\t"+b
    roundlist=roundlist+eintragb+"\\\\\n"
fout=open(foutname, "w")
fout.write(roundlist)
fout.close()
