import os, sys
from ..ext.errorHandling import valueError

def translateBinary(binary, bytes):
    try:
        if not isinstance(binary, int):
             print(valueError, file=sys.stderr), sys.exit()

        holder = list(str(binary))

        for i in holder:
            if i != "1" and i != "0":
                print(valueError, file=sys.stderr), sys.exit()

        binaryList = [1]
        binarySum = 0

        for i in range(len(holder)-1):
            binaryList.insert(0, binaryList[0] * 2)

        for i in range(len(holder)):
            if int(holder[i]) == 1:
                binarySum += binaryList[i]
                
        return binarySum
    except Exception as error:
        print(error, file=sys.stderr), sys.exit()


