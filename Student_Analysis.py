#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#reading the data
df = pd.read_csv('Expanded_data_with_more_features.csv')

#dropping unnamed column
df = df.drop('Unnamed: 0', axis = 1)

#change weeklystudyhours column 
df['WklyStudyHours'] = df['WklyStudyHours'].str.replace('05-Oct','5-10')

#For gender distribution
plt.figure(figsize=(6,6))
ax = sns.countplot(data = df, x = "Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()
#from above chart, we have analyzed that:
#the no. of females is more than the no. of males

#To see parent education impact on students score👇🏻
gb = df.groupby("ParentEduc").agg({"MathScore": "mean", "ReadingScore": "mean", "WritingScore": "mean"})
print(gb)
#plotting heat map for the same
plt.figure(figsize=(15,6))
sns.heatmap(gb, annot = True, cmap = 'viridis')
plt.title("Parent Education Impact on Students Score")
plt.show()
#From above chart, we have analyzed that:
#The education of the parents has a significant impact on the scores of the students

#To see parent marital status impact on the students score👇🏻
gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore": "mean", "ReadingScore": "mean", "WritingScore": "mean"})
print(gb1)
#plotting heat map for the same
plt.figure(figsize=(6,6))
sns.heatmap(gb1, annot = True, cmap = 'viridis')
plt.title("Parent Marital Status Impact on Students Score")
plt.show()
#From the above chart, we have analyzed that:
#The marital status of the parents has a negligible impact on the scores of the students

#To detect extreme values in mathscore👇🏻
sns.boxplot(data = df, x = "MathScore")
plt.show()

#To detect extreme values in reading score👇🏻
sns.boxplot(data = df, x = "ReadingScore")
plt.show()

#To detect extreme values in writing score👇🏻
sns.boxplot(data = df, x = "WritingScore")
plt.show()


#Ethnic Group Unique Values👇🏻
print(df["EthnicGroup"].unique())

#Ethinic Group Distribution👇🏻
#Creating a pie chart to get count
groupA = df.loc[(df['EthnicGroup'] == 'group A')].count()
groupB = df.loc[(df['EthnicGroup'] == 'group B')].count()
groupC = df.loc[(df['EthnicGroup'] == 'group C')].count()
groupD = df.loc[(df['EthnicGroup'] == 'group D')].count()
groupE = df.loc[(df['EthnicGroup'] == 'group E')].count()

mlist = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]
plt.pie(mlist, labels = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E'], autopct='%1.1f%%')
plt.title("Ethnic Group Distribution")
plt.show()