#Assignment module 5 
import pandas as pd # importing data  from panda data frame 
cof = pd.read_csv("D:\\R and python practice\\Module 5\\Assignment\\Datasets (7)\\CustomerOrderform.csv")
# data pre processing annalysis 
""" its a catagorical data """
cof.info()
len(cof) # for number of rows
len(cof.columns) # for columns
cof.shape # The shape number of rows and columns
cof.size    # total size of data each elements rows adn columns
cof.all() # data type of data frame
cof.all(axis= 'columns') # checking bool value of each column each true or false 
cof.all(axis= None) # cehcking all columns has false value exist or not is true means not exist 
cof.dtypes # 
cof.iloc[50] # the location of  the row and column
cof.head(10) # first head 10 items
cof.tail(10) # first tail 10 items
cof.describe() # it is to describ3e summary

""" Data pre processing and cleaning begins """

cof.isnull() # checking for missing values 
cof.isnull().sum()
cof.values 
cof = cof.dropna() # it will work only for column to do
cof.dropna(axis=1)
cof = cof.dropna(how ='all')
cof
cof.describe() # now no Nan value exists 
""" Data Prepared for further Anaalysis"""

mystack1 = []
mystack1.append(cof['Phillippines'])
mystack1.append(cof['Indonesia'])
mystack1.append(cof['Malta'])
mystack1.append(cof['India'])
mystack1
#mystack1.pop() Use it to remove stack value 
""" Stacking Complete"""

""" Anova can happen as it is 4 catagorical data  """

# Annalysis of Variance 
""" Testing Multivariate annalysis One way anova this is test demands"""
""" Since 4 sample are there we will do One way anova"""" 
#lab.columns
#import numpy as np
#import statsmodels.formula.api as sm
#import statsmodels.regression.linear_model as sm
import statsmodels.api as sm
from statsmodels.formula.api import ols

import statsmodels.api as sm
import statsmodels.formula.api as smf
mod = ols('cof.Phillippines~cof.Indonesia+cof.Malta+cof.India',data = cof).fit()

aov_table = sm.stats.anova_lm(mod, type=2) # anova ols model may not be working for catagorical data 
help(sm.stats.anova_lm) # New methodology to find out 
print(aov_table) 
print(cof.info())
print(cof.describe())
#summary(aov_table) /// later will find out 

""" Trying to find out but without stacking it wont help"""
from statsmodels.formula.api import ols
import scipy.stats as stats
"""
count=pd.crosstab(mystack[0],mystack[1])
count
Chisquares_results1=scipy.stats.chi2_contingency(count)
Chi_square1=[['','Test Statistic','p-value'],['Sample Data',Chisquares_results[0],Chisquares_results[1]]]
"""
""" preprocessign data annalysis of catagorical data By using R """
""" Successfully worked out by converting Value by R but Na value exist"""
# Since i do not know manipulative data catagorical data i will import clean data from R
# i will leann Data Waranglaing ,cleaning in Python verysoon 
cof1 = pd.read_csv("D:\\R and python practice\\Module 5\\Assignment\\cof.csv")
cof1.info()
len(cof) # for number of rows
len(cof1.columns) # for columns
cof1.shape # The shape number of rows and columns
cof1.size    # total size of data each elements rows adn columns
cof1.all() # data type of data frame
cof1.all(axis= 'columns') # checking bool value of each column each true or false 
cof1.all(axis= None) # cehcking all columns has false value exist or not is true means not exist 
cof1.dtypes # 
cof1.iloc[50] # the location of  the row and column
cof1.head(10) # first head 10 items
cof1.tail(10) # first tail 10 items
cof1.describe() # it is to describ3e summary

mystack =[]
mystack.append(cof1['values'])
mystack.append(cof1['ind'])

mystack
import scipy

count=pd.crosstab(mystack[0],mystack[1])
count
Chisquares_results=scipy.stats.chi2_contingency(count)
Chi_square=[['','Test Statistic','p-value'],['Sample Data',Chisquares_results[0],Chisquares_results[1]]]

#mystack.pop() # to remove addition object type

# there is also stack method is manually you can do but i have no idea
""" Data wasd not numeric so plotting was not possible for now 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks", color_codes=True)
tips = sns.load_dataset("tips")
sns.catplot(x="day", y="time", data=tips);

#lab = str(lab)
#a = str(cof.Malta)
#plt.hist(a.Malta)

i will work out fot ploting catagorical data later time 
"""


""" i have tried r instalation to use but it s nor working """

"""
import rpy2
print(rpy2.__version__)

import rpy2.situation
for row in rpy2.situation.iter_info():
    print(row)
rpy2.robjects()
"""