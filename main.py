import math
import random
def solveSystem(inArray):
    
    array = inArray 
    
    if len(array) == 1:
        newArray = array[0] 
        return [newArray[1]/newArray[0]]
    else:
        solutions = []
        variables = []
        targetArray = array[0]
        firstCoef = targetArray[0]
        plug = [1]
        
        
        for index in range(1,len(targetArray) - 1):
            newCoef = -1 * targetArray[index]/firstCoef
            plug.append(newCoef)
        plug.append(targetArray[-1]/firstCoef)
        
        for index in range(1,len(array)):
            targetArray = array[index]
            temp = plugVar(targetArray, plug)
            solutions.append(temp)
        
        
        newSol = solveSystem(solutions)
        
        variables = conCat(newSol, variables)
        
        newEquation = plugVal(array,variables)
        newSol = solveSystem([newEquation])
        
        return conCat(newSol, variables)
        
def plugVal(big, vals):
    startArray = big[:]
    outputArray = startArray[0]
    
    constant = outputArray.pop()
    finalVal = constant
    valEnd = len(vals)
    for index in range(0,valEnd):
        valCoef = outputArray.pop()
        val = vals[valEnd-index-1]
        finalVal -= valCoef * val 
    
    outputArray.append(finalVal)
    
    return outputArray
def plugVar(big, plug):
    solutions = []
    firstCoef = big[0]
    for index in range (1,len(big) - 1):
        solution = big[index] + firstCoef * plug[index]
        solutions.append(solution)
    final = big[-1] - firstCoef * plug[-1]
    solutions.append(final)
    
    return solutions
def conCat(array1,array2):
    newArray = []
    for element in array1:
        newArray.append(element)
    
    
    for element in array2:
        newArray.append(element)
    
    return newArray
def traceFunction(functionSet):
    degree = len(functionSet)
    system = []
    for element in functionSet:
        newEquation = []
        xVal = element[0]
        for index in range(0,degree):
            newCoef = xVal ** index
            newEquation.append(newCoef)
        yVal = element[1]
        newEquation.append(yVal)
        system.append(newEquation)
    return solveSystem(system)

def createFunction(coeffecients):
    coefAmount = len(coeffecients)
    def mathFunction(xVal):
        finalVal = 0
        for index in range (0,coefAmount):
            change = coeffecients[index] * xVal ** index
            finalVal += change
        return finalVal
    return mathFunction
def createDerivative(function):
    functionSize = len(function)
    newCoefs = deriveCoefs(function)
    def mathDerivative(xVal):
        derivative = createFunction(newCoefs)
        return(derivative(xVal))
    return mathDerivative
def deriveCoefs(coeffecients):
    coefAmount = len(coeffecients)
    finalCoefs = []
    for index in range(0,coefAmount):
        newCoef = index * coeffecients[index]
        finalCoefs.append(newCoef)
    
    return finalCoefs[1:]
function = [[1,2],[3,4],[2,9],[4,3]]
coefs = traceFunction(function)
print(coefs)
newFunction = createFunction(coefs)
print(newFunction(0.5))
newDerivative = createDerivative(coefs)
print(newDerivative(0.5))