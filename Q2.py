#Ques 2. wap to calculate person's income tax

gross=float(input('Enter your Gross Income ($) -> '))
depn=int(input('Enter the number of dependents -> '))

tax_income= gross - 10000 - (3000*depn)
tax= tax_income*0.2

print('You have incurred a tax of $', tax)
