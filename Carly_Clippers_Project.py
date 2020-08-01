#July 16 2020
#Carly's Clippers Project
#You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.
#You have been provided with three lists:
#hairstyles: the names of the cuts offered at Carly’s Clippers
#prices: the price of each hairstyle in the hairstyles list
#last_week: the number of each hairstyle in hairstyles that was purchased last week
#Let’s get started!

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_prices = 0
total_revenue = 0

for price in prices:
  total_prices += price

average_price = total_prices / len(prices)
print("Average Haircut Price: {}".format(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: {}".format(total_revenue))

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30 ]


print(cuts_under_30)
