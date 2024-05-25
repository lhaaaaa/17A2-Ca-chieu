def cong_ma_tran(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return -1
    else:
        C = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                row.append(A[i][j] + B[i][j])
            C.append(row)
        return C
    
def tru_ma_tran(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return -1
    else:
        C = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                row.append(A[i][j] - B[i][j])
            C.append(row)
        return C

def nhan_ma_tran(A, B):
    if len(A) != len(B[0]) or len(A[0]) != len(B):
        return -1 
    else:
        C = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                sum = 0
                for k in range(len(B)):
                    sum += A[i][k] * B[k][j]
                row.append(sum)
            C.append(row)
        return C