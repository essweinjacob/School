#Ho: True difference is equal to zero: u1 = u2
#Ha: True difference is not equal to zero: u1 > u2

b<-c(1,1,1,3)
a<-c(rep(0,17),1,1,2)

qqplot(b,a)

#Looking at our qqplot, we see that it does not resemble a normal curve at all so we should use a wilcox test

wilcox.test(b,a)

#Error message given saying the wilcox test cannot compute an exact p-value so we should try using a different test using a permuatation test.

library("RVAideMemoire", lib.loc="~/R/win-library/3.5")

b<-c(1,1,1,3)
a<-c(rep(0,17),1,1,2)

perm.t.test(b,a,alternative=c("greater"),progress=FALSE)

#Summary of Statistical Findings:
#  According to our t-test, we can say that their is substantial evidence that the number of O-ring incidents was related to the launch temps.

#Scope of Interferece:
#  The observational data cannot be used to establish casuality, nor is there any broader population of which they are a sample, but the association between temperature and O-ring fauure on these particular 24 lauches is consistant with the theory that lower temperatures impair the function of the O-rings.

