#customer bill calculator
customer_name = input("Customer Name : ")
customer_details = input("Table No : ")
bill_total = int(input("Total : " ))
before_tax_total = bill_total
after_tax_total = (before_tax_total + 50)
print("CUSTOMER DETAILS")
print("Customer Name: "+customer_name,"\n","Table No: "+customer_details)
print("Before Tax: " + str(before_tax_total) )
print(f"After Tax:  {after_tax_total}")
print("Grand Total: " + str(after_tax_total))