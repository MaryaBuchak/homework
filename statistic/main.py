import pandas
from scipy import stats
import matplotlib.pyplot as plt

data = []
f = open("data.txt", 'r')
for i in range(50):
    data.append(float(f.readline()))
f.close()

df = pandas.DataFrame(data={
    'experements': data
})
df.to_csv("Experiments.csv")

df.plot(kind='bar', xlabel='Number of measure ', ylabel='Temperature, °C', title='Data')
df.plot.kde(xlabel='Number of measure ', title='Data')

print(stats.kstest(data, 'norm', (df.mean(), df.std()), N=len(data)))

plt.show()