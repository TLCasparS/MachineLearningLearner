import pandas
import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame



data = pandas.read_csv("cleaned.csv")
data = pandas.read_csv('cleaned.csv')
data.describe()

data["revenue"] = data["Gross"] - data["Budget"]
#data.describe()

x = DataFrame(data = data.Gross)
y = DataFrame(data = data.Budget)

x0 =int(x.min())
xm = int(x.max() + 100000000)

y0 = int(y.min())
ym = int(y.max()+ 100000000)


plt.figure(figsize=(10, 6))
plt.xlim([x0,xm])
plt.ylim([y0,ym])
plt.scatter(x,y, alpha=0.3)
plt.xlabel('Revenue')
plt.ylabel('Budget')
plt.title("film cost vs revenue")
plt.show()
