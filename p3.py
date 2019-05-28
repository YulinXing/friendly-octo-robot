lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12.0) ** 12) / 12.0        
while True:
        pay = (lowerBound + upperBound) / 2.0
        unpaidBalance=balance
        for month in range(12):
                unpaidBalance-=pay
                unpaidBalance=unpaidBalance + unpaidBalance * (annualInterestRate /12.0)
        if abs(unpaidBalance - 0) <=0.01:  
                print 'Lowest Payment: '+'%.2f' % pay
                break
        else:
                if unpaidBalance > 0:
                        lowerBound = pay
                else:
                        upperBound = pay
