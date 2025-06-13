from __future__ import print_function


print("-:welcome to the tip calculator:-")
bill=float(input("what was the total bill? \n$"))
tip=int(input("how much tip would you like to give? 10,12 or 15?\n"))
people=int(input("How many people to split the bill?"))
totalbill= tip/100*bill+bill
bill_per_person=totalbill/people
Final_Amount=("{:.0f}".format(bill_per_person)) 
print (f"Each person should pay: \n-:${Final_Amount}")