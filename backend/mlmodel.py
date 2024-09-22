import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from catboost import CatBoostRegressor
import joblib

print(f"Loading The AmesHousing Dataset")
data = pd.read_csv("AmesHousing.csv")
print(f"Collecting required columns based on high correlation")
required_columns = ['Overall Qual', 'Gr Liv Area', 'Garage Cars', 'Garage Area', 'Total Bsmt SF', 'SalePrice']
print(f"Converting them to dataframe")
df = data[required_columns]
print(f"Dropping the rows which contain null values")
df = df.dropna()
print(f"Splitting the features and label")
X = df.drop(columns=['SalePrice']) #features
y = df['SalePrice'] #label
print(f"Splitting the data to train data and validation data")
X_train,X_val,y_train,y_val = train_test_split(X,y,test_size=0.2,random_state=42)
print(f"Using CatBoostRegressor")
cbr = CatBoostRegressor()
print(f"Training the CatBoostRegressoR Model")
cbr.fit(X_train,y_train) #Calling fit method to train the model
y_predcbr = cbr.predict(X_val) #Predicting X_val
print(f"Finding R2 score, Mean Squared Error, Mean Absolute Error and Root Mean Squared Error")
r2cbr = r2_score(y_val,y_predcbr) #Obtaining r2 score
msecbr = mean_squared_error(y_val,y_predcbr) #Obtaining Mean Squared Error
maecbr = mean_absolute_error(y_val,y_predcbr) #Obtaining Mean Absolute Error
rmsecbr = np.sqrt(msecbr)
print("The R2 score is ",r2cbr)
print("The Mean Squared Error(mse) score is ",msecbr)
print("The Mean Absolute Error(mae) score is ", maecbr)
print("The Root Mean Squared Error(rmse) score is ", rmsecbr)


if __name__ == "__main__":
    joblib.dump(cbr, 'house_price_model.pkl')