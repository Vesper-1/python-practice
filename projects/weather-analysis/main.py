import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
barwid = 2
days = np.arange(1,31)
centers = days * 5
tcol = 'temperature_2m_mean (°C)'
city1 = pd.read_csv('data/Austin-20250901-20250930.csv')
city2 = pd.read_csv('data/NewYork-20250901-20250930.csv')
autemp = city1[tcol]
nytemp = city2[tcol]
auprec = city1['precipitation_sum (mm)']
nyprec = city2['precipitation_sum (mm)']
auarr = autemp.to_numpy()
nyarr = nytemp.to_numpy()
dflist = np.abs(auarr[:30] - nyarr[:30])
# -->
city1['temp_ma3'] = (
    city1[tcol].rolling(window=3, center=True, min_periods=1).mean()
)
city2['temp_ma3'] = (
    city2[tcol].rolling(window=3, center=True, min_periods=1).mean()
)

fig, ax1 = plt.subplots(figsize=(16, 8))
plt.title('Comparison of Weather in Austin and New York in Sep 2025')
plt.grid()
plt.xlabel('Date')

ax1.plot(centers, city1['temperature_2m_mean (°C)'], color='red', label='Austin Temp (°C)', marker='o')
ax1.plot(centers, city2['temperature_2m_mean (°C)'], color='blue', label='NYC Temp (°C)', marker='o')
ax1.plot(centers, dflist, color='brown', label='Temp Difference (°C)', alpha=0.5, linewidth=2)
# -->
ax1.plot(centers, city1['temp_ma3'], color='red', linewidth=1.2, alpha=0.35, linestyle='-',zorder=2, solid_capstyle='round',label='Austin Temp—MA(3)')
ax1.plot(centers, city2['temp_ma3'], color='blue',linewidth=1.2, alpha=0.35, linestyle='-',zorder=2, solid_capstyle='round',label='NYC Temp—MA(3)')

ax1.set_ylabel('Temperature (Line)')
ax1.set_ylim(0, 40)
ax2 = ax1.twinx()
ax2.bar([i-barwid/2 for i in centers], auprec, color='orange', label='Austin Precip. (mm)', width=barwid, alpha=0.6)
ax2.bar([i+barwid/2 for i in centers], nyprec, color='cyan', label='NYC Precip. (mm)', width=barwid, alpha=0.6)
ax2.set_ylabel('Precipitation (Bar)')
ax2.set_ylim(0, 55)
plt.xticks([i for i in centers], days)
a_legend = ax1.legend(loc='upper left')
n_legend = ax2.legend(loc='upper right')
plt.show()
