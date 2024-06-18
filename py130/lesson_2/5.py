def concat_strings(*strings, sep= " "):
    return sep.join(strings)

print(concat_strings("Hello", "world!"))              # Hello world!
print(concat_strings("one", "two", "three", sep='+')) # one+two+three