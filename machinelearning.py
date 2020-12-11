import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

#Taken from https://bit.ly/2JiJSdn

df = pd.read_csv("test5.csv")

y = df['value']
X = df.drop(['Date','value','AOD1','STD3'], axis=1)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=1234)

X_train.shape, y_train.shape

X_test.shape, y_test.shape

X.columns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# Create linear regression object
regr = LinearRegression()
# Train the model using the training sets
regr.fit(X_train, y_train)
# Make predictions using the testing set
lin_pred = regr.predict(X_test)
linear_regression_score = regr.score(X_test, y_test)

from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# Create MLPRegressor object
mlp = MLPRegressor()
# Train the model using the training sets
mlp.fit(X_train, y_train)
# Score the model
neural_network_regression_score = mlp.score(X_test, y_test)
# Make predictions using the testing set
nnr_pred = mlp.predict(X_test)

from sklearn.linear_model import Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)
# Score the model
lasso_score = lasso.score(X_test, y_test)
# Make predictions using the testing set
lasso_pred = lasso.predict(X_test)

from sklearn.linear_model import ElasticNet
elasticnet = ElasticNet()
elasticnet.fit(X_train, y_train)
elasticnet_score = elasticnet.score(X_test, y_test)
elasticnet_pred = elasticnet.predict(X_test)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# Create Random Forrest Regressor object
regr_rf = RandomForestRegressor(n_estimators=200, random_state=1234)
# Train the model using the training sets
regr_rf.fit(X_train, y_train)
# Score the model
decision_forest_score = regr_rf.score(X_test, y_test)
# Make predictions using the testing set
regr_rf_pred = regr_rf.predict(X_test)

from sklearn.ensemble import ExtraTreesRegressor
extra_tree = ExtraTreesRegressor(n_estimators=200, random_state=1234)
extra_tree.fit(X_train, y_train)
extratree_score = extra_tree.score(X_test, y_test)
extratree_pred = extra_tree.predict(X_test)

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Create Decision Tree Regressor object
tree_1 = DecisionTreeRegressor()

tree_2 = AdaBoostRegressor(DecisionTreeRegressor(), n_estimators=200, learning_rate=.1)

# Train the model using the training sets
tree_1.fit(X_train, y_train)
tree_2.fit(X_train, y_train)

# Score the decision tree model
tree_1.score(X_test, y_test)

# Score the boosted decision tree model
boosted_tree_score = tree_2.score(X_test, y_test)

# Make predictions using the testing set
tree_1_pred = tree_1.predict(X_test)
tree_2_pred = tree_2.predict(X_test)

from xgboost.sklearn import XGBRegressor
#Fitting XGB regressor 
xboost = XGBRegressor(n_estimators=200)
xboost.fit(X_train, y_train)
xgb_score = xboost.score(X_test, y_test)
xboost_pred = xboost.predict(X_test)

print("\n")
print("Scores:")
print("Linear regression score: ", linear_regression_score)
print("Neural network regression score: ", neural_network_regression_score)
print("Lasso regression score: ", lasso_score)
print("ElasticNet regression score: ", elasticnet_score)
print("Decision forest score: ", decision_forest_score)
print("Extra Trees score: ", extratree_score)
print("Boosted decision tree score: ", boosted_tree_score)
print("XGBoost score:", xgb_score)
print("\n")
print("RMSE:")
print("Linear regression RMSE: %.2f"
      % sqrt(mean_squared_error(y_test, lin_pred)))
print("Neural network RMSE: %.2f"
      % sqrt(mean_squared_error(y_test, nnr_pred)))
print("Lasso RMSE: %.2f"
      % sqrt(mean_squared_error(y_test, lasso_pred)))
print("ElasticNet RMSE: %.2f"
      % sqrt(mean_squared_error(y_test, elasticnet_pred)))
print("Decision forest RMSE: %.2f"
      % sqrt(mean_squared_error(y_test, regr_rf_pred)))
print("Extra Trees RMSE: %.2f"
      % sqrt(mean_squared_error(y_test, extratree_pred)))
print("Boosted decision tree RMSE: %.2f"
      % sqrt(mean_squared_error(y_test, tree_2_pred)))
print("XGBoost RMSE: %.2f"
      % sqrt(mean_squared_error(y_test, xboost_pred)))

plt.style.use('ggplot')
plt.rcParams["figure.figsize"] = [16,9]
plt.scatter(y_test, regr_rf_pred)
plt.xlabel('Measured')
plt.ylabel('Predicted')
plt.title('Decision Forest Predicted vs Actual')
plt.show()

