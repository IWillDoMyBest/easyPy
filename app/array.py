import sys, os
from ..ext.errorHandling import listError, valueError

sys.dont_write_bytecode = True

def minValue(array):
	try:
		if not isinstance(array, list):
			print(listError, file=sys.stderr), sys.exit()

		for i in array:
			if not isinstance(i, float) and not isinstance(i, int):
				print(valueError, file=sys.stderr), sys.exit()

		array.sort()
		return array[0]
	except Exception as error:
		print(error, file=sys.stderr)

def maxValue(array):
	try:
		if not isinstance(array, list):
			print(listError, file=sys.stderr), sys.exit()

		for i in array:
			if not isinstance(i, float) and not isinstance(i, int):
				print(valueError, file=sys.stderr), sys.exit()

		array.sort()
		return array[-1]
	except Exception as error:
		print(error, file=sys.stderr)

def sumValue(array):
	try:
		aSum = 0

		if not isinstance(array, list):
			print(listError, file=sys.stderr), sys.exit()

		for i in array:
			if not isinstance(i, float) and not isinstance(i, int):
				print(valueError, file=sys.stderr), sys.exit()

		for i in array:
			aSum += int(i)

		return aSum
	except Exception as error:
		print(error, file=sys.stderr)

def averageValue(array):
	try:
		if not isinstance(array, list):
			print(listError, file=sys.stderr), sys.exit()

		for i in array:
			if not isinstance(i, float) and not isinstance(i, int):
				print(valueError, file=sys.stderr), sys.exit()

		array.sort()
		return float("{0:.2f}".format(float(sumValue(array)) / float(len(array))))
	except Exception as error:
		print(error, file=sys.stderr)

def sortList(array): 
	try:
		if not isinstance(array, list):
			print(listError, file=sys.stderr), sys.exit()

		for i in array:
			if not isinstance(i, float) and not isinstance(i, int):
				print(valueError, file=sys.stderr), sys.exit()

		for i in range(len(array)):
		    for j in range(i, len(array)):
		        if(array[i] > array[j]):
		            array[i], array[j] = array[j], array[i]
		            
		return array
	except Exception as error:
		print(error, file=sys.stderr)

def minIndex(array):
	try:
		if not isinstance(array, list):
			print(listError, file=sys.stderr), sys.exit()

		if len(array) == 0:
			return None

		for i in array:
			if not isinstance(i, float) and not isinstance(i, int):
				print(valueError, file=sys.stderr), sys.exit()

		minValue = array[0]
		for i in range(len(array)):
			if minValue > array[i]:
				minValue = array[i]

		return array.index(minValue)	

	except Exception as error:
		print(error, file=sys.stderr)

def maxIndex(array):
	try:
		if not isinstance(array, list):
			print(listError, file=sys.stderr), sys.exit()

		for i in array:
			if not isinstance(i, float) and not isinstance(i, int):
				print(valueError, file=sys.stderr), sys.exit()

		if len(array) == 0:
			return None

		maxValue = array[0]

		for i in range(len(array)):
			if maxValue < array[i]:
				maxValue = array[i]
		return array.index(maxValue)

	except Exception as error:
		print(error, file=sys.stderr)

def rDub(array):
	try:
		if not isinstance(array, list):
			print(listError, file=sys.stderr), sys.exit()
		
		for i in array:
			if not isinstance(i, float) and not isinstance(i, int):
				print(valueError, file=sys.stderr), sys.exit()

		newList = []

		for i in array:
			if i not in newList:
				newList.append(i)
		return newList

	except Exception as error:
		print(error, file=sys.stderr)

def diff(array):
	try:
		if not isinstance(array, list):
			print(listError, file=sys.stderr), sys.exit()

		for i in array:
			if not isinstance(i, float) and not isinstance(i, int):
				print(valueError, file=sys.stderr), sys.exit()
		return maxValue(array) - minValue(array)
	except Exception as error:
		print(error, file=sys.stderr)

def strToList(string):
	try:
		if not isinstance(string, str):
			print("Input needs to string", file=sys.stderr)
		return [letter for letter in string]
	except Exception as error:
		print(error, file=sys.stderr)
