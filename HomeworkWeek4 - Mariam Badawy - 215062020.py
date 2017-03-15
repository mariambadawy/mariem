# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 10:20:47 2017

@author: mariambadawy
"""

import nsfg
import thinkplot
import thinkstats2

pres = nsfg.ReadFemResp()

#Q1:
    
fmar1age = pres['fmar1age']
histogram1 = thinkstats2.Hist(fmar1age)
pres.fmar1age.value_counts().sort_index()
thinkplot.Hist(histogram1, color='Violet',width=0.75,label="Ages Frequency") 
thinkplot.Show(xlabel='Ages at First Marriage', ylabel='Frequency')


#Q2:
    
fmarno = pres['fmarno']
histogram2 = thinkstats2.Hist(fmarno)
pres.fmarno.value_counts().sort_index()

thinkplot.Hist(histogram2, color='Violet',width=0.75,label="Marriages Number")
thinkplot.Show(xlabel='Marriages Number', ylabel='Frequency Number')

#Q3:
    
totincr = pres['totincr']
histogram3 = thinkstats2.Hist(totincr)
pres.totincr.value_counts().sort_index()

thinkplot.Hist(histogram3, color='Violet',width=0.75,label="Total Income") 
thinkplot.Config(xlabel='Range', ylabel='Frequency')
thinkplot.Show()

#Q4:
    
neverMarried = pres[pres.fmarno == 0]
married = pres[pres.fmarno >= 1]
histogram4 = thinkstats2.Hist(neverMarried.totincr, label="Never Married")
histogram5 = thinkstats2.Hist(married.totincr, label="Married")
thinkplot.Hist(histogram4, align='right',width=0.5,color='Violet')
thinkplot.Hist(histogram5, align='left',width=0.5,color='Pink')
thinkplot.Show(xlabel='Time', ylabel='Amount',)

#Q5:

print 'The miminum value of the total income of the never married respondants is %.2f' %neverMarried.totincr.min()
print 'The miminum value of the total income of the married respondants is %.2f' %married.totincr.min()
print 'The maximum value of the total income of the never married respondants is %.2f' %neverMarried.totincr.max()
print 'The maximum value of the total income of the married respondants is %.2f' %married.totincr.max()
print 'The standard deviation of the total income of the never married respondants is %.2f' %neverMarried.totincr.std()
print 'The standard deviation of the total income of the married respondants is %.2f' %married.totincr.std()
print 'The variance of the total income of the never married respondants is %.2f' %neverMarried.totincr.var()
print 'The variance of the total income of the married respondants is %.2f' %married.totincr.var()
print 'The mean of the total income of the never married respondants is %.2f' %neverMarried.totincr.mean()
print 'The mean of the total income of the married respondants is %.2f' %married.totincr.mean()