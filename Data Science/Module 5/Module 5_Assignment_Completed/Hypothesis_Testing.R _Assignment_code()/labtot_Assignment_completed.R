# Assignment module 5 
#labTaT


# importing file
lab <- read.csv(file.choose())
lab
View(lab)
attach(lab)
# Univariate Annalysis with graph
#dotchart
dotchart(Laboratory.1)
dotchart(Laboratory.2)
dotchart(Laboratory.3)
dotchart(Laboratory.4)


#barplot
barplot(Laboratory.1)
barplot(Laboratory.2)
barplot(Laboratory.3)
barplot(Laboratory.4)

#boxplot
a <- boxplot(Laboratory.1)
a
b <- boxplot(Laboratory.2)
b
c <- boxplot(Laboratory.3)
c
d <- boxplot(Laboratory.4)
d
#histogram
hist(Laboratory.1,col = 'red')
hist(Laboratory.2,col = 'green')
hist(Laboratory.3,col='yellow')
hist(Laboratory.4,col = 'purple')

#Normality test using 
qqnorm(Laboratory.1)
qqline(Laboratory.1)

qqnorm(Laboratory.2)
qqline(Laboratory.2)

qqnorm(Laboratory.3)
qqline(Laboratory.3)

qqnorm(Laboratory.4)
qqline(Laboratory.4)

#Scatter plot

plot(Laboratory.1,Laboratory.2,main = "Scatter plot",col = "red", col.lab ="purple" ,pch =20 )
plot(Laboratory.3,Laboratory.4,main = "Scatter plot",col ="yellow",col.lab ="blue",pch = 20)

#data preprocessig #checking mean , NA exists
mean(lab$Laboratory.1)
mean(lab$Laboratory.2)
mean(Laboratory.3)
mean(Laboratory.4)
View(lab)
#dimention checking
dim(lab) # 141 rows and 4 columns
#checking first 10 head
head(lab,10)
#checking Tail
tail(lab,10)
#cloumn names
names(lab)
#structure
str(lab) # data frame
summary(lab) # present summary of data
#decting NA values by eash column by matrix view method
lab$Laboratory.1
lab$Laboratory.2
lab$Laboratory.3
lab$Laboratory.4
sum(is.na(lab)==T) # total 84 value missing 
sum(is.na(lab)==T)/length(lab)# length of row is 21 
# hence missing figure 21*4 = 84
#Tracing missing value by each column
sum(is.na(Laboratory.1)==T) # each column is true
sum(is.na(Laboratory.2)==T)
sum(is.na(Laboratory.3)==T)
sum(is.na(Laboratory.4)==T)
#checking length of each are same ,it is also percentage representation
sum(is.na(Laboratory.1)==T)/length(Laboratory.1)
sum(is.na(Laboratory.2)==T)/length(Laboratory.2)
sum(is.na(Laboratory.3)==T)/length(Laboratory.3)
sum(is.na(Laboratory.4)==T)/length(Laboratory.4)


#detecting missing value by percentage, 14% value is missing 
sapply(lab, function(lab)
  {
  sum(is.na(lab)==T)/length(lab)
  }
)
# Now visually representing missing numerical value Amelia
#install.packages("Amelia")
library("Amelia")
missmap(lab,main = "LabTAT") # in the graph below 15% is missing value
#AmeliaView() # to view using data file
# Now removing missing NA value
sum(is.na(lab)==T) # total value 
#removing from each column
lab$Laboratory.1[is.na(lab$Laboratory.1)] <- mean(Laboratory.1,na.rm = T) 
sum(is.na(lab$Laboratory.1)==T) 
lab$Laboratory.2[is.na(lab$Laboratory.2)] <- mean(Laboratory.2,na.rm = T) 
sum(is.na(lab$Laboratory.2)==T) 
lab$Laboratory.3[is.na(lab$Laboratory.3)] <- mean(Laboratory.3,na.rm = T) 
sum(is.na(lab$Laboratory.3)==T) 
lab$Laboratory.4[is.na(lab$Laboratory.4)] <- mean(Laboratory.4,na.rm = T) 
sum(is.na(lab$Laboratory.4)==T) 

View(lab)
mean(lab$Laboratory.1) # now mean is woriking means data is clean after attach
View(lab)

# test for normality shapiro test
shapiro.test(Laboratory.1)
shapiro.test(Laboratory.2)
shapiro.test(Laboratory.3)
shapiro.test(Laboratory.4)

#Variance  test
var.test(Laboratory.1,Laboratory.2)
var.test(Laboratory.2,Laboratory.3)
var.test(Laboratory.3,Laboratory.4)
var.test(Laboratory.4,Laboratory.1)

# 5% signigicance test at different laboratory 
t.test(Laboratory.1,Laboratory.2,alternative = "two.sided",conf.level = 0.95)
t.test(Laboratory.2,Laboratory.3,alternative = "two.sided",conf.level = 0.95)
t.test(Laboratory.3,Laboratory.4,alternative = "two.sided",conf.level = 0.95)
t.test(Laboratory.4,Laboratory.1,alternative = "two.sided",conf.level = 0.95)

# checking missing value met or not 
sum(is.na(lab)==T) # there is no NA value Congralulations
# now lets see ploting
plot(Laboratory.1,Laboratory.2) # means just to checking without affecting missing value replaced

sta <- stack(lab)
sta

plot(values~ind,data =sta) # to see the difference between various sample mean
write.csv(sta, file="final.csv")
getwd()
anova_result <- aov(values~ind,data = sta)
anova_result
summary(anova_result)
