import random as R

def Int(Min: int, Max: int) -> int:
	return R.randint(Min, Max)

def Float(Min: float, Max: float) -> float:
	return R.random()

def String(Sz: int, Chars: str) -> str:
	Out = Chars[Int(0, Sz)]

	for i in range(1, Sz, 1):
		Out += Chars[Int(0, Sz)]

	return Out

def Char(Chars: str):
	return Chars[Int(0, len(Chars))]

