import numpy as np
import matplotlib.pyplot as plt

# array = [3,4,5,1,1,2,1,2,3]
# array2= [1,2,1,3,1,2,1,1,1]
array = [1,2,1,2,1,1,1,1,2]
array2 = [1,2,1,3,4,1,5,1,2]
max = 6
intercept = 0
for j in range(len(array)-3):
    for i in range(j, j+3):
        intercept += (max - array[i])/2
        plt.plot([intercept, intercept + array[i]/4], [0, array2[i]], color='green')
        plt.plot([intercept + array[i]/4, intercept + (3 * array[i] / 4)], [array2[i], -1 * array2[i]], color='green')
        plt.plot([intercept + (3 * array[i] / 4), intercept + array[i]], [-1 * array2[i],0], color ='green')
        intercept += (max + array[i])/2
    plt.show(block=False)
    plt.pause(2)
    plt.close()

