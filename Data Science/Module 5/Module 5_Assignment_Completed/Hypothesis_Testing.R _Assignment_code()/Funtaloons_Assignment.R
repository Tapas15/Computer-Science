#Assignment module 5
# Fantaloon.csv

#importing csv file
fat <- read.csv(file.choose())
fat
View(fat)
# it is a catagorical data im just checking how it is numerically explained
attach(fat)
#numeric coversion as numeric
weekdays <-as.numeric( fat$Weekdays)
Weekend  <- as.numeric(fat$Weekend)

# prillminaryEDA data analysis by numeric value
library("lattice")
# Dot plot
dotplot(fat$Weekdays)
dotplot(fat$Weekend)
#hist
hist(weekdays)
hist(Weekend)

library(moments)
skewness(weekdays)
skewness(Weekend)

# Normality check
qqnorm(weekdays)
qqline(Weekdays)

qqnorm(weekdays)
qqline(Weekend)

library(UsingR)

densityplot(weekdays)
DensityPlot(weekdays)

densityplot(Weekend)
DensityPlot(Weekend)

#Histogram with probablity check
hist(weekdays,probability = TRUE)
line(density(weekdays))
line(density(weekdays,adjust = 2))

hist(Weekend,probability = TRUE)
line(density(Weekend))
line(density(Weekend,adjust = 2))

#scatter plot

plot(weekdays,Weekend,main = "Scatter plot",col = "red",col.main = "blue",pch = 20,xlab = "Male",ylab = "Female")

# boxplot
boxplot(weekdays)
boxplot(weekdays,horizontal = TRUE,col ="Red")

boxplot(Weekend)
boxplot(Weekend,horizontal = TRUE,col = "Green")

#normality test

shapiro.test(weekdays)
shapiro.test(Weekend)

#Variance test

var.test(weekdays,Weekend)

# T test
t.test(weekdays,Weekend,alternative = "two.sided",conf.level = 0.95)
t.test(weekdays,Weekend,alternative = "greater",var.equal = T)
t.test(weekdays,Weekend,alternative = "less",var.equal = T)

#Importing data for further data processing 
Fanta <- read.csv(file.choose(),stringsAsFactors = F,na.strings = c("","NA"))
View(Fanta)
dim(Fanta) # 425 rows and 2 columns data
nrow(Fanta)
ncol(Fanta)
#week days gender view
head(Fanta,10)
tail(Fanta,10)
# NA value view
sum(is.na(Fanta)==T) # it implies that there is 50 NA  value exists
sum(is.na(Fanta$Weekdays))
sum(is.na(Fanta$Weekend))
levels(Fanta)

is.na(Fanta) # checking if NA value is preent or not 
# now omit row which is NA value 
fanta <- na.omit(Fanta) # Na Value ommited now data is clean

View(fanta)
#colnames(fanta) = c("x","y")
names(fanta)
attach(fanta)
dotplot(x)
dotplot(y)
sum(is.na(fanta)) # there is no missing value 
# convert as factor to later get numeric value 
fanta$Weekdays <- as.factor(fanta$Weekdays)
fanta$Weekend  <- as.factor(fanta$Weekend)


#Now convert to numeric
fanta$Weekdays <- as.numeric(fanta$Weekdays)
fanta$Weekend <- as.numeric(fanta$Weekend)  
View(fanta)
#normality test
shapiro.test(fanta$Weekdays)
shapiro.test(fanta$Weekend)
#Variance test
var.test(fanta$Weekdays,fanta$Weekend)
# T test
t.test(fanta$Weekdays,fanta$Weekend,alternative = "two.sided",conf.level = 0.95)
t.test(fanta$Weekdays,fanta$Weekend,alternative = "greater",var.equal = T)
t.test(fanta$Weekdays,fanta$Weekend,alternative = "less",var.equal = T)
