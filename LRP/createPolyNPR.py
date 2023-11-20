from nhiemvu1 import *
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


def rut_gon_he_so_va_bac(Expr_poly, p):
    """
    Expr_poly đưa vào theo cặp ví dụ : 242x^105 + 262x^17
    thì tương ứng là : list [[242,105],[262,17]]
    """
    new_coefficients = [0] * p
    for para in Expr_poly:
        t_1 = para[0] % p
        if t_1:
            if para[1] != 0:
                t2 = para[1] % (p - 1)
                if t2:
                    new_coefficients[t2] = (new_coefficients[t2] + t_1) % p
                else:
                    new_coefficients[p - 1] = (new_coefficients[p - 1] + t_1) % p
            else:
                new_coefficients[0] = (new_coefficients[0] + t_1) % p
    new_coefficients.reverse()
    return new_coefficients


def tim_ucln_f1_poly_chung(Expr_poly, p):
    (
        Mang_phep_cong,
        Mang_phep_nhan,
        Mang_doi_cong,
        Mang_nghich_dao,
        Mang_phep_tru,
        Mang_phep_chia,
    ) = khoi_tao_pole(p)
    """
    Expr_poly đưa vào theo cặp ví dụ : 3x^2+2x+1
    thì tương ứng là : list [3,2,1]
    """
    coeff_pl2 = [0] * (p + 1)
    coeff_pl2[0] = 1
    coeff_pl2[-2] = p - 1
    temp = gcd_poly(np.array(Expr_poly), np.array(coeff_pl2))
    print(temp)


def function_bien_doi_loai1(Expr_ply, p):
    n = len(Expr_ply) - 1
    new_coefficients = [0] * (p**n)
    new_length = len(new_coefficients)
    for i in range(0, n + 1):
        new_coefficients[new_length - (p**i)] = Expr_ply[n - i]
    print(new_coefficients)


def function_bien_doi_loai2(Expr_ply, p):
    n = len(Expr_ply) - 1
    new_coefficients = [0] * ((p**n) + 1)
    new_length = len(new_coefficients)
    for i in range(0, n + 1):
        new_coefficients[new_length - (p**i) - 1] = Expr_ply[n - i]
    print(new_coefficients)


def nhan_pha_luy_thua(b, so_mu, mod):
    so_mu = int(so_mu)
    """_summary_
    đa thức có dạng : (x-b)^so_mu
    Args:
        Expr_poly (_type_): _description_
        so_mu (_type_): _description_
    """
    res = []
    for i in range(so_mu + 1):
        hs = (math.comb(so_mu, i) * ((-b) ** (so_mu - i))) % mod
        res.append(hs)
    res.reverse()
    return res


def tim_nghiem(poly_d, mod_p, denta, list_nghiem):
    if len(poly_d) != 2:
        poly_denta = nhan_pha_luy_thua(denta, (mod_p - 1) / 2, mod_p)
        poly_denta[-1] = Mang_phep_tru[poly_denta[-1]][1]
        h = gcd_poly(np.array(poly_d), np.array(poly_denta))
        while len(h) == 1 or len(h) == len(poly_d):
            denta += 1
            poly_denta = nhan_pha_luy_thua(denta, (mod_p - 1) / 2, mod_p)
            poly_denta[-1] = Mang_phep_tru[poly_denta[-1]][1]
            h = gcd_poly(np.array(poly_d), np.array(poly_denta))
        temp = poly_divide(np.array(poly_d), h)[0]
        tim_nghiem(h, mod_p, denta + 1, list_nghiem)
        tim_nghiem(temp.tolist(), mod_p, denta + 1, list_nghiem)
    else:
        list_nghiem.append(poly_d[-1])


# khoi_tao_pole()
# function_bien_doi_loai2([1, 2, 3], 2)
# print(rut_gon_he_so_va_bac([[1, 3], [7, 2], [10, 1], [16, 0]], 3))

# tim_ucln_f1_poly_chung([1, 2, 1], 3)
# print(nhan_pha_luy_thua(2, 2, 5))
list_nghiem = []
(
    Mang_phep_cong,
    Mang_phep_nhan,
    Mang_doi_cong,
    Mang_nghich_dao,
    Mang_phep_tru,
    Mang_phep_chia,
) = khoi_tao_pole(3)
tim_nghiem([1, 2, 1], 3, 0, list_nghiem)
list_nghiem = list(set(list_nghiem))
print(list_nghiem)
