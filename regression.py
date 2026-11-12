from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans

# Regression
X = [[1], [2], [3], [4]]
y = [100, 200, 300, 400]

model = LinearRegression()
model.fit(X, y)
print("Electricity Consumption:", model.predict([[5]]))

# Classification
X = [[10], [20], [80], [90]]
y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)
print("Product Status:", model.predict([[85]]))

# Clustering
X = [[10, 20], [12, 22], [80, 90], [82, 92]]

model = KMeans(n_clusters=2, random_state=0, n_init=10)
model.fit(X)
print("Machine Groups:", model.labels_)
