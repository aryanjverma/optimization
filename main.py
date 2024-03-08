import math
import random
from operations.preprocess import functionMaker
functionCalc = functionMaker()
function = [[1,4],[3,4],[-5,-7]]
coefs = functionCalc.traceFunction(function)
print(coefs)
newFunction = functionCalc.createFunction(coefs)
print(newFunction(0.5))
newDerivative = functionCalc.createDerivative(coefs)
print(newDerivative(0.5))