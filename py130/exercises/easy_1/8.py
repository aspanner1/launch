string = "abcdefghijklmnopqrstuvwxyz"

print(list((string[i] for i in range(len(string) - 1, 0, -1))))