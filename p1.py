monBalance=balance
totalPay=0
for month in range(1,13):
    minPayment=monBalance * monthlyPaymentRate
    restBalance=monBalance - minPayment
    interest=restBalance * (annualInterestRate/12.0)
    monBalance =restBalance + interest
    totalPay+=minPayment
    print 'Month:'+str(month)
    print 'Minimum monthly payment:'+'%.2f' % minPayment 
    print 'Remaining balance:'+'%.2f' % monBalance

print 'Total paid:'+'%.2f' % totalPay
print 'Remaining balance:'+'%.2f' % monBalance
