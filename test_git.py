import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

df = pd.read_csv("cardio_train.csv", sep=";")

X = df.iloc[ : , 1:-1]
y = df["cardio"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

kernel = 1.0 * RBF(1.0)
gpc = GaussianProcessClassifier(kernel = kernel, random_state = 778).fit(X_train, y_train)

y_pred = gpc.predict(X_test)