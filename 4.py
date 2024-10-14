n = input()
a = []
for i in str(n):
    a.append(int(i))
a.sort()
if a[0] == 0 and len(a) > 1:
    for i in range(1, len(a)):
        if a[i] > 0:
            a[i], a[0] = a[0], a[i]
            break
for i in a:
    print(i, end = "")

#we add all n's digits to an array and sort it
#after sorting, all 0's (if any) will go to the beggining, but a number can't begin with 0 so we search for the first number that isn't 0 and put it on the first position
# and print the resulting array 