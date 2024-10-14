ct = 0
n = 1
while int(n) > 0:
    n = input()
    if n[len(n)-1] < n[len(n)-2]:
        ct += 1
print(ct)
#for each number read, we compare its 2 least segnificant digits and increase the counter accordingly
#and then print it