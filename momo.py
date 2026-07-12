# momo shop revnue calculation
costprice_momo = 70
sellingprice_momo =120
Number_of_momo_sold= int (input("Enter the number of momo sold: "))
total_cost = costprice_momo * Number_of_momo_sold
total_revenue = sellingprice_momo * Number_of_momo_sold
profit = total_revenue - total_cost
profit_margin = (profit / total_revenue) * 100
print("The total cost is:", total_cost)
print("The total revenue is:", total_revenue)
print("The profit is:", profit)
print("The profit margin is:", profit_margin, "%")
