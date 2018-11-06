def additionMatrices(matrixOne, matrixTwo):
    finalMatrix = []
    indexRow = 0
    indexElement = 0

    for row in matrixTwo:
        finalMatrixRow = []
        indexElement = 0
        for element in row:
            sumElements = matrixOne[indexRow][indexElement] + matrixTwo[indexRow][indexElement]
            finalMatrixRow.append(sumElements) 
            indexElement += 1
        finalMatrix.append(finalMatrixRow)
        indexRow += 1

    print finalMatrix


def hasDifferentRowsNumber(matrixOne, matrixTwo):
    for row in matrixOne:
        for rowTwo in matrixTwo:
            if (len(row) != len(rowTwo)):
                return True
    return False

def main():
    matrixOne = [[1, 2, 3],[4, 5, 10]]
    matrixTwo = [[4, 12, 4],[9, 1, 2]]

    hasDifferentColumnsNumber = len(matrixOne) != len(matrixTwo) 
    if (hasDifferentColumnsNumber):
        print('Error, matrices with different number of columns')
    elif (hasDifferentRowsNumber(matrixOne, matrixTwo)):
        print('Error, matrices with different number of rows')
    else:
        additionMatrices(matrixOne, matrixTwo)

if __name__ == "__main__":
    main()