from enum import Enum
from gzip import BadGzipFile
from msilib.schema import File
from os		import remove
from Date import Current as DtCur
from Time import Current as TmCur

Ext = '.log'

class Error:
	class File:
		Name = 'Error'
		FN = Name + Ext

		def Create(self) -> None:
			ofs = open(self.FN, 'w+t')

			ofs.write(self.Name + ' file created on ' + DtCur.Full() + ', at ' + TmCur.Full() + '.\n')

			while not(ofs.closed):
				ofs.close()

			return None

		def Delete(self) -> None:
			remove(self.FN)

		def Reset(self):
			self.Create()

	class Entry:
		def Single(self, Msg: str) -> None:
			Out = '[' + DtCur.Full() + ' ' + TmCur.Full() + '] '
			Out += self.Name + ' : ' + Msg + '\n'

			ofs = open(self.FN, 'a+t')
			ofs.write(Out)

			while not(ofs.closed):
				ofs.close()

			return None

		def Multiple(self, Msgs: list[str]) -> None:
			ofs = open(self.FN, 'a+t')

			for Msg in Msgs:
				Out = '[' + DtCur.Full() + ' ' + TmCur.Full() + '] '
				Out += self.Name + ' : ' + Msg + '\n'
				ofs.write(Out)

			while not(ofs.closed):
				ofs.close()

			return None

		class Code(Enum):
			NoError		= 0
			TooBig		= 1
			TooSmall	= 2
			BadInput	= 3
			BadOption	= 4
			BadFile		= 5

		def WithCode(self, Nb: Code) -> Code:
			Msg: str

			if self.Code.NoError:
				Msg = 'No error occurred.'
			elif self.Code.TooBig:
				Msg = 'The value is too big.'
			elif self.Code.TooSmall:
				Msg = 'The value is too small.'
			elif self.Code.BadInput:
				Msg = 'The input is not valid.'
			elif self.Code.BadOption:
				Msg = 'The input is not a valid option.'
			elif self.Code.BadOption:
				Msg = 'The given file does not exist or is inaccessible.'
			else:
				Msg = 'No error occured.'

			self.Single(Msg)

			return Nb

class Event:
	class File:
		Name = 'Event'
		FN = Name + Ext

		def Create(self) -> None:
			ofs = open(self.FN, 'w+t')

			ofs.write(self.Name + ' file created on ' + DtCur.Full() + ', at ' + TmCur.Full() + '.\n')

			while not(ofs.closed):
				ofs.close()

			return None

		def Delete(self) -> None:
			remove(self.FN)

		def Reset(self):
			self.Create()

	class Entry:
		def Single(self, Msg: str) -> None:
			Out = '[' + DtCur.Full() + ' ' + TmCur.Full() + '] '
			Out += self.Name + ' : ' + Msg + '\n'

			ofs = open(self.FN, 'a+t')
			ofs.write(Out)

			while not(ofs.closed):
				ofs.close()

			return None

		def Multiple(self, Msgs: list[str]) -> None:
			ofs = open(self.FN, 'a+t')

			for Msg in Msgs:
				Out = '[' + DtCur.Full() + ' ' + TmCur.Full() + '] '
				Out += self.Name + ' : ' + Msg + '\n'
				ofs.write(Out)

			while not(ofs.closed):
				ofs.close()

			return None

		class Code(Enum):
			NoError		= 0
			TooBig		= 1
			TooSmall	= 2
			BadInput	= 3
			BadOption	= 4
			BadFile		= 5

		def WithCode(self, Nb: Code) -> Code:
			Msg: str

			if self.Code.NoError:
				Msg = 'No error occurred.'
			elif self.Code.TooBig:
				Msg = 'The value is too big.'
			elif self.Code.TooSmall:
				Msg = 'The value is too small.'
			elif self.Code.BadInput:
				Msg = 'The input is not valid.'
			elif self.Code.BadOption:
				Msg = 'The input is not a valid option.'
			elif self.Code.BadOption:
				Msg = 'The given file does not exist or is inaccessible.'
			else:
				Msg = 'No error occured.'

			self.Single(Msg)

			return Nb

class Warning:
	class File:
		Name = 'Warning'
		FN = Name + Ext

		def Create(self) -> None:
			ofs = open(self.FN, 'w+t')

			ofs.write(self.Name + ' file created on ' + DtCur.Full() + ', at ' + TmCur.Full() + '.\n')

			while not(ofs.closed):
				ofs.close()

			return None

		def Delete(self) -> None:
			remove(self.FN)

		def Reset(self):
			self.Create()

	class Entry:
		def Single(self, Msg: str) -> None:
			Out = '[' + DtCur.Full() + ' ' + TmCur.Full() + '] '
			Out += self.Name + ' : ' + Msg + '\n'

			ofs = open(self.FN, 'a+t')
			ofs.write(Out)

			while not(ofs.closed):
				ofs.close()

			return None

		def Multiple(self, Msgs: list[str]) -> None:
			ofs = open(self.FN, 'a+t')

			for Msg in Msgs:
				Out = '[' + DtCur.Full() + ' ' + TmCur.Full() + '] '
				Out += self.Name + ' : ' + Msg + '\n'
				ofs.write(Out)

			while not(ofs.closed):
				ofs.close()

			return None

		class Codes(Enum):
			NoError		= 0
			TooBig		= 1
			TooSmall	= 2
			BadInput	= 3
			BadOption	= 4
			BadFile		= 5

		def WithCode(self, Nb: Codes) -> Codes:
			Msg: str
			Out = Nb

			if		Nb ==	self.Codes.NoError:
				Msg = 'No error occurred.'
			elif	Nb ==		self.Codes.TooBig:
				Msg = 'The value is too big.'
			elif	Nb ==	self.Codes.TooSmall:
				Msg = 'The value is too small.'
			elif	Nb ==	self.Codes.BadInput:
				Msg = 'The input is not valid.'
			elif	Nb ==	self.Codes.BadOption:
				Msg = 'The input is not a valid option.'
			elif	Nb ==	self.Codes.BadOption:
				Msg = 'The given file does not exist or is inaccessible.'
			else:
				Msg = 'No error occured.'

			self.Single(Msg)

			return Out

