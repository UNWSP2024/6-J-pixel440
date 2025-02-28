def find_tax_rate(total_sales):
   state_rate=0.05
   county_rate=0.025

   state_tax=state_rate*total_sales
   county_tax=county_rate*total_sales
   total_tax=county_tax+state_tax

   return state_tax,county_tax,total_tax

def main():
   total_sales=float(input("Please enter the total sales this month:$"))

   total_county_tax,total_state_tax,total_tax=find_tax_rate(total_sales)


   print(f"The amount of county sales tax is ${total_county_tax:.2f}")
   print(f"The amount of state sales tax is ${total_state_tax:.2f}")
   print(f"The total sales tax (county plus state) is ${total_tax:.2f}")

if __name__=="__main__":
   main()
