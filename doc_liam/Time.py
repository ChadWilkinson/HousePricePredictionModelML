from datetime import datetime

class Current(object):
	def Hours(self) -> str:
		Now = datetime.now()
		return str(Now.today().time().hour)
	
	def Minutes(self) -> str:
		Now = datetime.now()
		return str(Now.today().time().Minute)
	
	def Seconds(self) -> str:
		Now = datetime.now()
		return str(Now.today().time().second)
	
	def Full(self) -> str:
		H = self.Hours()
		M = self.Minutes()
		S = self.Seconds()

		return str(H) + '-' + str(M) + '-' + str(S)

	def SecondsSinceMidnight(self):
		Out: int

		Out	=		int(self.Hours()) * 3600
		Out +=	int(self.Minutes()) * 60
		Out +=	self.Seconds()

		return Out

	def AM_PM(self):
		H_i = int(self.Hours())
		Out: str

		if H_i <= 11:
			Out = 'AM'
		else:
			Out = 'PM'

		return Out
 
