# Exploratory data annalysis 
#Asignment 5 Hyoothesis

library(readxl)
cur <- read.csv(file.choose())
cur
View(cur)

rm(x)
rm(y)

library("lattice")
cur

attach(cur)
#dot chart
dotchart(x)
dotchart(y)

#DOTplot()
dotplot(Unit.A)
dotplot(Unit.B)

#barplot
barplot(Unit.A)
barplot(Unit.B)

barchart(Unit.A)
barchart(Unit.B)
?barchart

#boxplot
boxplot(Unit.A)

x <- boxplot(Unit.A)
x 

y <- boxplot(Unit.B)
y
View(Unit.B)

# boxplot 

boxplot(Unit.A,horizontal = TRUE,col = "green")
boxplot(Unit.B,horizontal = TRUE,col = "red")

hist(Unit.A,col = "blue")
hist(Unit.B,col = "yellow")

#Normality check
qqnorm(Unit.A)
qqline(Unit.A)

qqnorm(Unit.B)
qqline(Unit.B)

#Transform
qqnorm(log(Unit.A))
qqline(log(Unit.A))


#Scattar plot
plot(Unit.A,Unit.B,main = "Scatter plot",col ="blue"
     ,col.main = "red",col.lab ="green",xlab ="Hero",ylab ="Heroin",pch =20)


# Normality test shapiro test
shapiro.test(Unit.A)
shapiro.test(Unit.B)

#Variance test 
var.test(Unit.A,Unit.B)

# 2 Shamplt test
t.test(Unit.A,Unit.B,alternative = "two.sided",conf.level = 0.95)

