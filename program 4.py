#!/usr/bin/env python
# coding: utf-8

# #### Write a  python progarm to swap two variables

# In[1]:


# Input two variables
a = input("Enter the value of the first variable(a): ")
b = input("Enter the value of the second variable(b): ")
#Dispaly the original value
print(f"Original values: a = {a},b = {b}")
#Swap the values using a temporary variable
temp = a
a = b
b = temp
# Display the swapped values
print(f"Swapped values: a = {a}, b={b}")

