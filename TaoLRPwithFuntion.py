import numpy as np
import pyfiglet

print(
    "================================================================================================"
)

big_font = pyfiglet.Figlet()
font = pyfiglet.Figlet(font="standard")
print(font.renderText("Copyright@ By HoangCoder "))
print(
    "================================================================================================\n\n"
)

DEGREE = 2
CHARACTER = 2
SIZEPOLE = 4
hsPole = 7
arrMultiple = [[0] * SIZEPOLE for i in range(SIZEPOLE)]
arrInverseSubtraction = [0] * SIZEPOLE


def multipleTwoElementField(a, b):
    if a == 0 or b == 0:
        return 0
    result = 0
    temp = 1 << DEGREE
    a_cp = 0
    k = 0
    t = 0
    while b != 0:
        if b & 0x1:
            t = k
            a_cp = a
            while t:
                a_cp <<= 1
                t -= 1
                if a_cp & temp:
                    a_cp ^= hsPole
            result ^= a_cp
        k += 1
        b >>= 1
    return result


def createArrayMult():
    temp = 0
    for i in range(SIZEPOLE):
        for j in range(i, SIZEPOLE):
            temp = multipleTwoElementField(i, j)
            arrMultiple[i][j] = temp
            arrMultiple[j][i] = temp
            if temp == 1:
                arrInverseSubtraction[i] = j
                arrInverseSubtraction[j] = i


def createArrayMultModule(module):
    temp = 0
    for i in range(module):
        for j in range(i, module):
            temp = (i * j) % module
            arrMultiple2[i][j] = temp
            arrMultiple2[j][i] = temp
            if temp == 1:
                arrInverseSubtraction2[i] = j
                arrInverseSubtraction2[j] = i


def tao_lrp(lst_hs, lst_start_u, begin_id, end_id, module):
    if end_id < begin_id:
        print("end_id <begin_id\n")
        return
    m = len(lst_hs) - 1
    for i in range(0, end_id):
        temp = 0
        for j in range(m):
            temp = (temp - arrMultiple2[lst_start_u[i + j]][lst_hs[j]]) % module
        lst_start_u.append(temp)
    print(lst_start_u[begin_id:end_id])
    # for idd in [1, 2, 4, 5, 8, 10, 15]:
    #     print(lst_start_u[idd], end=", ")


######################## khi dùng nhớ sửa biến module  #################
module = 5
arrMultiple2 = [[0] * module for i in range(module)]
arrInverseSubtraction2 = [0] * module
createArrayMultModule(module=module)
######### lst_hs : hệ số của function ví dụ : 1+2x+3x^2+x^5 thì sẽ nhập là : [1,2,3,0,0,1]
tao_lrp(
    lst_hs=[4, 3, 0, 0, 0, 1, 0, 1],
    lst_start_u=[2, 2, 2, 3, 4, 1, 1],
    begin_id=0,
    end_id=3 * 7,
    module=module,
)
