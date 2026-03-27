# Nhập 3 số nguyên
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

print("\n=== a) Tổng và tích ===")
print("Tổng =", a + b + c)
print("Tích =", a * b * c)

print("\n=== b) Hiệu của 2 số bất kỳ ===")
print("a - b =", a - b)
print("a - c =", a - c)
print("b - c =", b - c)

print("\n=== c) Chia 2 số bất kỳ ===")
# a và b
print("a // b =", a // b)   # chia lấy phần nguyên
print("a % b =", a % b)     # chia lấy phần dư
print("a / b =", a / b)     # chia chính xác

# a và c
print("a // c =", a // c)
print("a % c =", a % c)
print("a / c =", a / c)

# b và c
print("b // c =", b // c)
print("b % c =", b % c)
print("b / c =", b / c)