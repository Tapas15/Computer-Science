# Assignment  Fantaloon.csv
# import files 
import pandas as pd

fan = pd.read_csv("D:\\R and python practice\\Module 5\\Assignment\\Datasets (7)\\Fantaloons.csv")
""" Data Pre Processing """
fan # df , dataframe
fan.info() # to seestructure , dimentions , informations 
len(fan) # for number of rows
len(fan.columns) # for columns
fan.shape # The shape number of rows and columns
fan.size    # total size of data each elements rows adn columns
fan.all() # data type of data frame
fan.all(axis= 'columns') # checking bool value of each column each true or false 
fan.all(axis= None) # cehcking all columns has false value exist or not is true means not exist 
fan.dtypes # 
fan.iloc[50] # the location of  the row and column
fan.head(10) # first head 10 items
fan.tail(10) # first tail 10 items
fan.describe() # it is to describ3e summary
""" Checking and removing null value and rows """
fan.isnull() # checking for missing values 
fan.isnull().sum()
fan.values 
fan.dropna() # it will work only for column to do
fan.dropna(axis=1)
fan =  fan.dropna(how ='all')
fan

mystack1 = []
mystack1.append(fan['Weekdays'])
mystack1.append(fan['Weekend'])

mystack1
#mystack1.pop() to remove 
""" Stacking Complete"""

import scipy.stats as stats
count=pd.crosstab(mystack1[0],mystack1[1])
count
Chisquares_results1=scipy.stats.chi2_contingency(count)
Chi_square1=[['','Test Statistic','p-value'],['Sample Data',Chisquares_results[0],Chisquares_results[1]]]







""" Data pre processing of R stacked data it has problem it is not removing Nan value """
""" As we can we Nan value exist in catagorical data"""
""" i will learn how to deal with catagorical data very soon"""
# Now i will import clean stack value for futher annalysis 
# the data i am importing it from R  stacked data and clean data
fan1 = pd.read_csv("D:\\R and python practice\\Module 5\\Assignment\\fan.csv")
fan1 # df , dataframe
fan1.info() # to seestructure , dimentions , informations 
len(fan1) # for number of rows
len(fan1.columns) # for columns
fan1.shape # The shape number of rows and columns
fan1.size    # total size of data each elements rows adn columns
fan1.all() # data type of data frame
fan1.all(axis= 'columns') # checking bool value of each column each true or false 
fan1.all(axis= None) # cehcking all columns has false value exist or not is true means not exist 
fan1.dtypes # 
fan1.iloc[50] # the location of  the row and column
fan1.head(10) # first head 10 items
fan1.tail(10) # first tail 10 items
fan1.describe() # it is to describ3e summary

""" Data Warangling Missing value searchingin column search"""
fan1.isnull() # checking for missing values 
fan1.isnull().sum()
fan1.values 
fan1.dropna() # it will work only for column to do
fan1.dropna(axis=1)
fan1= fan1.dropna(how ='all')
fan1
mystack =[]
mystack.append(fan1['values'])
mystack.append(fan1['ind'])

mystack
import scipy
import scipy.stats as stats
count=pd.crosstab(mystack[0],mystack[1])
count
Chisquares_results=scipy.stats.chi2_contingency(count)
Chi_square=[['','Test Statistic','p-value'],['Sample Data',Chisquares_results[0],Chisquares_results[1]]]

#mystack.pop() # to remove addition object type


 