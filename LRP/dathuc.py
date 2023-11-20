import galois
from SolveSystemFinitePoleMatrixBacThang import *

MODULE = 2
# Định nghĩa trường hữu hạn
GF = galois.GF(MODULE)  # Ví dụ: Trường hữu hạn Z/7Z

# Tạo đa thức trên trường hữu hạn
# poly1 = galois.Poly([4, 3, 2, 1], field=GF)
# poly2 = galois.Poly([1, 1], field=GF)


def process(lst_hs, lst_index, col_b, mod):
    lst_cp = lst_hs.copy()
    lst_hs.reverse()
    poly1 = galois.Poly(lst_hs, field=GF)
    print(poly1)
    deg = len(lst_hs) - 1
    matrixA = []
    for elem in lst_index:
        temp = [0] * (elem + 1)
        temp[0] = 1
        # print(temp)
        poly2 = galois.Poly(temp, field=GF)
        # print(poly2)
        rem1 = divmod(poly2, poly1)[1]
        rem = list(divmod(poly2, poly1)[1].coeffs)
        # if elem == 8:
        rem.reverse()
        hieu_deg = deg - len(rem)
        for i in range(hieu_deg):
            rem.append(0)
        matrixA.append(rem.copy())
    # print(matrixA)
    # Chuyển đổi ma trận sang kiểu dữ liệu int
    matrixA_int = np.array([[int(element) for element in row] for row in matrixA])
    arrMultiple2, arrInverseSubtraction2 = createArrayMultModule(mod)
    solveSystemGFZ(
        matrixA_int,
        np.array(col_b),
        arrMultiple2=arrMultiple2,
        arrInverseSubtraction2=arrInverseSubtraction2,
        mod=mod,
    )
    lst_hs = lst_cp


################################################################
## hệ số nhập theo thứ tự từ f_0 ví dụ : 1 + 2x + 3x^3+x^4 [1,2,0,3,1]
lst_hs = [1, 0, 0, 1, 1, 1, 1]
lst_index = [1, 2, 4, 5, 8, 10, 15]
lst_curr_u = [0, 0, 1, 0, 1, 0, 0]
# 0, 0, 1, 0, 1, 0, 0
# lst_curr_u[2] = 1
process(lst_hs, lst_index, lst_curr_u, MODULE)
