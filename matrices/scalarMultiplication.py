def scalarMultiplication(matrix, multiplier):
    finalMatrix = []
    for row in matrix:
        matrixElement = []
        for element in row:
            element *= multiplier
            matrixElement.append(element)
        finalMatrix.append(matrixElement)
    print(finalMatrix)

def main():
    matrix = [[1, 2, 5], [12, 4, 5], [1, 4, 5]]
    multiplier = 2

    scalarMultiplication(matrix, multiplier)

if __name__ == "__main__":
    main()