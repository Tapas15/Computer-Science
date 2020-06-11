#Assignemnt 5 
# firat read r to load data without using any funcion import data method

cof <- readr::read_csv(file.choose())

View(cof)
#attach(cof)
#data preprocessing 
sum(is.na(cof)==T) # 60 na value exists 
head(cof) # head ,tail view
tail(cof) 
dim(cof) # number of row and columns

# made stacked data 
cof_stack <- stack(cof)
View(cof_stack)
sum(is.na(cof_stack)==T) # after stack 60 na value exists
#before data NA value removed chiaquare and table value
table(cof_stack$values,cof_stack$ind) 

chisq.test(table(cof_stack$values,cof_stack$ind))

##################################################################################
#removing NA from stack data 
v <- table(cof_stack$values,useNA = "always")
cof_stack$values <- v
#stack value sum Na = 0
sum(is.na(cof_stack$values)==T)
sum(is.na(cof_stack$ind)==T)


View(cof_stack)
sum(is.na(cof_stack)==T) # now stack data has no na value

#before data NA value removed chiaquare and table value
table(cof_stack$values,cof_stack$ind)

chisq.test(table(cof_stack$values,cof_stack$ind))

head(cof_stack)
tail(cof_stack)
