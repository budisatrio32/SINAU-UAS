import pandas as pd

df = pd.read_csv('katalog_gempa.csv')
print(df[df['remark'] == 'Banda Sea'])