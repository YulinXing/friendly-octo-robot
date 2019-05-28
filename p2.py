pay=10
while True:
    unpaidBalance=balance
    for month in range(12):   
        unpaidBalance-=pay
        unpaidBalance=unpaidBalance + unpaidBalance * (annualInterestRate /12.0)
    if unpaidBalance <=0:     
            print 'Lowest Payment: '+str(pay)
            break
    else:
        pay+=10
