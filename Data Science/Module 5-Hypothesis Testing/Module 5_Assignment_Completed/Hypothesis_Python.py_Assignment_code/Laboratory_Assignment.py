#Assignmernt module no 5 labTaT.csv
import pandas as pd
#impporting file to read
lab = pd.read_csv("D:\\R and python practice\\Module 5\\Assignment\\Datasets (7)\\LabTAT.csv")
""" Data Pre Processing """  #data.frame is lab
lab.info() # to seestructure , dimentions , informations 
len(lab) # for number of rows
len(lab.columns) # for columns
lab.shape # The shape number of rows and columns
lab.size    # total size of data each elements rows adn columns
lab.all() # data type of data frame
lab.all(axis= 'columns') # checking bool value of each column each true or false 
lab.all(axis= None) # cehcking all columns has false value exist or not is true means not exist 
lab.dtypes # 
lab.iloc[50] # the location of  the row and column
lab.head(10) # first head 10 items
lab.tail(10) # first tail 10 items
lab.describe() # it is to describ3e summary
# From above we caame to know there is some missing value and are all numerice data
#changing column name
lab.columns = "Laboratory_1" ,"Laboratory_2" , "Laboratory_3" , "Laboratory_4" 
lab

""" Exploratory Data Annalyis Visualizations before cleaning"""
#Using Histogram from panda data frame univariate annalysis
lab['Laboratory_1'].hist(bins=50) # plotted histogram
lab['Laboratory_2'].hist(bins=50)
lab['Laboratory_3'].hist(bins=50) # plotted histogram
lab['Laboratory_4'].hist(bins=50)



#Matplot library
import matplotlib.pyplot as plt
""" Histogram Bi-plot annalys of datas  prelim """
fig =plt.figure(figsize=(8,4))  # histogram to visualize data to see
ax1 =fig.add_subplot(121) # it looks like unit b value is more as compared to a
ax1.set_xlabel("Laboratory_1")
ax1.set_ylabel("Laboratory_2")
ax1.set_xlabel("Laboratory_3")
ax1.set_ylabel("Laboratory_4")
ax1.set_title("Two plot Difference 1")
lab.plot(kind="hist")
#ploting line and learning about the data  
ax = plt.gca()
lab.plot(kind='line',x ='Laboratory_1',y ='Laboratory_2',ax=ax)
plt.show()

ax = plt.gca()
lab.plot(kind='line',x ='Laboratory_2',y ='Laboratory_3',ax=ax)
plt.show()

ax = plt.gca()
lab.plot(kind='line',x ='Laboratory_3',y ='Laboratory_4',ax=ax)
plt.show()

ax = plt.gca()
lab.plot(kind='line',x ='Laboratory_4',y ='Laboratory_1',ax=ax)
plt.show()

#plt.gca(projection='polar')
#help(plt.gca)

""" Data Warangling Missing value searchingin column search"""
lab.apply(lambda x: sum(x.isnull()),axis=0) # number of value missing in column
#fillinng
lab["Laboratory_1"].fillna(lab["Laboratory_1"].mean(),inplace =True) # replace missing value with mean
lab["Laboratory_2"].fillna(lab["Laboratory_2"].mean(),inplace =True) # replace missing value with mean
lab["Laboratory_3"].fillna(lab["Laboratory_3"].mean(),inplace =True) # replace missing value with mean
lab["Laboratory_4"].fillna(lab["Laboratory_4"].mean(),inplace =True) # replace missing value with mean

lab.apply(lambda x: sum(x.isnull()),axis=0) # checking columns for missing value A is cleaned

import statistics # to do statistics calculational part
#cut.columns = "x","y"
statistics.mean(lab.Laboratory_1) # we found mean it means the value replaced by mean 
statistics.mean(lab.Laboratory_2) # we found mean it means the value replaced by mean 
statistics.mean(lab.Laboratory_3) # we found mean it means the value replaced by mean 
statistics.mean(lab.Laboratory_4) # we found mean it means the value replaced by mean 

# lets check all columns value 
lab.apply(lambda x: sum(x.isnull()),axis = 0) # it says that unit b is still 16 NA value 
lab["Laboratory_1"].fillna(lab["Laboratory_2"].mean(),inplace = True) # we filled mean in free place
lab["Laboratory_3"].fillna(lab["Laboratory_4"].mean(),inplace = True)
lab.apply(lambda x: sum(x.isnull()),axis =0) # now both column replaced with mean
# Data cleaning process finished

