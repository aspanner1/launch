from functools import reduce

print(reduce(lambda x, y: x + " " + y, ["Hello", "Darkness", "My", "Old", "Friend"]))