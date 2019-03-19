import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

diabetesTrainingData = pd.read_csv("diabetesTraining.csv")
print(diabetesTrainingData.head(10))
print("Data size ", diabetesTrainingData.shape)
print(list(diabetesTrainingData.columns))
print("total data rows = " +str(len(diabetesTrainingData.index)))


diabetesTestdata =pd.read_csv("diabetesTest.csv")
print(diabetesTestdata.head(10))
print("total data rows = " +str(len(diabetesTestdata.index)))

'''*******Plot differnt kinds of graphs for the data'''
'''sns.countplot(x="Outcome", hue="Age" , data=diabetesTestdata)
diabetesTrainingData["Age"].plot.hist()
diabetesTestdata["BloodPressure"].plot.hist()
plt.ylabel('age') 
plt.show() '''

'''*******show if there are any columns null in training and test data '''
'''print(diabetesTestdata.isnull().sum())
print(diabetesTrainingData.isnull().sum()) '''



'''*******create the logisitic regression model with the training data'''

x=diabetesTrainingData.drop("Outcome", axis=1)
y= diabetesTrainingData["Outcome"]
from sklearn.linear_model import LogisticRegression
logmodel =LogisticRegression()
logmodel.fit(x,y)
print ("Log model Score=", logmodel.score(x,y))


'''x_test =diabetesTestdata.drop("Outcome",axis=1)'''
x_test =diabetesTestdata.drop("Outcome", axis=1)
y_test =diabetesTestdata["Outcome"]



results = logmodel.predict_proba(x_test)

print (results)

'''predicted_probs = logmodel.predict(x_test)
from sklearn.metrics import classification_report
print (classification_report (y_test,predicted_probs))

help(logmodel)


predictions = logmodel.predict(x)

from sklearn.metrics import classification_report

print (classification_report (y,predictions))


from sklearn.metrics import confusion_matrix

print (confusion_matrix (y, predictions))'''