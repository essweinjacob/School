#CASE 1

p <- c(0.659, 0.689, 0.702, 0.703, 0.709, 0.713, 0.72, 0.72, 0.726, 0.726, 0.729, 0.731, 0.736, 0.737, 0.738, 0.738, 0.739, 0.743, 0.744, 0.745, 0.752, 0.752, 0.754, 0.764)
s <- c(0.687, 0.703, 0.709, 0.715, 0.721, 0.723, 0.723, 0.726, 0.728, 0.728, 0.728, 0.729, 0.73, 0.73, 0.733, 0.733, 0.735, 0.735, 0.736, 0.739, 0.741, 0.741, 0.741, 0.741, 0.743, 0.749, 0.751, 0.752, 0.752, 0.755, 0.756, 0.766, 0.767, 0.769, 0.77, 0.78)

#Ho: Perished and Survived groups are not different: u1 = u2
#Ha: Perished and Survived groups are different: u1 != u2

boxplot(p,s)
qqnorm(p)
qqnorm(s)

t.test(p,s)

#Summary of Statstical Findings: There is evidence to say that there is a difference between the mean humerous length of the survious and perished.
#Comparing our box plots, their means are reletivly the same but not exact, but also their data ranges are pretty different.
#Comparing the Q-Q Plots, their shapes are relativly the same, but their spreads are different.
#Using a two sample t-test, we see that the alternative hypothesis is true on a 95% confidence interval, and that the mean lenght is estimated to be between -0.217 inches and 0.002 inches greater then those that survived than those that perished.

#Scope of Interference: From our data, we learned that the survivors had larger humerus lengths on average then those that perished, however that does not mean we can assume that their longer humerous length is what caused them to survive, as their could have been countless other factors.
#The observation also tells us that the sparrows were gathered from a specific area. While this keeps data consistant, it would be bad to assume that this data would work on a global scale.

#CASE 2
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

#CASE 3
V<-c(170,290,-130,-70,-185,-220,200,290,270,200,300,-30,650,150,500,920,450,500,500,960,500,850,800,1090)
D<-c(0.021,0.099,0.134,0.205,0.255,0.325,0.475,0.550,0.600,0.730,0.800,1.000,1.050,1.100,1.200,1.300,1.475,1.600,1.800,1.800,1.900,1.950,2.000,2.000)

#We need to use a linear regression model to fit the data to check the big bang theory inrder to see whether at time 0 between the stars is 0
fit<-lm(D~V)
summary (fit)

# Assuming the big bang theory is correct, we want to try to fit the lienar model by forcing the intercept to be 0
fit<-lm(D~0+V)
summary(fit)
plot(fit)

#Summary of Statistical Findings:
# Our data is not consistent with the Big Bang Theory as proposed. Although the relationship between mean measured distance and velocity approximates a straight line, the value of the line at velocity zero is apparently not zero, as predicted by the theory.

#Scope of Interference
#These data are not random sample, so they do not represent what would result from tking measurements from other nebulae. These analysis assumes that there is an exact linear relationshop between distance and velocity, but the measured distancess do not fall exactly on a straight line because of measurements errors.