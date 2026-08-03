import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def encode_categorical_features(X):

    categorical_columns = X.select_dtypes(include='object').columns

    X_encoded = pd.get_dummies(X , columns= categorical_columns , dtype= int)

    return X_encoded


def data_splitting(X_encoded , y , test_size= 0.2):

    x_train , x_test , y_train , y_test = train_test_split(X_encoded , y , test_size= test_size , random_state= 48 , shuffle= True)

    return x_train , x_test , y_train , y_test


def scale_features(x_train , x_test):

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(x_train)

    X_test_scaled = scaler.transform(x_test)

    return X_train_scaled, X_test_scaled 


