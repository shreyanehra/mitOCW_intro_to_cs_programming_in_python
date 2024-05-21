# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:13:35 2024

@author: shrey
"""




    


def calculate_months(c, s, p, r):
    portion_down_payment = 0.25
    current_savings = 0.00
    annual_rate_of_interest = 0.04
    down_payment = portion_down_payment*c
    num_months = 0
   # half_year = 0
    
    print("Down Payment is 25% of the total cost : Rs.", down_payment, 
          "\nPer month rate of interest on Current Savings = ", (annual_rate_of_interest/12)*100)
    
    while current_savings < down_payment: 
        
         
        if num_months%6==0 and num_months!=0: 
            s = s*(1 + r/100)
        current_savings = current_savings*(1+ annual_rate_of_interest/12) + (p/100)*(s/12)
        num_months += 1

    return num_months
    


total_cost = float(input("Please enter cost of your dream house currently in rupees: "))
annual_salary = float(input("Enter your annual salary in rupees: "))
portion_saved = float(input("Enter the percentage you wish to save per month: "))
semi_annual_raise = float(input("Enter the percentage by which your salary increases every 6 months : "))


print(calculate_months(total_cost, annual_salary, portion_saved, semi_annual_raise))
