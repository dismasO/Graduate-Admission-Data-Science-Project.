##DATA VISUALIZATION

##PACKAGES
import pandas as pd
import numpy as np, matplotlib.pyplot as plt, seaborn as sns
data = pd.read_csv('Graduate Admission Data.csv', sep=',')

##Basic info about the data

data.head(10)
data.info()
data = data.drop(['Serial No.'], axis=1)

#Renaming the columns for ease of manipulation.
data = data.rename(columns={'GRE Score':'GRE', 'TOEFL Score':'TOEFL','University Rating':'UniR','Chance of Admit ':'CoA'})

#Heatmap to show the relations between the variables.
sns.heatmap(data.corr(), annot=True)
plt.title('Heatmap of the data.')
plt.show() #See the interpretation section for graphs.

#Visualizing the Research feature
data.Research.value_counts()
y_Research = np.array([len(data[data.Research==0]),len(data[data.Research==1])])
x_Research = ['No Research','Done Research']
sns.barplot(x_Research, y_Research)
plt.title('Bargraph on Research')
plt.ylable('Frequency')
plt.show()

#Visualizing with scatterplots
#CGPA for GRE Score
plt.scatter(data.GRE, data.CGPA)
plt.title('Scatterplot: CGPA for GRE Score')
plt.show()
#CGPA for University Ratings
plt.scatter(data.UniR, data.CGPA)
plt.title('Scatterplot: CGPA scores for University Ratings')
plt.show()

#Visualizing with Histogram
data.GRE.plot(kind='hist', bins=200, figsize=(6,6))
plt.title('Histogram: GRE Scores')
plt.ylabel('Frequency')
plt.show()

subset = data[data.CoA >=0.75]['UniR'].value_counts()
subset.plot(kind='bar', figsize=(20,10))
plt.title('University Ratings of Candidates with 75% acceptance chance.')
plt.xlabel('University Ratings')
plt.ylabel('Frequency')
plt.show()
