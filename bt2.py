# expression_matcher.py
# Bài 2: Matching mathematical expressions
from kanren import run, var, fact
import kanren.assoccomm as la
# Định nghĩa các phép toán
add = 'addition'
mul = 'multiplication'

# Khai báo tính chất giao hoán, kết hợp
fact(la.commutative, add)
fact(la.commutative, mul)
fact(la.associative, add)
fact(la.associative, mul)

# Tạo biến
a, b, c = var('a'), var('b'), var('c')

# Biểu thức gốc
# expression_orig = 3 * (-2) + (1 + 2 * 3) * (-1)

expression_orig = (add,
                   (mul, 3, -2),
                   (mul, (add, 1, (mul, 2, 3)), -1))

# Các biểu thức biến đổi (dạng có biến a, b, c)
# ((1+(2a))×b)+(3×c) đưa số 3, -2, -1 thành biến a, b, c
expression1 = (add,
               (mul, (add, 1, (mul, 2, a)), b),
               (mul, 3, c))

# (c×3)+(b×((2a)+1)) hoán đổi thứ tự nhân/cộng
expression2 = (add,
               (mul, c, 3),
               (mul, b, (add, (mul, 2, a), 1)))

# (((2a)×b)+b)+(3×c) khai triển phân phối
expression3 = (add,
               (add, (mul, (mul, 2, a), b), b),
               (mul, 3, c))

# So khớp biểu thức
print("So khớp expression1 với expression_orig:")
print(run(0, (a, b, c), la.eq_assoccomm(expression1, expression_orig)))

print("So khớp expression2 với expression_orig:")
print(run(0, (a, b, c), la.eq_assoccomm(expression2, expression_orig)))

print("So khớp expression3 với expression_orig:")
print(run(0, (a, b, c), la.eq_assoccomm(expression3, expression_orig)))
