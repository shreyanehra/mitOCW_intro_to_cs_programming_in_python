

annual_salary = int(input("Enter your annual salary in rupees : "))
annual_rate_of_interest = 0.04
semi_annual_salary_increase  = 0.07
num_months = 36
low = 0
high = 10000
money_2_save = 1000000
guessed_savings_rate = high/10000
epsilon = 100
savings_now = 0

def current_savings(savings, annual_salary, annual_rate_of_interest, semi_annual_salary_increase, guessed_savings_rate, num_months):
    for i in range(0, 36, 1):
        if i%6==0 and i!=0:
            annual_salary += annual_salary*semi_annual_salary_increase
        savings = savings(1 + (annual_rate_of_interest/12)) + (annual_salary/12)*guessed_savings_rate
        
    return savings
        
#if all of the sary was gettings saved
savings_now = current_savings(savings_now, annual_salary, annual_rate_of_interest, semi_annual_salary_increase, guessed_savings_rate, num_months) 

def canBuy(savings_now, money_2_save):
    if(savings_now<money_2_save) :
        print("Can't buy the house in 3 months.")
        return False
    else:
        return True
    
guessed_savings_rate = int((high+low)/20000)
savings_now = current_savings(0, annual_salary, annual_rate_of_interest, semi_annual_salary_increase, guessed_savings_rate, num_months) 

while(abs(money_2_save - savings_now)>=epsilon)
    if(money_2_a