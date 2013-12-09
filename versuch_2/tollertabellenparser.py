#!/usr/bin/python3

fname=input("Wie heißt die Datei?")
f=open(fname)
fstr=f.read()
flist=fstr.splitlines()
roundlist=[]
for eintrag in flist:
	a=eintrag.split()[0]
    ar=a.split(,)[0]
    b=eintrag.split()[1]
    bp=b.replace(",",".")
    br=round(bp,2)
    eintragb=[ar,br]
    eintragedit=eintragb.join("\t&\t")
    roundlist.append(eintragedit+"\\\\\n")


