import matplotlib.pyplot as plt
ax = plt.axes()
ax.arrow(1,2, 5,5 , head_width=0.5, head_length=0.5)
plt.ylim(0,10)
plt.xlim(0,10)
plt.show()