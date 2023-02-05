def nikalant_row(d):
    pi_val, sign_t, m = 3, 1, 2
    while abs(pi_val - (pi_val + sign_t * 4 / (m ** 3 + 3 * m ** 2 + 2 * m))) > 10 ** (-d-1):
        pi_val = pi_val + sign_t * 4 / (m ** 3 + 3 * m ** 2 + 2 * m)
        sign_t = -1 * sign_t
        m = m + 2
    return round((pi_val + (pi_val + sign_t * 4 / (m ** 3 + 3 * m ** 2 + 2 * m))) / 2, d)

d = int(input('Введите точность определения числа ПИ (количество знаков после запятой): '))
pi = nikalant_row(d)
print(f'С точностью {d = }, число {pi = }; ')