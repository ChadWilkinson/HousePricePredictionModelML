import os
from typing_extensions import Self 
from File import Exists_, Get

Ext = '.db'
ColSep = ';'
LineSep = '\n'
NbOfColumns = 0

def MkName(Name: str) -> str:
	return Name + Ext

def Create(Name: str, Columns: list[str]):
	Name += Ext
	ofs = open(Name, 'w+t')

	NbOfColumns = len(Columns)

	for i in Columns:
		ofs.write(i + ColSep)

	while ofs.closed == False:
		ofs.close()

	return None

class Write:
	class Line:
		def Enter(Name: str):
			Out: list[str]
			In: str
			ofs = open(Name + Ext)
			itr = 0

			while len(Out) != NbOfColumns:
				In = input('Data (' + ++itr + '/' + NbOfColumns + ') : ')
				Out.append(In)

				# Left as WIP here too

		def Add(Name: str, Data: list[str]):
			Out = ''

			for i in Data[0 : NbOfColumns]:
				Out += i + ColSep

			Out += LineSep

			ofs = open(Name + Ext, 'a+t')
			ofs.write(Out)

			while ofs.closed != True:
				ofs.close()

			return None

		def Change(Name: str, Ln: int, Data: list[str]) -> None:
			Lines: list[str]
			Line = ''
			ofs = open(Name + Ext, 'r+t')
			C = ofs.read()

			while C != None:
				Line += C
				C = ofs.read()

				if C == LineSep:
					Lines.append(Line)
					Line = ''

			# Left as WIP here