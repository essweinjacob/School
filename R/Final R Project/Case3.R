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