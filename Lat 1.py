import math

m = float(input("Masukkan jarak atap rumah ke tanah: "))
n = float(input("Masukkan panjang tangga: "))

jarak = math.sqrt(n**2 - m**2)

sinus = m/n
sudut = math.asin(sinus)
kemiringan = (round(math.degrees(sudut),2))

print(jarak)
print(kemiringan)
