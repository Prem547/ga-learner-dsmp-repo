# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df = pd.read_csv(path)
print(df.shape)
print(df.head(5))

X = df.loc[:, df.columns != 'list_price']
y = df.iloc[:,1].values
print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)
# code ends here
#data.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns


# --------------
import matplotlib.pyplot as plt

# code starts here        
cols = (X_train.columns)
print(cols.shape)
#print(cols)
fig, axes = plt.subplots(3,3, figsize=(20,10))

for i in range(0,3):
    for j in range(0,3):
        col = cols[i*3+j]
        axes[i,j].scatter(X_train[col],y_train)
        plt.show()
# code ends here



# --------------
# Code starts here
corr = X_train.corr().abs()
high_corr_var=np.where(corr>0.8)



high_corr_var=[(corr.columns[X_train],corr.columns[y_train]) for X_train,y_train in zip(*high_corr_var) if X_train!=y_train and X_train<y_train]

print(high_corr_var)




X_train.drop(['play_star_rating','val_star_rating'], 1 ,inplace=True)
X_test.drop(['play_star_rating','val_star_rating'], 1 ,inplace=True)

# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor = LinearRegression()

regressor.fit(X_train, y_train)
print(regressor)

y_pred = regressor.predict(X_test)
print(y_pred)

mse = mean_squared_error(y_test,y_pred) 
print(mse)

r2 = r2_score(y_test,y_pred)
print(r2)
# Code ends here


# --------------
# Code starts here
residual = y_test - y_pred
#print(residual)

plt.hist(y_test, bins = 8)
plt.xlabel("y_test - y_pred")
plt.ylabel("residual")
plt.show()

# Code ends here


