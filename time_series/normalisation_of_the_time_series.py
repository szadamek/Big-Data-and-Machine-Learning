import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('LBMA-GOLD.csv', nrows=100, usecols=['Date', 'USD (AM)', 'GBP (AM)'])
print(df)

attribute = ['USD (AM)', 'GBP (AM)']
df_sub = df[attribute]

X_min = df_sub.min()
X_max = df_sub.max()

# normalizujemy dane
df_normalized = (df_sub - X_min) / (X_max - X_min)

# Tworzymy wykres dla składowej "USD (AM)"
plt.plot(df_normalized['USD (AM)'], label='USD (AM)')
plt.title('Normalized LBMA Gold Prices')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

# Tworzymy wykres dla składowej "GBP (AM)"
plt.plot(df_normalized['GBP (AM)'], label='GBP (AM)')
plt.title('Normalized LBMA Gold Prices')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()
