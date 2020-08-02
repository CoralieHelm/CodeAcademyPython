#!/usr/bin/env python
# coding: utf-8

# # BUILD A TOURISM RECOMMENDATION ENGINE
# 
# "Welcome to The Boredless Tourist, an online application giving you the power to find the parts of the city that fit the pace of your life. We at The Boredless Tourist run a recommendation engine using Python. We first evaluate what a person’s interests are and then give them recommendations in their area to venues, restaurants, and historical destinations that we think they’ll be engaged by."
# 
# 
# 

# In[1]:


destinations = [
"Paris, France",
"Shanghai, China",
"Los Angeles, USA",
"São Paulo, Brazil",
"Cairo, Egypt",
]


# In[3]:


test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


# 
# In the body of get_destination_index(), find the index of destination and save the results into a variable called destination_index.

# In[27]:


def get_destination_index(destination):
  try:
    destination_index = destinations.index(destination)
    return destination_index
  except Exception as e:
        return "An error has occured. The destination is not listed"


# In[23]:


Paris = get_destination_index("Paris, France")
print(Paris)


# In[28]:


Hyderabad = get_destination_index("Hyderabad, India")
print(Hyderabad)


# Now let’s define a function called get_traveler_location().
# 
# get_traveler_location() is going to take a single parameter, traveler.
# 
# In the body of get_traveler_location(), access the traveler’s destination string and save it into traveler_destination.

# In[29]:


def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  return traveler_destination


# In[31]:


test = get_traveler_location(test_traveler)
print(test)


# 
# Use traveler_destination along with get_destination_index() to retrieve the index of the destination where the traveler is. Save the index of the traveler’s destination into the variable traveler_destination_index.

# In[34]:


def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)


# 
# Now we want to create and maintain a list of attractions. Let’s start by defining a list called attractions.
# Actually, we want attractions to be an empty list for every destination in destinations.

# In[50]:


attractions = [ [] for destination in destinations]


# In[51]:


print(attractions)


# Now let’s create a function called add_attraction(). This function should take two parameters: destination, the name of the location and attraction, the attraction. First we should attempt to find the index of the destination. Use get_destination_index() with the passed in destination in order to retrieve the index of the destination. Save the results into destination_index. What happens if the destination passed in to add_attraction() doesn’t exist? Right now we want to ignore it.
# 
# Add a try block to the body of add_attraction() and catch the possible ValueError that could happen when you define destination_index.

# In[49]:


def add_attractions(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
  except Exception as e:
    return "Error occured"
  


# 
# If the destination does exist, then we already have a list for it in attractions. Use the destination_index to find the appropriate list in attractions and save that list to attractions_for_destination.Append the attraction passed into add_attraction to the list attractions_for_destination.
# 
# That’s all we want this function to do, so we can return after adding the attraction to the list.

# In[52]:


def add_attractions(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except Exception as e:
    return 

add_attractions("Los Angeles, USA", ['Venice Beach', ['beach']])
print(attractions)


# Let’s add a few more interesting places to go, paste the following code to add a few more attractions:
# 
# add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
# 
# add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
# 
# add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
# 
# add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
# 
# add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
# 
# add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
# 
# add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
# 
# add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
# 
# add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
# 
# add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# In[62]:


add_attractions("Paris, France", ["the Louvre", ["art", "museum"]])
add_attractions("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attractions("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attractions("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attractions("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attractions("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attractions("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attractions("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attractions("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attractions("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


# In[77]:


print(attractions)


# We want to be able to help our traveler’s find the most interesting places in a new city for them. In order to do that we need to match their interests with the possible locations in a city.
# 
# Write a function called find_attractions() that takes two parameters: destination, the name of the destination and interests, a list of interests.
# We’ll need the city’s destination_index to look up its attractions in our attractions table.
# 
# Create a variable called destination_index and save the destination’s index to it using get_destination_index()

# In[56]:


def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)


# Look up that destination’s attractions by indexing into attractions with destination_index. Save this into the variable attractions_in_city.

# In[57]:


def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  


# Create a new list called attractions_with_interest. Make it empty when declaring it, we’ll save attractions into this list if they match one of our interests.

# In[64]:


attractions_with_interest = []


# 
# Create a loop over attractions_in_city saving each item in the list into the temporary variable possible_attraction.
# 
# For each attraction, retrieve the tagged information about it. The tags are all saved in the second place (index 1) in the attraction. In the body of the for loop, save the attraction’s tags into the variable attraction_tags.

# In[87]:


def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = possible_attraction[1]


# 
# After retrieving the attraction tags, we want to see if any of the given interests are in attraction_tags. In order to do this, we’re going to loop through the interests and check if any of them are in attraction_tags.
# 
# Create a for loop in the body of the current for loop to loop through each interest in interests.
# 
# For every interest in interests, check if that interest is in attraction_tags.
# 
# If the interest is in the attraction_tags, append possible_attraction to attractions_with_interest.

# In[84]:



def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction)
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)


# We don’t want to show the tags to our users when we recommend things to them, so let’s just append the name of each attraction.
# 
# In the body of find_attractions(), find where you append possible_attraction to attractions_with_interest. Change this so you only append possible_attraction[0] which will only append the name.

# In[86]:


def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)


# Now let’s get to the main event, connecting people with the attractions that they are interested in.
# 
# Define a function called get_attractions_for_traveler() that takes a single parameter, traveler.
# 
# Let’s separate out the traveler’s data. Save the following data:
# 
# Save traveler[1] into a variable called traveler_destination.
# 
# Save traveler[2] into a variable called traveler_interests.

# In[88]:


def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests  = traveler[2]


# 
# Call find_attractions() with the two arguments traveler_destination and traveler_interests. Save the results into traveler_attractions.

# In[89]:


def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests  = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)


# Create a new string, this is what we’ll want to show our traveler when they open our application:
# 
# "Hi Dorothy Bortman, we think you'll like these places around Seattle, USA: the SAM, the Pike Place Market."
# Start with the beginning, just "Hi " (with a space afterwards).
# 
# Save "Hi " into a variable called interests_string.
# 
# 
# Update interests_string to include the name of the traveler. The traveler’s name can be found at traveler[0]. “Add” this to interests_string so that it includes the name of the traveler.
# 
# We’ll want to add a little more to the interests_string before we list the interests. Add the following:
# 
# This string:
# ", we think you'll like these places around "
# The place
# 
# 
# Lastly, we want to add the names of the places to go! Loop through traveler_attractions and for every attraction in the list concatenate that attraction to interests_string. You can add commas and spaces to interests_string to make it more legible as well.
# 
# 
# After you’re finished adding all the names of the interests, return interests_string

# In[ ]:





# 
# Let’s give it a test drive! Try calling get_attractions_for_traveler() with the following argument:
# 
# ['Dereck Smill', 'Paris, France', ['monument']]
# Save the results of get_attractions_for_traveler() into the variable smills_france.

# In[109]:


def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests  = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi {}, we think you'll like these places around {}:".format(traveler[0], traveler[1])
  
  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:
      interests_string += " the " + traveler_attractions[i] + "."
    else:
      interests_string += " the " + traveler_attractions[i] + ", "
  return interests_string


smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(smills_france)
ross_china = get_attractions_for_traveler(["Ross Helm", "Shanghai, China", ["art"]])
print(ross_china)


# In[ ]:





# In[ ]:




