#Default arguments 
# Create calculate_loan_interest(principal, years, rate=8.5) that calculates simple interest. Show calls with the default rate and with a 
# custom rate.
def calculate_loan_interest(principal,years,rate=8.5):
    interest=(principal*years*rate)/100
    return interest
interest1=calculate_loan_interest(100000,2)
print("Interest with default rate =",interest1)
interest2=calculate_loan_interest(100000,2,10)
print("Interest with custom rate =",interest2)