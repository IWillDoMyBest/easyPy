import sys, os
from ..ext.errorHandling import listError, valueError

def pq(x, p, q): 
	try:
		if isinstance(x, int or float) and isinstance(p, int or float) and (q, int or float):
			if x != 1:
				p /= x
				q /= x
			if not ((p/2)**2-q) < 0:
				return round(((-p/2)+((p/2)**2-q)**0.5), 2), round(((-p/2)-((p/2)**2-q)**0.5), 2)
			return str(round((-p/2), 2)) + "+" + str(round((-1*((p/2)**2-q))**0.5, 2)) + "i", str((-p/2)) + "-" + str(round((-1*((p/2)**2-q))**0.5, 2)) + "i"		
			print(valueError, file=sys.stderr), sys.exit()
	except Exception as error:
		print(error, file=sys.stderr), sys.exit()

def root(x):
	try:
		if not isinstance(x, int):
			print(valueError, file=sys.stderr), sys.exit()
		if not x < 0:
			return x**0.5
		return str(round((x*-1)**0.5, 2)) + "i"

	except Exception as error:
		print(error, file=sys.stderr), sys.exit()

def distance(x, y):
	try:
		if not isinstance(x, (int, float)) and not isinstance(y, (int, float)):
			print(valueError, file=sys.stderr), sys.exit()
		return round(((x**2) +(y)**2)**0.5, 2) 
	except Exception as error:
		print(error, file=sys.stderr), sys.exit()

