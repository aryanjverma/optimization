import math
import random
from operations.preprocess import functionMaker, functionProperties
functionCalc = functionMaker()
e = math.e
'''
function = [[1,3.71828182846],[2,15.7781121979],[0,1]]
diffs = [[1,5.43656365692],[2,22.1671682968],[0,1]]
coefs = functionCalc.diffTraceFunction(function, diffs)
'''
coefs = [1,3,1,-4,1]

propertyFinder = functionProperties()
print(propertyFinder.findAllZeros(coefs))
exit(3)
coefs = [1,1,0,1]
print(coefs)
newSquare = propertyFinder.createSquareFunction(coefs)
print(newSquare)
print(propertyFinder.findZero(coefs))