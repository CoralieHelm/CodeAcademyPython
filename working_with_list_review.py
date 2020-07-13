#July 12 2020
#WORKING WITH LISTS IN PYTHON
#Review

#inventory is a list of items that are in the warehouse for Bob’s Furniture. How many items are in the warehouse?
# Save your answer to inventory_len.

inventory_len = len(inventory)

#S elect the first element in inventory. Save it to the variable first.
first = inventory[0]

# Select the last item from inventory and save it to the variable last.
last = inventory[-1]

#Select items from the inventory starting at index 2 and up to, but not including, index 6.
#Save your answer to inventory_2_6.

inventory_2_6 = inventory[2:6]

#Select the first 3 items of inventory and save it to the variable first_3.
first_3 = inventory[:3]

#How many 'twin bed's are in inventory? Save your answer to twin_beds.
twin_beds = inventory.count("twin bed")

#Sort inventory using .sort().
inventory.sort()
