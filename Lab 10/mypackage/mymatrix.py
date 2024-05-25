def isMatrix(A):
    if len(A) < 2:
        return False
    else:
        for i in range(len(A)):
            if len(A[i]) != len(A[0]):
                return False
        return True

def inMatrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end = " ")
        print()

def isSquare(A):
    if len(A) != len(A[0]):
        return False
    return True

def ChangeRow(A,row1, row2):
    if row1 < 0 or row1 >= len(A) or row2 < 0 or row2 >= len(A):
        return False
    else:
        temp = A[row1]
        #Thay đổi vị trí 2 hàng
        A[row1] = A[row2]
        A[row2] = temp
        return True
    
def ChangeCol(A,col1, col2):
    if col1 < 0 or col1 >= len(A[0]) or col2 < 0 or v >= len(A[0]):
        return False
    else:
        for row in range(len(A)):
            A[row][col1], A[row][col2] = A[row][col2], A[row][col1]
        return True
    
def transpose(A):
    chuyen_vi = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            chuyen_vi[j][i] = A[i][j]
    return chuyen_vi

def GetSymetry(A):
    if len(A) != len(A[0]):
        return False
    else:
        for i in range(len(A)):
            for j in range(i, len(A[0])):
                if A[i][j] != A[j][i]:
                    return False
        return True