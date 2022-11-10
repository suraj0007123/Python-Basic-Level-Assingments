import collections
list1=[5,6,1.25,8.35,'suraj',7+9j,True,False]
list2=[4,3,2.50,3.75,'manasa',7+8j,True,False]
list3=list1+list2
print(list3)
print("Original List : ",list3)
ctr = collections.Counter(list3)
print("Frequency of the elements in the List : ",ctr)
list3.reverse()
print('Reversed List:', list3)


set1={1,2,3,4,5,6,7,8,9,10}
set2={5,6,7,8,9,10,11,12,13,14,15}
print("set1 intersection set2 : ",
      set(set1).intersection(set(set2)))
set_difference=set1-set2
print(set_difference)
set_difference=set2-set1
print(set_difference)

dict1={'Maharashtra':7867391,'Andhra Pradesh':2318176,'Delhi':1860887,'Gujarat':1223034,'Kerala':6506655}
dict1.keys()
dict1.update({'Tamil Nadu':3450333})
print(dict1)

x=399
y=543
z=12345
x/3
y/3
z/3


a=5
b=3
c=10

a/=b
a
c*=5
c

R="Data Science"
s=R.find("S")
print(s)
4**3


age1=5
5age=55


age_1=100
age@1=100


s="Suraj"
print(s)
del(s)
print(s)


age=29
if age < 10:
    print("Children")
elif age > 60:
    print("senior citizen")
else:
    print("normal citizen")
    
 
ticketPrice=600
gender='male'
age=62
if gender =="male":
    if age>=60:
        print(0.7*ticketPrice)
    else:
        print(ticketPrice)
elif gender =="female":
    if age>=60:
        print(0.5*ticketPrice)
    else:
        print(0.7*ticketPrice)
        
        
num=1025        
if num>0 and num%5==0:
    print('num is divisible by 5 and positive num')
else:
    print('num is not divisible by 5 and negative num')


list1=[1,5.5,(10+20j),'data science']
for i in (list1):
    print(i)
        
    

list1=[0,1,2,3,4,5,6,7,8,9]
list2=['zero','one','two','three','four','five','six','seven','eight','nine']
dict_from_list = dict(zip(list2, list1))
print(dict_from_list)

l=[3,4,5,6,7,8]
l2=[i+10 for i in l if i%2==0]    
print(l2)
l1=[i*5 for i in l if i%2!=0]    
print(l1)

def greet(name):  
    print ('Hello ', name)
greet('naveen good morning') 
greet('how are you')

import pandas as pd
cities=pd.read_csv(r"C:\Users\Sony\OneDrive\Desktop\assignments\assignment1\Indian_cities (1).csv")
print("The Top 10 Cities sorted according to sex ratio (Descending Order)")
top_pop_cities = cities.sort_values(by='sex_ratio',ascending=False)
top10_pop_cities=top_pop_cities.head(10)
top10_pop_cities

print("The Top 10 Cities sorted according to total gradutes (Descending Order)")
top_pop_cities = cities.sort_values(by='total_graduates',ascending=False)
top10_pop_cities=top_pop_cities.head(10)
top10_pop_cities

print("The Top 10 Cities sorted according to effective literacy rate total (Descending Order)")
top_pop_cities = cities.sort_values(by='effective_literacy_rate_total',ascending=False)
top10_pop_cities=top_pop_cities.head(10)
top10_pop_cities

 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.hist(cities.literates_total)

state_name = cities['state_name']
male_graduates = cities['male_graduates']
female_graduates = cities['female_graduates']

plt.scatter(state_name , male_graduates , c = female_graduates , edgecolor = 'yellow')

sns.boxplot(cities.effective_literacy_rate_total)


cities.isna().sum().sum()
