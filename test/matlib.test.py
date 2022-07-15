import numpy as np
import matplotlib.pyplot as plt
import math
import os




# r1 = np.arange(0.001, 4, 0.01)
# theta1 = math.radians(60)*(r1/r1)

# r2 = np.arange(0.001, 6, 0.01)
# theta2 = math.radians(120)*(r2/r2)

# fig, ax = plt.subplots(1,3,subplot_kw={'projection': 'polar'})

# ax[0].plot(theta1, r1)
# ax[1].plot(theta2, r2)


# for i in range(3):
#     ax[i].set_rmax(10)
#     ax[i].set_rticks(np.arange(1, 10, 1))  # Less radial ticks
#     ax[i].set_rlabel_position(-22.5)  # Move radial labels away from plotted line
#     ax[i].grid(True)


mng = plt.get_current_fig_manager()
mng.frame.Maximize(True)
mng.show()