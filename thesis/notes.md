## mpl settings

import matplotlib as mpl
mpl.rcParams.update({'axes.labelsize': 16})
mpl.rcParams.update({'figure.figsize': (12,12)})
mpl.rcParams.update({'axes.facecolor': "white"})


## statsmodels

R-squared is the measurement of how much of the independent variable is explained by changes in our dependent variables.

The adjusted R-squared penalizes the R-squared formula based on the number of variables, therefore a lower adjusted score may be telling you some variables are not contributing to your model’s R-squared properly.

Prob (F-Statistic) uses this number to tell you the accuracy of the null hypothesis, or **whether it is accurate that your variables’ effect is 0**.

**lower p(F-stat) means less likely your group of variables is 0**

Our std error is an estimate of the standard deviation of the coefficient, a measurement of the amount of variation in the coefficient throughout its data points. The t is related and is a measurement of the precision with which the coefficient was measured. A low std error compared to a high coefficient produces a high t statistic, which signifies a high significance for your coefficient.

P>|t| is one of the most important statistics in the summary. It uses the t statistic to produce the p value, a measurement of **how likely your coefficient is measured through our model by chance**. The p value of 0.378 for Wealth is saying there is a 37.8% chance the Wealth variable has no affect on the dependent variable, Lottery, and our results are produced by chance. Proper model analysis will compare the p value to a previously established alpha value, or a threshold with which we can apply significance to our coefficient. A common alpha is 0.05, which few of our variables pass in this instance.

**lower p(t-stat) means less likely the effects of this variable is random chance**

Omnibus describes the normalcy of the distribution of our residuals using skew and kurtosis as measurements. A 0 would indicate perfect normalcy. Prob(Omnibus) is a statistical test measuring the probability the residuals are normally distributed. A 1 would indicate perfectly normal distribution.


## table 

\begin{table}
    \begin{center}
        \caption{}\label{}
        \begin{tabular*}{}
            \hline
            
        \end{tabular*}
    \end{center}
\end{table}

## cref

\cpageref
\cpagerefrange
