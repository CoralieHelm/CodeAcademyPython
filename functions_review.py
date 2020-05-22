#May 22 2020
#Functions Review Code

def repeat_stuff(stuff, num_repeats=10):
  return stuff * num_repeats

lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)

print(song)

