def concatenate(*words):
    sentence = " ".join(words)
    return sentence

print(concatenate("Launch", "School", "is", "great")) # Launch School is great
print(concatenate("I", "am", "working", "on", "the", "PY130", "course")) # I am working on the PY130 course