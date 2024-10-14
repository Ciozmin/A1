a = set(input())
b = set(input())
print("They have the same digits" if a == b else "They don't have the same digits")

#we convert both numbers to sets, to keep count of what digits each one is made of.
#and then we compare them and print the corresponding message