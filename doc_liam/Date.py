from datetime import date

class Current(object):
	def Years(self) -> str:
		return str(date.today().year)

	def Months(self) -> str:
		return str(date.today().month)
	
	def Days(self) -> str:
		return str(date.today().day)
	
	def Full(self) -> str:
		Y = self.Years()
		M = self.Months()
		D = self.Days()

		return str(Y) + '-' + str(M) + '-' + str(D)

	def DayOfWeek(self) -> str:
		DayCode = date.today().weekday()
		Out: str
 
		if DayCode == 0:
			Out = 'Sunday'
		elif DayCode == 1:
			Out = 'Monday'
		elif DayCode == 2:
			Out = 'Tuesday'
		elif DayCode == 3:
			Out = 'Wednesday'
		elif DayCode == 4:
			Out = 'Thursday'
		elif DayCode == 5:
			Out = 'Friday'
		elif DayCode == 6:
			Out = 'Saturday'

		return Out