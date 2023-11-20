# from sympy import *

# x = symbols("x")
# coefficients = [4, 3, 2, 1]
# A = sum(coefficients[i] * x**i for i in range(len(coefficients)))
# print("Đa thức A:", A)

# # B = 3 + 2 * x**1 + 3 * x**2 + 4 * x**3 + 2 * x**4 + 2 * x**5 + 2 * x**6
# # gcd_A_B = gcd(A, B, domain=GF(7))
# # quo, rem = div(A, gcd_A_B, domain=GF(7))


# A = x**4 - 5 * x**3 + 5 * x**2 + 5 * x - 6
# factors = factor(A, domain=GF(2609))
# print("Phân tích đa thức thành nhân tử:", factors)


from sympy import *

x = symbols("x")
n = symbols("n", integer=True)
u = [1, 2, 3, 4]  # Các giá trị ban đầu của chuỗi số
F = 2 * x**2 + 3 * x + 1  # Hàm F(x)
p = Poly(u, x)  # Chuyển đổi list thành đa thức
un = rsolve_poly(F, p, n)  # Tìm công thức tổng quát của chuỗi số
print("Công thức tổng quát của chuỗi số là:", un)
