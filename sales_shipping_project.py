#July 9th 2020
#Code Academy Python Course
#Project Sal's Shipping

#Task: Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.
#If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

def ground_shipping_cal(weight):
    flat_charge = 20
    if weight <= 2:
        cost = (weight * 1.50) + flat_charge
        print ("Ground Shipping: To ship a {} lbs package costs ${} which includes a flat charge of ${}.".format(weight, cost, flat_charge))
        print()
        return cost
    elif weight > 2 and weight <= 6:
            cost = (weight * 3.00) + flat_charge
            print("Ground Shipping: To ship a {} lbs package costs ${} which includes a flat charge of ${}.".format(weight, cost, flat_charge))
            print()
            return cost
    elif weight > 6 and weight <= 10:
            cost = (weight * 4.00) + flat_charge
            print("Ground Shipping: To ship a {} lbs package costs ${} which includes a fat charge of ${}.".format(weight, cost, flat_charge))
            print()
            return cost
    elif weight > 10:
            cost = (weight * 4.75) + flat_charge
            print("Ground Shipping: To ship a {} lbs package costs ${} which includes a flat charge of ${}.".format(weight, cost, flat_charge))
            print()
            return cost
    else:
        return "An error has occured. Please use a valid weight"

def premium_shipping_cal(weight):
  cost = 125
  print("Premium Shipping: To ship any package regardless of it's weight costs ${}".format(cost))
  print()
  return cost

def drone_shipping(weight):
  if weight <= 2:
    cost = (4.50 * weight)
    print("Drone Shipping: To ship a {} lbs package costs ${}.".format(weight, cost))
    print()
    return cost
  elif weight > 2 and weight <= 6:
    cost = (9.00 * weight)
    print("Drone Shipping: To ship a {} lbs package costs ${}.".format(weight, cost))
    print()
    return cost
  elif weight < 6 and weight <= 10:
    cost = (12.00 * weight)
    print("Drone Shipping: To ship a {} lbs package costs ${}.".format(weight, cost))
    print()
    return cost
  elif weight > 10:
      cost = (14.25 * weight)
      print("Drone Shipping: To ship a {} lbs package costs ${}".format(weight, cost))
      print()
      return cost
  else: "An error occured. Please, use a valid weight."


def cheapest_shipping(weight):
  ground_shipping_cost = ground_shipping_cal(weight)
  premium_ground_shipping_cost = premium_shipping_cal(weight)
  drone_shipping_cost = drone_shipping(weight)
  if ground_shipping_cost < premium_ground_shipping_cost and ground_shipping_cost < drone_shipping_cost:
      print()
      return "Ground shipping is the cheapest way to ship your package. To ship a package that weights {} lbs costs ${}.".format(weight, ground_shipping_cost)
  elif premium_ground_shipping_cost < ground_shipping_cost and premium_ground_shipping_cost < drone_shipping_cost:
      print()
      return "Premium Shipping is the cheapest way to ship your package. To ship a package that weights {} lbs costs ${}.".format(weight, premium_ground_shipping_cost)
  elif drone_shipping_cost < ground_shipping_cost and drone_shipping_cost < premium_ground_shipping_cost:
      print()
      return "Drone Shipping is the cheapest way to ship your package. To ship a package that weights {} lbs costs ${}.".format(weight, drone_shipping_cost)


print("What is the cheapest method of shipping a 4.8 pound package and how much would it cost?")
print("****************")
print(cheapest_shipping(4.8))
print()
print("--------------------------------")
print()
print("What is the cheapest method of shipping a 41.5 pound package and how much would it cost?")
print("****************")
print(cheapest_shipping(41.5))
