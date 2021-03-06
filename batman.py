#!/usr/bin/env python3

# original: https://www.desmos.com/calculator/dnzfajfpym

import numpy as np
from matplotlib import pyplot as plt
from math import fabs,sqrt,fmod

# period = 28, amplitude = -3..+3
def batman(x):
  # top part
  x = fabs(x)
  x = fmod(fabs(x+14),28)-14
  x = fabs(x)
  if x < 0.5:
    return 2.25
  if x < 0.75:
    return 3*x+0.75
  if x < 1:
    return 9-8*x
  if x < 3:
    return 1.5-x/2-6*sqrt(10)/14*(sqrt(3-x*x+2*x)-2)
  if x < 7:
    return 3*sqrt(1-x*x/(7*7))
  # renormalize x for bottom part
  x = fmod(fabs(x+7),14)-7
  x = fabs(x)
  if x < 4:
    z = fabs(x-2)-1
    return x/2-(3*sqrt(33)-7)/112*x*x+sqrt(1-z*z)-3
  if x < 7:
    return -3*sqrt(1-x*x/(7*7))
  return 0


sampling_interval=0.05
fpath_xpts = np.arange(-21.0, 21.0+sampling_interval, sampling_interval)
fpath_ytop = np.array([batman(x)    for x in fpath_xpts])
fpath_ybot = np.array([batman(x+14) for x in fpath_xpts])
plt.plot(
      fpath_xpts, fpath_ytop, "r-",
      fpath_xpts, fpath_ybot, "b-"
)
plt.show()
    