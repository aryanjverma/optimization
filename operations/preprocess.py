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

    def createFunction(self,coeffecients):
        coefAmount = len(coeffecients)
        def mathFunction(xVal):
            finalVal = 0
            for index in range (0,coefAmount):
                change = coeffecients[index] * xVal ** index
                finalVal += change
            return finalVal
        return mathFunction
    def createDerivative(self,function):
        functionSize = len(function)
        newCoefs = self.deriveCoefs(function)
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
