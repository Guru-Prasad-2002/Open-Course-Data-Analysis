# -*- coding: utf-8 -*-
"""ML_Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jQugyke8f6XGc8x6FVhZp5UWyf8g4yo5

# ***S Guru Prasad and Sai Harshit B***
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

plt.style.use("bmh")

df = pd.read_csv('datadoc.csv')
# df2 = pd.read_csv('datadoc.csv')

P=df["Physics Marks"]   #Reading Physics Marks as Array
C=df["Chem Marks"]
B=df["Biology Marks"]
Sum=df["SUM"]
Avg=df["AVG"]        #Reading average of all 3 subjects as an Array
GPA=df["HighSchool GPA"] #Reading GPA of a Studenty as an Array
# print(C)
# print(B)
# print(Sum)
# print(Avg)
# print(GPA)



# Phy_Avg=0.0
# Chem_Avg=0.0
# Math_Avg=0.0
# Overall_Avg=0.0
# count=0
# sum=0
# for x in P:
#   sum=sum+x
#   count=count+1
# Phy_Avg=sum/count

# print(Phy_Avg)
df.describe()

# print(df1)
# print(df2)

# df1.size                         #No of Rows*Columns
# df1.shape                        #No of Rows and Columns
# df2.size
# df2.shape
# df1.describe
# df2.describe

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

plt.style.use("bmh")
Phy_Avg=0.0
Chem_Avg=0.0
Bio_Avg=0.0
Overall_Avg=0.0
count=0
sum=0
for x in P:
  sum=sum+x
  count=count+1
Phy_Avg=sum/count          #Overall Physics Average             
sum=0.0
count=0
for x in C:
    sum=sum+x
    count=count+1
Chem_Avg=sum/count          #Overall Chemistry Average
sum=0.0
count=0
for x in B:
  sum=sum+x
  count=count+1
Bio_Avg=sum/count           #Overall Biology Average
sum=0.0
count=0
for x in Avg:
  sum=sum+x
  count=count+1
Overall_Avg=sum/count       #Overall Avearge of Average Scores of the Students
print(Phy_Avg)
print(Chem_Avg)
print(Bio_Avg)
print(Overall_Avg)

l=[Phy_Avg,Chem_Avg,Bio_Avg,Overall_Avg]

plt.xlabel('Subjects')
plt.ylabel('Averages')
plt.bar(["Physics","Chemistry","Biology","Overall"],l)
plt.show()

# print(Phy_Avg)

# print(df1)
# print(df2)

# df1.size                         #No of Rows*Columns
# df1.shape                        #No of Rows and Columns
# df2.size
# df2.shape
# df1.describe
# df2.describes

# INFERENCE
# Chemistry is Easy 
# Biology is the Hardest
# Students perform below Average in Physics and Biology
# Students Scores Above Average in Chemistry

import scipy
from scipy import stats  #Applying Linear Regression to find Total using Physics Score 

my_y = Sum
my_x = P

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(my_x, my_y)
    
print(slope)
print(intercept)

plt.scatter(P,Sum)
plt.show()

def calc_total_with_phy_score():
    print("Enter Score")
    n=int(input())
    ans=(n*3)+5
    print(ans)
calc_total_with_phy_score()

import datetime 
Application_no=df["Application No"]
# print(Application_no)
DOB=df["DOB"]
# print(DOB)
# print(type(DOB[0]))
def get_month_no(mon):
    if(mon=="Jan"):
      return 1
    if(mon=="Feb"):
      return 2
    if(mon=="Mar"):
      return 3
    if(mon=="Apr"):
      return 4
    if(mon=="May"):
      return 5
    if(mon=="Jun"):
      return 6
    if(mon=="Jul"):
      return 7
    if(mon=="Aug"):
      return 8
    if(mon=="Sep"):
      return 9
    if(mon=="Oct"):
      return 10
    if(mon=="Nov"):
      return 11
    if(mon=="Dec"):
      return 12
# k=DOB[10]
# print(k)
# print(k[-4:])
# print(len(k))
# print(k[-4:0])

Bday=[]                   #Converting String to Datetime
for x in DOB:
    dd=mm=yyyy=flag=0
    if(x[1]=="-"):
      dd=int(x[0])
      flag=0
    else:
      dd=int(x[0:2])
      flag=1
    yyyy=x[-4:]
    yyyy=int(yyyy)
    print(yyyy)
    if(flag==0):
      mm=get_month_no(x[2:-5])
    else:
      mm=get_month_no(x[3:-5])
      print(mm)
    elem=datetime.datetime(yyyy,mm,dd)
    Bday.append(elem)
print(Bday)
print(type(Bday[12]))
print(Bday[0].year)
# DOB.__dir__()

from scipy.stats.stats import pearsonr   
print(pearsonr(P,C))     #Finding Correlation Coefficient
#INFERENCE
#Have very Strong Linear RelationShip

print(pearsonr(Avg,GPA)) 
plt.scatter(Avg,GPA)
#INFERENCE
# Very WeaK Linear RelationShip bw GPA and Avg
#No Linear Relation between Age and GPA/Avg/Marks of any subject

year=[]                       #Distribution Based on Birth Year
for x in Bday:
  year.append(x.year)
d={}
for x in year:
  if x not in d.keys():
    d[x]=1
  else:
    d[x]=d[x]+1
print(d)
years=list(d.keys())
count=list(d.values())
plt.bar(years,count)
plt.show()
#INFERENCE
#Time period between 1997 and 1999 has seen the most no of Students

"""DATA VISUALISATIONS"""

import pandas as panda
raw_data=panda.read_csv("datadoc.csv")
raw_data.describe()

clean1=raw_data[raw_data["Chem Marks"]<=100]
clean2=clean1[clean1["Physics Marks"]<=100]
cleaned=clean2[clean2["Biology Marks"]<=100]
cleaned.describe()
cleaned.corr()

import matplotlib.pyplot as ppp
gpa=cleaned['HighSchool GPA']
chem=cleaned['Chem Marks']
phy=cleaned['Physics Marks']
bio=cleaned['Biology Marks']

overall=phy+chem+bio
count=0

phytotal=0
count=0
for x in phy:
  phytotal=phytotal+x
  count=count+1
phyavg=phytotal/count

chemtotal=0
for x in chem:
  chemtotal=chemtotal+x
chemavg=chemtotal/count

biototal=0
for x in bio:
  biototal=biototal+x
bioavg=biototal/count

overtotal=0
for x in overall:
  overtotal=overtotal+x
overtotavg=overall/3
overavg=overtotal/(3*count)

ppp.scatter(gpa,phy)
ppp.title("GPA vs Physics Marks")
ppp.xlabel("GPA")
ppp.ylabel("Physics Marks")
ppp.legend()

ppp.scatter(gpa,bio)
ppp.title("GPA vs Biology marks")
ppp.xlabel("GPA")
ppp.ylabel("Biology Marks")
ppp.legend()

ppp.scatter(gpa,chem)
ppp.title("GPA vs Chem marks")
ppp.xlabel("GPA")
ppp.ylabel("Chem Marks")
ppp.legend()

ppp.scatter(phy,chem)
ppp.title("Physics marks vs Chem marks")
ppp.xlabel("Physics Marks")
ppp.ylabel("Chem Marks")
ppp.legend()

ppp.scatter(bio,chem)
ppp.title("Biology marks vs Chem marks")
ppp.xlabel("Biology Marks")
ppp.ylabel("Chem Marks")
ppp.legend()