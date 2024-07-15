raw_midwest = pd.read_csv('data/midwest.csv')
raw_midwest.head()
raw_midwest.tail()
raw_midwest.shape
raw_midwest.info()
raw_midwest.describe()

new_midwest = raw_midwest.copy()
new_midwest = new_midwest.rename(columns = {'poptotal' : 'total'})
new_midwest = new_midwest.rename(columns = {'popasian' : 'asian'})
new_midwest.head()

import matplotlib.pyplot as plt
plt.clf()
new_midwest['asian_total'] = new_midwest['asian'] / new_midwest['total'] * 100
new_midwest['asian_total'].plot.hist(rot=0)
plt.show()

import numpy as np
asian_total_mean = sum(new_midwest['asian_total']) / len(new_midwest)
new_midwest['grade'] = np.where(new_midwest['asian_total']>asian_total_mean, 'large', 'small')

my_series = new_midwest['grade'].value_counts()
plt.clf()
my_series.plot.bar(rot=0)
plt.show()
