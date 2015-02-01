import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansdata = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv') #read in the Lending Club Data as a csv, store in loansdata
loansdata.dropna(inplace=True) #drop the missing data

loansdata.boxplot(column = 'Amount.Requested') #create a boxplot
plt.title('Lending Club Data: Amount Requested Boxplot')
plt.savefig("amountrequestedboxplot.png") #save the graph

plt.figure()#resets the graph
loansdata.hist(column = 'Amount.Requested') #create a histogram of the data
plt.title('Lending Club Data: Amount Requested Histogram')
plt.savefig("amountrequestedhistogram.png") #save the histogram

plt.figure() #resets the graph
graph = stats.probplot(loansdata['Amount.Requested'], dist = 'norm', plot=plt)#create the QQ graph, checking it against normal distribution
plt.title('Lending Club Data: Amount Requested QQ Plot')
plt.savefig("amountrequestedQQplot.png") #save the QQ plot

