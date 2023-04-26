from	genericpath	import exists
from	Log					import Error, Event, Warning
from	Charsets		import FileName

InvalidNames = "CON,PRN,AUX,NUL,COM1,COM2,COM3,COM4,COM5,COM6,COM7,COM8,COM9,LPT1,LPT2,LPT3,LPT4,LPT5,LPT6,LPT7,LPT8,LPT9".split(",")

def Exists_(File: str) -> bool:
	return exists(File)

class Get:
	def Name(self, MinSz: int, MaxSz: int):
		In: str
		InSz: int

		In = input('File name: ')
		InSz = len(In)

		while InSz < MinSz or InSz > MaxSz:
			print(In + " is not a valid option. Please try again\n")

			In = input('File name: ')
			InSz = len(In)

class Write:
	