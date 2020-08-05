# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:40:42 2020

@author: xiexi
"""

# BUS 211 FINAL PROJECT PYTHON CODE

# a. 
# plot the distribution of products and modules per department
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import matplotlib.pyplot as plt
from pylab import *

#module distribution
module = pd.read_csv("./data/a-module_department.csv")
height_m = module["number_of_module"]
bars_m = module["department_at_prod_id"]
y_pos_m = np.arange(len(bars_m))
 
# Create bars
plt.bar(y_pos_m, height_m)

plt.title('Module per Department')
plt.xlabel('Department')
plt.ylabel('Number of Modules')
 
# Create names on the x-axis
plt.xticks(y_pos_m, bars_m, rotation=90)
 
# Show graphic
plt.show()

# In[]

# product distribution
product = pd.read_csv("./data/a-product_department.csv")
height_m = product["number_of_product"]
bars_m = product["department_at_prod_id"]
y_pos_m = np.arange(len(bars_m))
 

# Create bars
plt.bar(y_pos_m, height_m)

plt.title('Products per Department')
plt.xlabel('Department')
plt.ylabel('Number of products')

 
# Create names on the x-axis
plt.xticks(y_pos_m, bars_m, rotation=90)
 
# Show graphic
plt.show()
# In[]
#    b
##  Loyalism: Among the households who shop at least once a month, which % of them
##    concentrate at least 80% of their grocery expenditure (on average) on single retailer? And
##    among 2 retailers?
##    iii. Where do they live? Plot the distribution by state

# b-2-iii
df_state = pd.read_csv("./data/b-2-iii.csv")

#fig, ax1 = plt.subplots(figsize=(9,4.5), dpi= 80)
color1 = "firebrick"
color2 = "g"
color3 = "orange"
fig, ax1 = plt.subplots(figsize=(13,9), facecolor='white', dpi= 80)
ax2 = ax1.twinx()
plt1 = ax2.plot(df_state["hh_state"],df_state["num_hh"]/df_state["num_hh_all"], color = color3,alpha = 1, label = 'percentage')
ax2.set_ylabel('% of households',fontsize=10)
plt2 = ax1.bar(df_state["hh_state"],df_state["num_hh_all"], color=color1, alpha=1, label = 'number of households')
plt3 = ax1.bar(df_state["hh_state"],df_state["num_hh"], color = color2,alpha = 0.7, label = 'number of households shopping at least once a month')
ax1.set_xlabel('state',fontsize=12)
ax1.set_ylabel('number of households',fontsize=10)
ax1.set_xticks(range(0,49,1))
ax1.set_xticklabels(df_state.hh_state[0:49], rotation=60, fontsize=7.2)

# Solution for having two legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=2)

plt.title('The distribution of households that shop at least once a month by state', fontdict={'size':13.5})
plt.grid(linestyle=':')
plt.show()
plt.savefig('b-2-iii.png')

# In[]
##    Plot with the distribution:
##    i. Average number of items purchased on a given month
# b-3-i
df_q = pd.read_csv("./data/b-3-i.csv")

fig, ax = plt.subplots(figsize=(8,5), facecolor='white', dpi= 80)
plt.plot(df_q["year_mon"],df_q["avg_purchase_quant_per_month"])
plt.xlabel('month',fontsize=12)
plt.ylabel('Average number of items purchased on a given month',fontsize=10)
plt.ylim(8,11)
plt.title('Average number of items purchased on a given month', fontdict={'size':12})
plt.yticks(fontsize = 12)
plt.xticks(fontsize = 10)
plt.grid(True)
plt.show()
#plt.savefig('b-3-i.png')

# In[]
##    Plot with the distribution:
##    ii. Average number of shopping trips per month.
# b-3-ii
df_t = pd.read_csv("./data/b-3-ii.csv")

fig, ax = plt.subplots(figsize=(8,5), facecolor='white', dpi= 80)
plt.plot(df_t["year_mon"],df_t["avg_num_trips"])
plt.xlabel('month',fontsize=12)
plt.ylabel('Average number of shopping trips on a given month',fontsize=10)
plt.title('Average number of shopping trips on a given month', fontdict={'size':12})
plt.yticks(fontsize = 12)
plt.xticks(fontsize = 10)
plt.ylim(10,17.2)
plt.grid(True)
plt.show()
#plt.savefig('b-3-ii.png')

# In[]
##  Plot with the distribution:
##    iii. Average number of days between 2 consecutive shopping trips.
# b-3-iii
df_average_days_two_consecutive_trips = pd.read_csv("./data/b-3-iii.csv")

num_people = df_average_days_two_consecutive_trips["num_people_same_avg"]
fig, ax = plt.subplots(figsize=(8,5), facecolor='white', dpi= 80)
plt.bar(df_average_days_two_consecutive_trips["diff_day"],num_people)
plt.xlabel('The average number of days between to consecutive shopping trips',fontsize=12)
plt.ylabel('number of housesholds',fontsize=12)
plt.title('distribution of average number of days between 2 consecutive shopping trips', fontdict={'size':12})
plt.yticks(fontsize = 10)
plt.xticks(fontsize = 10)
plt.show()
#plt.savefig('b-3-iii.png')

# In[] c-1 

## loading data
#trip_item_by_month    = pd.read_csv("./data/3-1.csv",header=None, sep="\t")
trip_item_by_month    = pd.read_csv("./data/c-1.csv",header=None, sep="\t")
trip_item_by_month[0] = range(0,13)
trip_item_by_month    = trip_item_by_month.drop(index=0).rename(columns={0:'month', 1:'avg_trips', 2:'avg_items'}).set_index('month')
print(trip_item_by_month)

## making plot
plt.style.use('bmh')
month = trip_item_by_month.index.to_list()
data1 = trip_item_by_month.avg_trips
data2 = trip_item_by_month.avg_items

fig, ax1 = plt.subplots(figsize=[12,7])

ax1.set_title("Comparision between the Number of Trips and Items",fontsize=22, pad=30)


ax1.set_xlabel('Month',fontsize=18, labelpad = 20)
ax1.set_ylabel('Average Number of Trips', color='orangered', fontsize=18, labelpad = 16)
ax1.plot(month, data1, color='orangered', linewidth=3)
ax1.tick_params(axis='y', labelcolor='orangered', labelsize=14)
ax1.tick_params(axis='x', labelsize=16)
ax1.set_ylim(14.6,16.6)
ax1.set_yticks(np.arange(14.8,16.5,0.4))
ax1.set_xticks(month)


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylabel('Average Number of Items', color='steelblue',fontsize=18, labelpad = 16)  # we already handled the x-label with ax1
ax2.plot(month, data2, color='steelblue',linewidth=3)
ax2.tick_params(axis='y', labelcolor='steelblue', labelsize=14)
ax2.set_ylim(9.0,11)
ax2.set_yticks(np.arange(9.2,10.9,0.4))


fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
#plt.savefig('c-1.png')

# In[] c-2 
## loading data
price_item = pd.read_csv("./data/c-2.csv",header=None, sep="\t")
price_item = price_item.rename(columns={0:'avg_price', 1:'avg_items'})
print(price_item.head())

## making plot
plt.style.use('seaborn')
plt.figure(figsize=[12,10]) 
plt.scatter(price_item.avg_price[:1000], price_item.avg_items.loc[:1000], color="darkturquoise")
plt.xlabel("Average Price Paid", fontsize=18, labelpad = 20)                                                               
plt.ylabel("Average Number of Items Purchased", fontsize=18, labelpad = 16)
plt.title("Correlation between Price and Items", fontsize=22, pad=26)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()
#plt.savefig('c-2.png')



# In[] c-3-i 
## loading data
PL_category = pd.read_csv("./data/c-3-i.csv",header=None, sep="\t")
PL_category[0] = PL_category[0].str.capitalize()
PL_category = PL_category.drop(index=9).rename(columns={0:'category', 1:'private_label'}).set_index('category')
PL_category = PL_category*100
print(PL_category)

## making plot
x_ticks = ["Dry\nGrocery", 
           "Health &\nBeauty Care", 
           "Non-food\nGrocery",
           "General\nMerchandise",
           "Frozen\nFoods",
           "Dairy",
           "Deli",
           "Packaged\nMeat",
           "Fresh\nProduce",
           "Alcoholic\nBeverage"]

plt.style.use('seaborn')
plt.figure(figsize=[18,9]) 
barplot = plt.bar(x_ticks, PL_category.private_label, width=0.6, color="steelblue")
barplot[0].set_color('darkorange')
plt.xlabel("Category", fontsize=22, labelpad = 20)                                                               
plt.ylabel("Private Label (%)", fontsize=22, labelpad = 16)
plt.ylim(0,40)
plt.xticks(fontsize=15)
plt.yticks(fontsize=16)
plt.title("Private Label Share in Each Category", fontsize=26, pad=26)
plt.grid(linestyle=':')
plt.show()
plt.savefig('c-3-i.png')

# In[] c-3-ii 
## loading data
private_label_share = pd.read_csv("./data/c-3-ii PL_cost_share.csv", index_col="month", sep="\t")
private_label_share['market_share_percentage']= round(private_label_share['total_price_paid_at_TC_prod_id']*100,2)
print(private_label_share)

# making plot
plt.style.use('seaborn')
plt.figure(figsize=[12,7]) 
private_label_share['market_share_percentage'].plot(style='-o', color="steelblue",linewidth=3, markersize=10)
plt.xlabel("Month", fontsize=16, labelpad = 20)
plt.ylabel("Market Share (%)", fontsize=16, labelpad = 16)
plt.ylim(13,16)
plt.xlim(0.5,12.5)
plt.xticks(ticks=range(1,13), fontsize=16, ha='center', va='top')
plt.yticks(ticks=np.arange(13,16.5,0.5), fontsize=16)
plt.title("The Market Share of Private Label", fontsize=22, pad=26)
plt.grid(linestyle=':')

plt.savefig('c-3-ii.png')

# In[] c-3-iii-(1) Private label ratio
# loading data
PL_grocery_rate = pd.read_csv("./data/c-3-iii PL_monthly_ratio.csv", index_col="month", sep="\t")
PL_grocery_rate = round(PL_grocery_rate*100,2)
print(PL_grocery_rate)

# making plot
plt.style.use('seaborn')
plt.figure(figsize=[12,7]) 
PL_grocery_rate.high_income.plot(style='-', color="steelblue",linewidth=3,label="high income")
PL_grocery_rate.medium_income.plot(style='-', color="mediumseagreen",linewidth=3, label="medium income")
PL_grocery_rate.low_income.plot(style='-', color="salmon",linewidth=3,label="low income")
plt.xlabel("Month", fontsize=18, labelpad = 20)
plt.ylabel("Private Label (%)", fontsize=16, labelpad = 16)
plt.ylim(3,11)
plt.xlim(0.5,12.5)
plt.xticks(ticks=range(1,13), fontsize=16, ha='center', va='top')
plt.yticks(ticks=np.arange(4,11,2), fontsize=16)
plt.title("The Private Label Share in Monthly Grocery Expenditures", fontsize=22, pad=26)
plt.legend(loc="lower center", ncol=3, prop={"size":15})
plt.grid(linestyle=':')

plt.savefig('c-3-iii-(1).png')

# In[] 3-3-iii-(2) grovery monthly expenditure
## loading data
grocery_avgcost = pd.read_csv("./data/c-3-iii total_monthly_expenditure.csv",index_col='month', sep="\t")
grocery_avgcost = round(grocery_avgcost,2)
print(grocery_avgcost)

# making plot
plt.style.use('seaborn')
plt.figure(figsize=[12,7]) 
grocery_avgcost.high_income.plot(style='-', color="steelblue",linewidth=3, label="high income")
grocery_avgcost.medium_income.plot(style='-', color="mediumseagreen",linewidth=3, label="medium income")
grocery_avgcost.low_income.plot(style='-', color="salmon",linewidth=3, label="low income")
plt.xlabel("Month", fontsize=16, labelpad = 20)
plt.ylabel("The Expentures on Grocery (dollars)", fontsize=16, labelpad = 16)
plt.ylim(300,1000)
plt.xlim(0.5,12.5)
plt.xticks(ticks=range(1,13), fontsize=16, ha='center', va='top')
plt.yticks(fontsize=18)
plt.title("Monthly Grocery Expenditures by Income Level", fontsize=22, pad=26)
plt.grid(linestyle=':')
plt.legend(loc="lower center", ncol=3, prop={"size":15})

plt.savefig('c-3-iii-(2).png')

# In[] 3-3-iii-(3) : total vs private label by income level
## loading data
PL_avgcost = pd.read_csv("./data/c-3-iii PL_monthly_expenditure.csv",index_col='month', sep="\t")
PL_avgcost = round(PL_avgcost,2)
print(PL_avgcost)

# making plot
month = range(1,13)
A = grocery_avgcost.low_income
B = PL_avgcost.low_income

C = grocery_avgcost.medium_income
D = PL_avgcost.medium_income

E = grocery_avgcost.high_income
F = PL_avgcost.high_income

plt.style.use('seaborn')
fig, ax = plt.subplots(1,3,figsize=[14,7], sharex=True, sharey=True)
ax[0].bar(month, A, color = 'salmon', label="total",      width=0.7)
ax[0].bar(month, B, color = 'gold',label="private label", width=0.7)

ax[0].set_title("Low-Income", fontsize=22, pad=26)
ax[0].set_xlabel("Month", fontsize=16, labelpad = 10)
ax[0].set_ylabel("Expenditures (dollars)", fontsize=16, labelpad = 6)
ax[0].tick_params(axis='y', labelsize=14)
ax[0].tick_params(axis='x', labelsize=14)
ax[0].set_ylim(0,1050)
ax[0].set_xlim(0.2,12.8)
ax[0].set_xticks(month)
ax[0].legend(loc="upper center", ncol=2, prop={"size":14})

ax[1].bar(month, C, color = 'mediumseagreen', label="total", width=0.7)
ax[1].bar(month, D, color = 'gold',   label="private label", width=0.7)
ax[1].set_title("Medium-Income", fontsize=22, pad=26)
ax[1].set_xlabel("Month", fontsize=16, labelpad = 10)
ax[1].tick_params(axis='y', labelsize=14)
ax[1].tick_params(axis='x', labelsize=14)
ax[1].legend(loc="upper center", ncol=2, prop={"size":14})

ax[2].bar(month, E, color = 'steelblue', label="total",      width=0.7)
ax[2].bar(month, F, color = 'gold',   label="private label", width=0.7)
ax[2].set_title("High-Income", fontsize=22, pad=26)
ax[2].set_xlabel("Month", fontsize=16, labelpad = 10)
ax[2].tick_params(axis='y', labelsize=14)
ax[2].tick_params(axis='x', labelsize=14)
ax[2].legend(loc="upper center", ncol=2, prop={"size":14})

fig.tight_layout(w_pad=2)

plt.savefig('c-3-iii-(3).png')

