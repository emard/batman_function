#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
length=10
sampling_interval=0.2
fpath_xpts = np.arange(0.0, length, sampling_interval)
fpath_ytop = fpath_xpts
fpath_ybot = fpath_xpts
plt.plot(
      fpath_xpts, 1000*fpath_ytop, "b-",
      fpath_xpts,-1000*fpath_ybot, "r-"
)
plt.ylabel('mm blue:true red:rover')
plt.show()
    