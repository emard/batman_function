#!/usr/bin/env python3

# original: https://www.desmos.com/calculator/dnzfajfpym

def batman_top(x):
  if x > -4 and x < 4:
    return fabs(x/2)-(3*sqrt(33)-7)/112*x**2+sqrt(1-(fabs(fabs(x)-2)-1)**2)-3
  return 0

def batman_bot(x):
  return 0

import numpy as np
from matplotlib import pyplot as plt
from math import fabs,sqrt
sampling_interval=0.2
fpath_xpts = np.arange(-7.0, 7.0, sampling_interval)
#fpath_ytop = np.array([fabs(x/2)-(3*sqrt(33)-112)/7*x**2+sqrt(1-(fabs(fabs(x)-2)-1)**2)-3 for x in fpath_xpts])
fpath_ytop = np.array([batman_top(x) for x in fpath_xpts])
fpath_ybot = np.array([batman_bot(x) for x in fpath_xpts])
plt.plot(
      fpath_xpts, fpath_ytop, "r-",
      fpath_xpts, fpath_ybot, "b-"
)
plt.ylabel('mm blue:true red:rover')
plt.show()
    