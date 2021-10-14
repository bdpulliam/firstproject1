import math as m
import numpy as np

#Problem 2.1
#How much does Bill have after 10 years with 5% interest?
dep1=1000
int1=0.05
time1=10 
wealth1 = "${:,.2f}".format(np.round(dep1*(1+int1)**time1,2))
print ("2.1: Bill's total wealth is", wealth1 + ".")

#Problem 2.2
#How long does it take Bill to double his money?
double = np.round(m.log10(2)/m.log10((1+int1)),2)
print ("2.3: It takes Bill",double, "years to double his money.")

#Problem 2.3
#Does Jack double his money in 6 years?
dep2 = 1000
int2 = 0.2
time2 = 6
wealth2 = dep2*(1+int2)**time2

if wealth2 > 2 * dep2:
    print("2.3: True")
else:
    print("2.3: False")
    
#Problem 2.4
#Create list of amounts saved in Savings account
Savings = ['Bill', 1000, 'Jack', 5000, 'Amy', 6700, 'Cindy', 5699, 'Harry', 6700]
print("2.4:", Savings)

#PRoblem 2.5
#Create Dictionary called "Account"
Accounts = {'Bill': 1000, 'Jack': 5000, 'Amy': 6700, 'Cindy': 5699, 'Harry': 6700}
print ("2.5:", Accounts)

#Problem 2.6
#Create List of tuples
savingstuple=('(Bill, 1000),' '(Jack, 5000),' '(Amy, 6700),' '(Cindy, 5699),' '(Harry, 6700)')
print("2.6:", savingstuple)

#Problem 2.7
#Differences among lists, sets and dictionaries
print ("2.7:", 'A list is a collection of ordered data. ' \
       'A touple is also a collection of ordered data. ' \
       'A set is an unordered collection of data. ' \
       'A dictionary is a an unordered collection of data that stores that data ' \
       'in key-value pairs.')

