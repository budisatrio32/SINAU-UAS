import math

while True:
    try:
        m = int(input("Masukkan jumlah tim finalis(0 < m ≤ 10): "))
        n = int(input("Masukkan jumlah tim yang akan dipilih (0 < n ≤ 5): "))
    except ValueError:
        print("Input harus berupa angka")

    if m > 10 and n > 5:
        print("Jumlah tim finalis harus tidak boleh lebih dari 10")
        print("Jumlah tim yang akan dipilih tidak boleh lebih dari 5")
        
    elif m > 10:
        print("Jumlah tim finalis harus tidak boleh lebih dari 10")
    
    elif n > 5:
        print("Jumlah tim yang akan dipilih tidak boleh lebih dari 5")
    
    else:
        jumlah_petandingan = math.factorial(m)
        jumlah_cara_memilih_tim = math.comb(m, n)

        print(f"Jumlah cara untuk menentukan urutan presentasi dari {m} tim adalah {jumlah_petandingan}")
        print(f"Jumlah cara yang berbeda untuk memilih {n} tim dari {m} tim finalis adalah {jumlah_cara_memilih_tim}")
        break
