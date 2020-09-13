# Assignment model no 5  Cutlet.csv
import pandas as pd 

#impporting file to read
cut = pd.read_csv("D:\\R and python practice\\Module 5\\Assignment\\Datasets (7)\\Cutlets.csv")
""" Data Pre Processing """
cut # df , dataframe
cut.info() # to seestructure , dimentions , informations 
len(cut) # for number of rows
len(cut.columns) # for columns
cut.shape # The shape number of rows and columns
cut.size    # total size of data each elements rows adn columns
cut.all() # data type of data frame
cut.all(axis= 'columns') # checking bool value of each column each true or false 
cut.all(axis= None) # cehcking all columns has false value exist or not is true means not exist 
cut.dtypes # 
cut.iloc[50] # the location of  the row and column
cut.head(10) # first head 10 items
cut.tail(10) # first tail 10 items
cut.describe() # it is to describ3e summary

""" Exploratory Data Annalyis Visualizations"""
#Using Histogram from panda data frame
cut['Unit A'].hist(bins=50) # plotted histogram
cut['Unit B'].hist(bins=50)
#Matplot library
import matplotlib.pyplot as plt
 """ Histogram Bi-plot annalys prelim """
fig =plt.figure(figsize=(8,4))  # histogram to visualize data to see
ax1 =fig.add_subplot(121) # it looks like unit b value is more as compared to a
ax1.set_xlabel("Unit_A")
ax1.set_ylabel("Unit_B")
ax1.set_title("Cutlet")
cut.plot(kind="hist")

#changing column name
cut.columns = "Unit_A","Unit_B" 
cut
#ploting line and seeing about data 
ax = plt.gca()
cut.plot(kind='line',x ='Unit_A',y ='Unit_B',ax=ax)
plt.show()

""" Data Warangling Missing value searchingin column search"""
cut.apply(lambda x: sum(x.isnull()),axis=0) # number of value missing in column
#fillinng
cut["Unit_A"].fillna(cut["Unit_A"].mean(),inplace =True) # replace missing value with mean
cut.apply(lambda x: sum(x.isnull()),axis=0) # checking columns for missing value A is cleaned
import statistics # to do statistics calculational part
#cut.columns = "x","y"
statistics.mean(cut.Unit_A) # we found mean it means the value replaced by mean 
statistics.mean(cut.Unit_B)  # we found value nan means value mean is not replaced
# lets check all columns value 
cut.apply(lambda x: sum(x.isnull()),axis = 0) # it says that unit b is still 16 NA value 
cut["Unit_B"].fillna(cut["Unit_B"].mean(),inplace = True) # we filled mean in free place
cut.apply(lambda x: sum(x.isnull()),axis =0) # now both column replaced with mean
# Data cleaning process finished

#type of data checking dealing with
cut.dtypes # data type is float
cut.mean() # whole data mean not returning NaN

""" EDA After Cleaning data Uni-Variate Annalysis"""
#Histogram plot
plt.hist(cut.Unit_A)
plt.hist(cut.Unit_B)
#Boxplot
plt.boxplot(cut.Unit_A) # outliers
help(cut.boxplot) # checking additional meaning, if we treat outliers data may imbalance 
plt.boxplot(cut.Unit_B) # two outliers 
#boxplt dat Horizental
plt.boxplot(cut.Unit_A,vert=False) 
plt.boxplot(cut.Unit_B,vert=False)
""" EDA bi-Variate Annalysis Scattar plot """    
# Scattar plot to see the data scatterness and outliers 
plt.scatter(x = cut.Unit_A, y = cut.Unit_B) # now scatter plot is made

# to treat outliers either we have to remove row or column 
# we need to check that out liver is meaning full and not significantlly changing the data meaning
""" Our Data is clean lests do the further processing"""
# Nrmality check qqplot, qqline

import scipy.stats as stats
import pylab

# checking normality using line qqline ,qqplot of disttribution of data 
stats.probplot(cut.Unit_A,dist ="norm",plot = pylab) # as we can see the normalcy blue dotted point lies
stats.probplot(cut.Unit_B,dist ="norm",plot =pylab,rvalue =True) # we can see dat normality 

#Now Data Normality check  shapiro test

print(stats.shapiro(cut.Unit_A)) # Shapiro test after cleaning
print(stats.shapiro(cut.Unit_B)) # shapiro test after cleaning
help(stats.shapiro)

#test for equal variances 
import scipy
scipy.stats.levene(cut.Unit_A,cut.Unit_B) # it implies that there is no Difference
# 2 sample test t test
scipy.stats.ttest_ind(cut.Unit_A,cut.Unit_B) # PValue is higher Null accepted





