import pandas
import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('cleaned.csv')
data.describe()
data["revenue"] = data["Gross"] - data["Budget"]
#data.describe()

X = DataFrame(data = data.Gross)
y = DataFrame(data = data.Budget)

regression = LinearRegression()
regression.fit(X,y)

x0 =int(X.min())
xm = int(X.max() + 100000000)

y0 = int(y.min())
ym = int(y.max()+ 100000000)

regression = LinearRegression()
regression.fit(X,y)

plt.figure(figsize=(10, 6))
plt.xlim([x0,xm])
plt.ylim([y0,ym])
plt.scatter(X,y, alpha=0.3)

plt.plot(X, regression.predict(X), color="red")

plt.xlabel('Revenue')
plt.ylabel('Budget')
plt.title("film cost vs revenue")
plt.show()

R2= regression.score(X,y) # gbt uns R²
print(R2)
