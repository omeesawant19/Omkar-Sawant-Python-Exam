#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("---------------------")
print("--------MENU---------")
print("---------------------")

print("Burger       : 50 RS each")
print("Pizza        : 120 RS each")
print("French Fries : 80 RS each")

print("----------------------------------------")

burger = int(input("Enter the number of Burger :"))
pizza = int(input("Enter the number of Pizza :"))
fries = int(input("Enter the number of French Fries :"))

print("==========Bill Summary==========")

print("Burgers :",burger*50)
print("Pizza :",pizza*120)
print("French Fries :",fries*80)


d = burger*50 + pizza*120 + fries*80
print("----------------------")

print("Total bill without discount :",d)
if d >=1000:
    print("Bill after Discount is :",d-(d*0.20))
else:
    print("You dont have any Discount")



