import pandas as pd
import numpy as np
import copy
import matplotlib as mpl

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt


path = 'C:\\Users\\s-jallemann\\Documents\\GitHub\\cs-664-ai-project1\\yoeki\\'

durations1 = open(path + 'durations_1.txt', "r")
durations1 = durations1.read().split("\n")

durations2 = open(path + 'durations_2.txt', "r")
durations2 = durations2.read().split("\n")

data = pd.DataFrame(durations1)
data['1']  = durations2

#df.rename(columns = {'y':'year'})
data = data.rename(columns = {0:'brute','1':'minarray'})

test = copy.deepcopy(data)
test['bruteslice'] = pd.to_numeric(test.brute.str.slice(start = 5), downcast = 'float')
test['minarrayslice'] = pd.to_numeric(test.minarray.str.slice(start = 5), downcast = 'float')

plotframe = copy.deepcopy(test)
plotframe = plotframe.drop(columns=['brute','minarray'])[0:-1]

#plotframe.boxplot(column = ['bruteslice','minarrayslice'],widths=0.05)

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(plotframe)

plt.show()

