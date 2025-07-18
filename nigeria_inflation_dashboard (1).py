
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('nigeria_inflation.csv')

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Inflation Rate (%)'], marker='o', linestyle='-', color='blue')
plt.title('Nigeria Inflation Rate (2015–2023)')
plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')
plt.grid(True)

# Annotate min and max
min_val = df['Inflation Rate (%)'].min()
max_val = df['Inflation Rate (%)'].max()
min_year = df[df['Inflation Rate (%)'] == min_val]['Year'].values[0]
max_year = df[df['Inflation Rate (%)'] == max_val]['Year'].values[0]

plt.annotate(f'Lowest: {min_val}% in {min_year}', xy=(min_year, min_val),
             xytext=(min_year-1, min_val+3), arrowprops=dict(facecolor='green', shrink=0.05))

plt.annotate(f'Highest: {max_val}% in {max_year}', xy=(max_year, max_val),
             xytext=(max_year-2, max_val-5), arrowprops=dict(facecolor='red', shrink=0.05))

plt.tight_layout()
plt.show()
