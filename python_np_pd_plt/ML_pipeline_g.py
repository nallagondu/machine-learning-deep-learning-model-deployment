import numpy as np
import pandas as pd


training_data = pd.read_csv('storepurchasedata.csv')
training_data.describe()

X = training_data.iloc[:,:-1].values

Y = training_data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.20,random_state=0)