#type of data checking dealing with Unimodal value 
lab.dtypes # data type is float
lab.mean() # whole data mean not returning NaN
#mode
lab.Laboratory_1.mode()
lab.Laboratory_2.mode()
lab.Laboratory_3.mode()
lab.Laboratory_4.mode()

#median value 
lab.Laboratory_1.median()
lab.Laboratory_2.median()
lab.Laboratory_3.median()
lab.Laboratory_4.median()

""" EDA After Cleaning data Uni-Variate Annalysis"""
#Histogram plot
plt.hist(lab.Laboratory_1)
plt.hist(lab.Laboratory_2)
plt.hist(lab.Laboratory_3)
plt.hist(lab.Laboratory_4)

#Boxplot
plt.boxplot(lab.Laboratory_1) # outliers
plt.boxplot(lab.Laboratory_2) # outliers
plt.boxplot(lab.Laboratory_3) # outliers
plt.boxplot(lab.Laboratory_4) # outliers

help(lab.boxplot) # checking additional meaning, if we treat outliers data may imbalance 
#boxplt dat Horizental
plt.boxplot(lab.Laboratory_1,vert=False) 
plt.boxplot(lab.Laboratory_2,vert=False) 
plt.boxplot(lab.Laboratory_3,vert=False) 
plt.boxplot(lab.Laboratory_4,vert=False) 

""" EDA bi-Variate Annalysis Scattar plot """    
# Scattar plot to see the data scatterness and outliers 
plt.scatter(x = lab.Laboratory_1, y = lab.Laboratory_2) # now scatter plot is made
plt.scatter(x = lab.Laboratory_2, y = lab.Laboratory_3) # now scatter plot is made
plt.scatter(x = lab.Laboratory_3, y = lab.Laboratory_4) # now scatter plot is made
plt.scatter(x = lab.Laboratory_4, y = lab.Laboratory_1) # now scatter plot is made

# to treat outliers either we have to remove row or column 
# we need to check that out liver is meaning full and not significantlly changing the data meaning
""" Our Data is clean lests do the further processing"""
import scipy.stats as stats
import pylab

# checking normality using line qqline ,qqplot of disttribution of data 
stats.probplot(lab.Laboratory_1,dist ="norm",plot = pylab) # as we can see the normalcy blue dotted point lies
stats.probplot(lab.Laboratory_2,dist ="norm",plot = pylab) # as we can see the normalcy blue dotted point lies
stats.probplot(lab.Laboratory_3,dist ="norm",plot = pylab) # as we can see the normalcy blue dotted point lies
stats.probplot(lab.Laboratory_4,dist ="norm",plot = pylab) # as we can see the normalcy blue dotted point lies
#Now Data Normality check  shapiro test each 4 sample

print(stats.shapiro(lab.Laboratory_1)) # Shapiro test after cleaning
print(stats.shapiro(lab.Laboratory_2)) # Shapiro test after cleaning
print(stats.shapiro(lab.Laboratory_3)) # Shapiro test after cleaning
print(stats.shapiro(lab.Laboratory_4)) # Shapiro test after cleaning
help(stats.shapiro)
""" Tesging Bi-Variate annalysis Sample test"""
#test for equal variances but here 4 samples are given 
import scipy
scipy.stats.levene(lab.Laboratory_1,lab.Laboratory_2) # it implies that there is no Difference
scipy.stats.levene(lab.Laboratory_2,lab.Laboratory_3) # it implies that there is no Difference
scipy.stats.levene(lab.Laboratory_3,lab.Laboratory_4) # it implies that there is no Difference
scipy.stats.levene(lab.Laboratory_4,lab.Laboratory_1) # it implies that there is no Difference

# 2 sample test t test
scipy.stats.ttest_ind(lab.Laboratory_1,lab.Laboratory_2) # PValue is higher Null accepted
scipy.stats.ttest_ind(lab.Laboratory_2,lab.Laboratory_3) # PValue is higher Null accepted
scipy.stats.ttest_ind(lab.Laboratory_3,lab.Laboratory_4) # PValue is higher Null accepted
scipy.stats.ttest_ind(lab.Laboratory_4,lab.Laboratory_1) # PValue is higher Null accepted

# Annalysis of Variance 
""" Testing Multivariate annalysis One way anova this is test demands"""































