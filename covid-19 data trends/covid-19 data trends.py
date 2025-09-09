# covid_trends.py
import pandas as pd
import matplotlib.pyplot as plt

covid = pd.read_csv('covid_data.csv', parse_dates=['Date'])

# Global daily cases
daily_cases = covid.groupby('Date')['New_cases'].sum()

# Plot
plt.figure(figsize=(10,5))
daily_cases.plot()
plt.title('Global Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.tight_layout()
plt.show()
