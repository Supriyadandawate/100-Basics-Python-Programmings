#!/usr/bin/env python
# coding: utf-8

# #### Write a Python program to do arthematical operations addition and division.
# 

# In[1]:


# Addition
num1 = float(input("Enter the first number for addition:"))
num2 = float(input("Enter the second number for addition:"))
sum_result = num1 +num2 
print(f"sum:{num1} +{num2} = {sum_result}")


# In[2]:


#division
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divided for division: "))
if num4 == 0:
    print("Error: Division by zero is not allowed.")
else:
    div_result = num3/num4
    print(f"Division: {num3}/{num4} = {div_result}")

