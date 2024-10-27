a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
c = int(input("Masukkan bilangan C: "))

if a > b:
    if a > c:
        print("Bilangan A adalah terbesar")
    else:
        print("Bilangan C adalah terbesar")
else:
    if b > c:
        print("Bilangan B adalah terbesar")
    else:
        print("Bilangan C adalah terbesar")
