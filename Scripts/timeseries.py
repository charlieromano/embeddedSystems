import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import deterministicTrends as tr

filename = '../Datasets/Portugal.1995.2021.csv'
filename_2 = '../Datasets/Spain.1995.2021.csv'

column_name = 'Name'
value_name = 'Electronics'
x_name = 'Year'
y_name = 'Current Gross Export'

ncolors = 21
cmap = plt.get_cmap('nipy_spectral')
colors = cmap(np.linspace(0,1,ncolors))

df = pd.read_csv(filename)
df2= pd.read_csv(filename_2)

dt = df[df[column_name]==value_name][[x_name, y_name]]
dt[y_name]=dt[y_name].str.replace('[$B]', '', regex=True).astype(float)

dt2 = df2[df2[column_name]==value_name][[x_name, y_name]]
dt2[y_name]=dt2[y_name].str.replace('[$B]', '', regex=True).astype(float)

# Series

plt.plot(dt[x_name],dt[y_name])
plt.plot(dt2[x_name],dt2[y_name])
plt.show()


x, y = dt[x_name],dt[y_name]
popt, _ = curve_fit(tr.objective_linear, x,y)
a,b = popt
x_line = range(min(x), max(x),1)
y1_line = tr.objective_linear(x_line, a, b)
x, y = dt2[x_name],dt2[y_name]

x2, y2 = dt2[x_name],dt2[y_name]
popt2, _2 = curve_fit(tr.objective_linear, x2,y2)
a2,b2 = popt2
x_line2 = range(min(x2), max(x2),1)
y2_line = tr.objective_linear(x_line2, a2, b2)
x2, y2 = dt2[x_name],dt2[y_name]

# Linear regressions

plt.scatter(dt[x_name],dt[y_name])
plt.scatter(dt2[x_name],dt2[y_name])
plt.plot(x_line, y1_line, '--',)
plt.plot(x_line2, y2_line, '--',)
plt.show()

# Series - trends

y1 = dt[y_name].values
y2 = dt2[y_name].values
x  = dt2[x_name].values

y1_flat = y1[1:] - y1_line
y2_flat = y2[1:] - y2_line

y1_flat_mean = np.mean(y1_flat)
y2_flat_mean = np.mean(y2_flat)

plt.subplot(1,2,1)
plt.plot(x_line, y1_flat, color=colors[2])
plt.axhline(y1_flat_mean, color=colors[2], linestyle='--')
plt.subplot(1,2,2)
plt.plot(x_line2, y2_flat, color=colors[5])
plt.axhline(y2_flat_mean, color=colors[5], linestyle='--')
plt.show()

# Tests
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

adfuller(y1)
kpss(y1)

adfuller(y1_flat)
kpss(y1_flat)

# Autocorrelations

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.graphics import tsaplots as tsa

_lags = 10

y1=dt[y_name].values
y2=dt2[y_name].values
x=dt2[x_name].values

fig, ax = plt.subplots(2,2)

tsa.plot_acf(y1, lags=_lags, ax=ax[0,0])
tsa.plot_pacf(y1, lags=_lags, ax=ax[0,1])

tsa.plot_acf(y2, lags=_lags, ax=ax[1,0])
tsa.plot_pacf(y2, lags=_lags, ax=ax[1,1])

plt.show()

# Cross-correlations

import statsmodels.api as sm

R = sm.tsa.stattools.ccf(y1, y2, 
                         adjusted=True, 
                         fft=True, 
                         nlags=None, 
                         alpha=None)
plt.subplot(1,2,1)
plt.plot(x,y1)  
plt.plot(x,y2)
plt.plot(x,R)
plt.grid()

y1_norm = (y1-min(y1))/(max(y1)-min(y1))
y2_norm = (y2-min(y2))/(max(y2)-min(y2))
R_norm = sm.tsa.stattools.ccf(y1_norm, y2_norm, adjusted=False)

plt.subplot(1,2,2)
plt.plot(x,y1_norm)  
plt.plot(x,y2_norm)
plt.plot(x,R_norm)
plt.grid()
plt.show()

