import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np


#---- this part is about data and how are going to feed the model ---#
 #In the code below there might be some comments of commands that i used to visualize some outputs and will not effect the project behaviour#
        
teams=pd.read_csv("teams.csv")
teams=teams[["athletes","age" ,"prev_medals","medals","year","team"]]
#sns.lmplot(x="athletes",y="medals",data=teams,fit_reg=True,ci=None)
teams.plot.hist(y="medals")
#plt.show()
#print(teams[teams.isnull().any(axis=1)])
teams=teams.dropna()
train=teams[teams["year"]<2012].copy()
test=teams[teams["year"]>=2012].copy()


#---- this part is about training the model ----#

reg = LinearRegression() #the linear regression model 
predictors = ["athletes","prev_medals"]
target="medals"

reg.fit(train[predictors],train["medals"])
LinearRegression()

predictions = reg.predict(test[predictors])
test["predictions"] = predictions
test.loc[test["predictions"] <0 , "predictions"] = 0 
test["predictions"] = test["predictions"].round()

error=mean_absolute_error(test["medals"], test["predictions"])
#test[test["team"] == "USA"]

errors = (test["medals"] -test["predictions"]).abs()
errors_by_team = errors.groupby(test["team"]).mean()
#print (errors_by_team)
medals_by_team = test["medals"].groupby(test["team"]).mean()
error_ratio= errors_by_team/medals_by_team


error_ratio= error_ratio[~pd.isnull (error_ratio)]
error_ratio= error_ratio[np.isfinite(error_ratio)]
error_ratio.plot.hist()
print(error_ratio.sort_values())


#plt.show()

































