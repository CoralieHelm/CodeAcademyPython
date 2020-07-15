#July 14 2020
#FLOW, DATA, AND ITERATION
#Len's Slice Project on CodeAcademy
#Topic: You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]
num_pizzas = len(toppings)
pizzas = list(zip(prices, toppings))


print("We sell {} different kinds of pizza!".format(num_pizzas))
print("****************")
print(pizzas)
print()
pizzas.sort()
print(pizzas)
print("****************")

cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
num_two_dollar_slices = prices.count(2)

print("The cheapest pizza is {}.".format(cheapest_pizza))
print("The most expensive pizza is {}.".format(priciest_pizza))
print("The three cheapest pizzas are {}.".format(three_cheapest))
print("The number of occurrences of 2 in the prices are: {}.".format(num_two_dollar_slices))
