from math import ceil
from typing import overload

class Numbers:
	@overload
	def Even_(A: int) -> bool:
		return bool(A % 2 == 0)

	@overload
	def Even_(A: float) -> bool:
		return bool(ceil(A % 2) == 0)
	
	@overload
	def Odd_(A: int) -> bool:
		return bool(A % 2 == 1)

	@overload
	def Odd_(A: float) -> bool:
		return bool(A % 2 == 1)
 
	@overload(int, int)
	@overload(float, float)
	def Equal_(A: int, B: int) -> bool:
		return bool(A == B)
	
	@overload(int, int)
	@overload(float, float)
	def NotEqual_(A: int, B: int) -> bool:
		return bool(A != B)
	
	@overload(int, int)
	@overload(float, float)
	@overload(float, float)
	def NotEqual_(A: int, B: int) -> bool:
		return bool(A != B)