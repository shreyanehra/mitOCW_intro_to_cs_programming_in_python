annual_salary = int(input("Enter your annual salary in rupees : "))
annual_rate_of_interest = 0.04
semi_annual_salary_increase = 0.07
num_months = 36
low = 0
high = 10000
money_2_save = 1000000*0.25
epsilon = 100

def current_savings(savings, annual_salary, annual_rate_of_interest, semi_annual_salary_increase, guessed_savings_rate, num_months):
    for i in range(num_months):
        if i % 6 == 0 and i != 0:
            annual_salary += annual_salary * semi_annual_salary_increase
        savings += (annual_salary / 12) * guessed_savings_rate + savings*(annual_rate_of_interest / 12)
        
    return savings

savings_now = current_savings(0, annual_salary, annual_rate_of_interest, semi_annual_salary_increase, 1.00, num_months)
canBuy = savings_now >= money_2_save
if canBuy == False:
    print ("Can't buy house")
else : 
    guessed_savings_rate = (high + low) / 20000
    savings_now = current_savings(0, annual_salary, annual_rate_of_interest, semi_annual_salary_increase, guessed_savings_rate, num_months)

    steps_in_bisection = 1
    while abs(money_2_save - savings_now) > epsilon and canBuy:
        if money_2_save > savings_now:
            low = guessed_savings_rate
        else:
            high = guessed_savings_rate

        guessed_savings_rate = (high + low) / 2
        savings_now = current_savings(0, annual_salary, annual_rate_of_interest, semi_annual_salary_increase, guessed_savings_rate, num_months)
        steps_in_bisection += 1

    print("Steps in Bisection :", steps_in_bisection)
    print("Guessed rate :", guessed_savings_rate)
    
