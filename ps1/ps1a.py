# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:21:25 2024

@author: shrey
"""


def calculate_months(c, s, p):
    portion_down_payment = 0.25
    current_savings = 0.00
    annual_rate_of_interest = 0.04
    down_payment = portion_down_payment*c
    num_months = 0
    
    print("Down Payment is 25% of the total cost : Rs.", down_payment, 
          "\nPer month rate of interest on Current Savings = ", (annual_rate_of_interest/12)*100)
    
    while current_savings<= down_payment: 
        num_months += 1
        current_savings = current_savings*(1+ annual_rate_of_interest/12) + (p/100)*(s/12)

    return num_months
    


total_cost = float(input("Please enter cost of your dream house currently in rupees: "))
annual_salary = float(input("Enter your annual salary in rupees: "))
portion_saved = float(input("Enter the percentage you wish to save per month: "))


print(calculate_months(total_cost, annual_salary, portion_saved))


