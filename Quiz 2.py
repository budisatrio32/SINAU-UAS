import pandas as pd
import matplotlib.pyplot as plt


file_csv = pd.read_csv('katalog_gempa.csv')

data_bersih = file_csv.dropna()

# Membuat histogram untuk kolom 'mag'
plt.hist(data_bersih['mag'], bins=10, edgecolor='black', color='skyblue')
plt.title('Histogram Magnitudo Gempa')
plt.xlabel('Magnitudo')
plt.ylabel('Frekuensi')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Menampilkan histogram
plt.show()