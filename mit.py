## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
yearly_salary = float(input("Enter your yearly salary: "))
b = yearly_salary
low = 0.0
high = 1.0
portion_saved = (low+high)/2
cost_of_dream_home = 1000000.0
semi_annual_raise = .07
portion_down_payment = 0.25
amount_saved = 0
r = 0.04
amount_needed = cost_of_dream_home*portion_down_payment
months = 36
monthly_saved = yearly_salary*portion_saved/12
count = 0
maximum = amount_needed + 100
minimum = amount_needed -100
a = True

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
while(a):
    yearly_salary = b 
    amount_saved = 0
    monthly_saved = yearly_salary*portion_saved/12
    
    for i in range(0,months):
        amount_saved += monthly_saved + amount_saved*r/12
        if(i%6==0):
            yearly_salary += yearly_salary*semi_annual_raise
            monthly_saved = yearly_salary*portion_saved/12

    if amount_saved > maximum:
        portion_saved = (portion_saved+low)/2
        print("hi")
    elif amount_saved < minimum:
        portion_saved = (high+portion_saved)/2
        print("bye")
    else:
        print(portion_saved)
        a = False
    count +=1
    print(count)
