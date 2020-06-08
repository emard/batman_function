#!/usr/bin/env python3

# original: https://www.desmos.com/calculator/dnzfajfpym

import numpy as np
from matplotlib import pyplot as plt
import math
sampling_interval=0.2
fpath_xpts = np.arange(-7.0, 7.0, sampling_interval)
fpath_ytop = np.array([math.fabs(x/2) for x in fpath_xpts])
fpath_ybot = fpath_xpts
plt.plot(
      fpath_xpts, 1000*fpath_ytop, "r-",
      fpath_xpts,-1000*fpath_ybot, "b-"
)
plt.ylabel('mm blue:true red:rover')
plt.show()
    