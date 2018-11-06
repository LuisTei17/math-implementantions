# Finish the logic

def transposition(matrix):
    indexColumn = 0

    finalMatrix = []
    for row in matrix:
        matrixElement = []
        indexRow = 0
        finalMatrix[indexColumn] = []
        for element in row:
            print(indexRow)        
            num = matrix[indexRow][indexColumn];    
            finalMatrix[indexRow][indexColumn] = num
            indexRow += 1
        indexColumn += 1        
    print(finalMatrix)

def main():
    matrix = [[1, 2, 5], [12, 4, 5]]

    transposition(matrix)

if __name__ == "__main__":
    main()