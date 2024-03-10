import math
import random
from operations.preprocess import functionMaker, functionProperties
functionCalc = functionMaker()
function = [[1,3],[3,4],[4,2]]
diffs = [[1,4],[3,-4],[4,-2]]
coefs = functionCalc.diffTraceFunction(function, diffs)
print(coefs)

propertyFinder = functionProperties()
exit(3)
coefs = [1,1,0,1]
print(coefs)
newSquare = propertyFinder.createSquareFunction(coefs)
print(newSquare)
print(propertyFinder.findZero(coefs))