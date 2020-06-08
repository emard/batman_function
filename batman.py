#!/usr/bin/env python3

# original: https://www.desmos.com/calculator/dnzfajfpym

def batman_top(x):
  if fabs(x) <= 4:
    return fabs(x/2)-(3*sqrt(33)-7)/112*x**2+sqrt(1-(fabs(fabs(x)-2)-1)**2)-3
  if fabs(x) <= 7:
    return -3*sqrt(-(x/7)**2+1)
  return 0

def batman_bot(x):
  if fabs(x) <= 0.5:
    return 2.25
  if fabs(x) <= 0.75:
    return 3*fabs(x)+0.75
  if fabs(x) <= 1:
    return 9-8*fabs(x)
  if fabs(x) <= 3:
    return 1.5-fabs(x/2)-6*sqrt(10)/14*(sqrt(3-x**2+2*fabs(x))-2)
  if fabs(x) <= 7:
    return 3*sqrt(1-(x/7)**2)
  return 0

import numpy as np
from matplotlib import pyplot as plt
from math import fabs,sqrt
sampling_interval=0.1
fpath_xpts = np.arange(-7.0, 7.0+sampling_interval, sampling_interval)
fpath_ytop = np.array([batman_top(x) for x in fpath_xpts])
fpath_ybot = np.array([batman_bot(x) for x in fpath_xpts])
plt.plot(
      fpath_xpts, fpath_ytop, "r-",
      fpath_xpts, fpath_ybot, "b-"
)
plt.show()
    