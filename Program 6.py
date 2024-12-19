#!/usr/bin/env python
# coding: utf-8

# #### Write a python program to convert kilometer to miles.

# In[1]:


kilometers =float(input("Enter distance in kilometers: "))

#Conversion factor :1 kilometer = 0.621371 miles
conversion_factor = 0.621371

miles = kilometers * conversion_factor

print(f"{kilometers} kilometers is equal to {miles} miles")

