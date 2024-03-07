def solveSystem(inArray):
    varCount = len(inArray) 
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
print(solveSystem([[1,1,-3,1,2],[-5,3,-4,1,0],[1,1,2,-1,1],[1,2,-2,-2,12]]))