from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import pandas as pd
import os


class SalePredictor:
    def __init__(self,_xcols,_ycol):
        self.model = Pipeline([
            ("onehot", OneHotEncoder()),  
            ("linear", LinearRegression())
        ])
        self.xcols = _xcols
        self.ycol = _ycol

    def fit(self, train):
        self.model.fit(train[self.xcols], train[self.ycol])

    def predict(self, test):
        print(self.model.predict(test[self.xcols]))

    def score(self, train_x, train_y, test_x, test_y):
        pass
