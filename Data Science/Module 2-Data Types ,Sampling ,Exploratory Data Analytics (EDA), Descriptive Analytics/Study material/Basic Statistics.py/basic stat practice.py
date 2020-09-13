# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:08:07 2020

@author: Home
"""

" Basic stat practice for exploratory data annalysis " 
2+2

#pyrhon  library packages
# pip install <packages name>
#pip install pandas

import pandas as pd

""" Read data intp python"""

education = pd.read_csv("D:/R and python practice/Module 2/Data Sets (1)/education.csv")

#ecploratory data annalysis

#Measures of central tendency /fiirst moemtn of business]

education.datasrno.mean()
education.workex.mean()
education.gmat.mean()

education.datasrno.median()
education.workex.median()
education.gmat.median()

education.datasrno.mode()
education.workex.mode()
education.gmat.mode()

from scipy import stats
stats.mode(education.datasrno)
stats.mode(education.workex)
stats.mode(education.gmat)

#second order business descision #measues of Dispersion
education.datasrno.var()
education.workex.var()
education.gmat.var()

#standard davitation 
education.datasrno.std()
education.workex.std()
education.gmat.std()

#range
ranged = max(education.datasrno) - min(education.datasrno)
ranged

rangew = max(education.workex) - min(education.workex)
rangew

rangeg = max(education.gmat) - min(education.gmat)
rangeg
# third moment business descision
education.datasrno.skew()
education.workex.skew()
education.gmat.skew()

#fourth moment business descision
education.datasrno.kurt()
education.workex.kurt()
education.gmat.kurt()

#Graphical Representaion
import matplotlib.pyplot as plt
import numpy as np

plt.bar(height = education.datasrno, x = np.arange(1,744,1))
plt.bar(height = education.workex, x = np.arange(1,744,1))
plt.bar(height = education.gmat, x = np.arange(1,744,1))


# lets make histogram

plt.hist(education.datasrno)
plt.hist(education.workex)
plt.hist(education.gmat)

#lets make box plt
plt.boxplot(education.datasrno)
plt.boxplot(education.workex)
plt.boxplot(education.gmat)

#NOrmal distrubution check            
import scipy.stats as stats
import pylab

# data normally distrbibuted or naot check
stats.probplot(education.datasrno,dist = "norm",plot =pylab)
stats.probplot(education.workex,dist = "norm",plot =pylab)
stats.probplot(education.gmat , dist = "norm",plot = pylab)

#transform
import numpy as np
stats.probplot(np.log(education.datasrno),dist ="norm",plot =pylab)
stats.probplot(np.log(education.workex),dist = "norm",plot =pylab)
stats.probplot(np.log(education.gmat),dist ="norm",plot =pylab)

#z diatrubution practice
stats.norm.cdf(740,711,29)

#ppf percent point function
stats.norm.ppf(0.975,0,1)

# t distrubution
stats.t.cdf(1.98,139)
stats.t.ppf(0.975,139)

help(stats.t.ppf)
