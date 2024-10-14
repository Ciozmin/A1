n = int(input())

print(len(bin(n)) - 3)

#bin(n) converts n to binary.
#the length of n's binary representation gives us the greatest power of 2 smaller or equal to n
#so we take the length of the string returned by bin(n) and decrease 3
#we decrease 3 because, on top of the indexing difference, bin(n) puts "0b" before the bits of n, so we must decrease 2 more to compensate for it