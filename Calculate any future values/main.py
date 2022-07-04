# Python e data neye kaj korar jonno most popular holo pandas
# Ai code korar jono kicu modiul Install korte hbe r akta file lagbe jeta holo csb excel file.
# jekhane data thakbe( , )separeted
# Python mechine Larning..........................

"""
    1. pip install pandas  [Data Gulo Access er jonno ei library install]
    2. pip install -U scikit-learn  ----------   scikit-learn [Machine Learning in Python]
          Akhan theke import korte hobe .....
               from sklearn.linear_model import LinearRegression
"""

import pandas
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('iphone_price.csv')
model = LinearRegression()


model.fit(data[['version']], data[['price']])
x = int(input('Enter The Version = '))
output = model.predict([[x]])
for result in output:
    print('$',result)


