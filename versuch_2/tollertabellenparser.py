#!/usr/bin/python3

fname=input("Wie heißt die Datei?")
f=open(fname)
fstr=f.read()
flist=fstr.splitlines()
for eintrag in flist:
	a=eintrag.split()[0] 
