import os, sys
from ..ext.errorHandling import valueError

def switch(a, b):
	try:
		a, b = b, a
	except Exception as error:
		print(error, file=sys.stderr), sys.exit()

def comb(*args):
	try:
		sumValue = 0
		for i in args:
			if not isinstance(i, (int, float)):
				print("\"" + i +"\"" +  " Needs be a int or float", file=sys.stderr), sys.exit()
			sumValue += i
		return sumValue
	except Exception as error:
		print(error, file=sys.stderr), sys.exit()
