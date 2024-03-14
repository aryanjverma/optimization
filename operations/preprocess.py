import math
from random import random
class functionMaker:
    def __init__(self):
        pass
    def solveSystem(self, inArray):
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
                temp = self.plugVar(targetArray, plug)
                solutions.append(temp)
            
            
            newSol = self.solveSystem(solutions)
            
            variables = self.conCat(newSol, variables)
            
            newEquation = self.plugVal(array,variables)
            newSol = self.solveSystem([newEquation])
            
            return self.conCat(newSol, variables)
            
    def plugVal(self, big, vals):
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
    def plugVar(self, big, plug):
        solutions = []
        firstCoef = big[0]
        for index in range (1,len(big) - 1):
            solution = big[index] + firstCoef * plug[index]
            solutions.append(solution)
        final = big[-1] - firstCoef * plug[-1]
        solutions.append(final)
        
        return solutions
    def conCat(self,array1,array2):
        newArray = []
        for element in array1:
            newArray.append(element)
        for element in array2:
            newArray.append(element)
        return newArray
    def traceFunction(self,functionSet):
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
        return self.solveSystem(system)
    def diffTraceFunction(self,functionSet,diffSet):
        degree = len(functionSet) * 2
        
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
        for element in diffSet:
            newEquation = []
            xVal = element[0]
            newEquation.append(0)
            for index in range(1,degree):
                newCoef = (index) * (xVal ** (index-1)) 
                newEquation.append(newCoef)
            
            diffVal = element[1]
            newEquation.append(diffVal)
            system.append(newEquation)
        
        return self.solveSystem(system)

    def createFunction(self,coeffecients):
        coefAmount = len(coeffecients)
        def mathFunction(xVal):
            finalVal = 0
            for index in range (0,coefAmount):
                change = coeffecients[index] * xVal ** index
                finalVal += change
            return finalVal
        return mathFunction
    def createDerivative(self,oldCoefs):
        functionSize = len(oldCoefs)
        newCoefs = self.deriveCoefs(oldCoefs)
        def mathDerivative(xVal):
            derivative = self.createFunction(newCoefs)
            return(derivative(xVal))
        return mathDerivative
    def deriveCoefs(self,coeffecients):
        coefAmount = len(coeffecients)
        finalCoefs = []
        for index in range(0,coefAmount):
            newCoef = index * coeffecients[index]
            finalCoefs.append(newCoef)
        return finalCoefs[1:]

class functionProperties:
    def __init__(self):
        self.functionCalc = functionMaker()
    def createSquareFunction(self,coefs):
        function = self.functionCalc.createFunction(coefs)
        newDegree = 2* len(coefs)
        functionSet = []
        for xVal in range(0,newDegree):
            newPair = [xVal]
            yVal= (function(xVal)) ** 2
            newPair.append(yVal)
            functionSet.append(newPair)
        newSquareFunc = self.functionCalc.traceFunction(functionSet)
        newSquareFunc.pop()
        return newSquareFunc
    def findSquareZero(self,coefs):
        newCoefs = self.createSquareFunction(coefs)
        newFunc = self.functionCalc.createFunction(newCoefs)
        derivative = self.functionCalc.createDerivative(newCoefs)
        xVal = 0
        count = 0
        while math.fabs(newFunc(xVal)) > 1/(10**6):
            count += 1
            if derivative(xVal) == 0:
                xVal += 1
            else:
                currentVal = newFunc(xVal)
                currentDiff = derivative(xVal)
                xVal -= currentVal/currentDiff 
        print(count)
        return xVal
    def findZero(self,coefs,lowerBound,upperBound):
        newFunc = self.functionCalc.createFunction(coefs)
        derivative = self.functionCalc.createDerivative(coefs)
        if lowerBound == "No":
            xVal = upperBound
        elif upperBound == "No":
            xVal = lowerBound
        else:
            xVal = (lowerBound + upperBound)/2
        maxIterations = 1000 
        
        for iteration in range(maxIterations):
            if math.fabs(newFunc(xVal)) < (10**-6):
                return xVal
            if derivative(xVal) == 0:
                
                xVal += 1
            else:
                currentVal = newFunc(xVal)
                currentDiff = derivative(xVal)
                xVal -= currentVal/currentDiff
                
                if upperBound != "No":
                    if xVal > upperBound:
                        xVal = upperBound
                if lowerBound != "No":
                    if xVal < lowerBound:
                        xVal = lowerBound
        return "No"
    def findAllZeros(self,coefs): 
        degree = len(coefs)
        if degree == 2:
            return [-1 * coefs[0]/coefs[1]]
        else:
            
            newFunc = self.functionCalc.createFunction(coefs)
            derivativeCoefs = self.functionCalc.deriveCoefs(coefs)
            derivative = self.functionCalc.createFunction(derivativeCoefs)
            guessList = self.findAllZeros(derivativeCoefs)
            for index in range(len(guessList)):
                if index == 0:
                    temp = guessList[index]
                    guessList.insert(0,temp)
                    guessList[index] -= 10**-6
                else:
                    guessList[index] += 10**-6
            if len(guessList) == 0:
                guessList.append(0)
            guessList.insert(0,"No")
            guessList.append("No")
            guessAmount = len(guessList)
            zeroList = []
            
            for iteration in range(guessAmount - 1):
                
                lowerBound = guessList[iteration]
                upperBound = guessList[iteration + 1]
                zero = self.findZero(coefs,lowerBound,upperBound)
                if zero != "No":
                    newZeroCheck = 1
                    for oldZero in zeroList:
                        if math.fabs(oldZero - zero) < (10**-3):
                            newZeroCheck = 0
                    if newZeroCheck == 1:
                        zeroList.append(zero)
                    
            return zeroList