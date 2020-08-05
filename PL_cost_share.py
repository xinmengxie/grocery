# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:20:01 2020

@author: xiexi
"""

# preliminaries
# load dataset and merge table 
households = pd.read_csv("C:/Users/xiexi/Desktop/final/households.csv")
products   = pd.read_csv("C:/Users/xiexi/Desktop/final/products.csv")
trips      = pd.read_csv("C:/Users/xiexi/Desktop/final/trips.csv")
purchases  = pd.read_csv("C:/Users/xiexi/Desktop/final/purchases.csv")

# In[]
# change date to year&month
trips['month'] = trips.TC_date.str[2:7]

# remove useless columns
households = households.drop(columns = households.columns.values[[0,2,3,4,5,7,8]])
products = products.drop(columns = products.columns.values[[0,2,4,5,6,7]])
trips = trips.drop(columns = trips.columns.values[[0,2,3,4,5]])
purchases = purchases.drop(columns = purchases.columns.values[[0,2,4,5]])

# create private label prod_id
private_label_id = products.loc[products["brand_at_prod_id"] == "CTL BR"]
private_label_id = private_label_id["prod_id"]

# merge households and trips table
merge_1 = pd.merge(trips, households, how="left", on="hh_id")

# merge households, trips and purchases table
merge_2 = pd.merge(purchases, merge_1, how="left", on="TC_id")

# create private label only table
merge_PL_only = pd.merge(merge_2, private_label_id, how="inner", on="prod_id")

# In[] final result for c-3-ii

PL_cost_by_month = merge_PL_only.groupby('month')['total_price_paid_at_TC_prod_id'].sum()
total_cost_by_month = merge_2.groupby('month')['total_price_paid_at_TC_prod_id'].sum()
PL_cost_share_by_month = PL_cost_by_month/total_cost_by_month

# remove 2003-12 and reset index
PL_cost_share_by_month = PL_cost_share_by_month[1:].reset_index()

# create month column
PL_cost_share_by_month['month'] = range(1,13)

# set month as index
PL_cost_share_by_month = PL_cost_share_by_month.set_index('month')

#print(PL_cost_share_by_month)

# In[]
PL_cost_share_by_month.to_csv("C:/Users/xiexi/Desktop/Repository/Grocey Shopping Analysis Project/code&data/data/c-3-ii PL_cost_share.csv", sep='\t')
