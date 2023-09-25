# Indexing Starts From 0 
# Indexing From Accending Order. left to right
a = "hello"
result1 = a.index('h')
print(result1)

# Indexing From Decending Order. right to left
b = "hello"
result2 = b.rindex('h')
print(result2)

#sub-string concept 

my_var = "this word will be extracted"
fragment = my_var[0:4]
print(fragment)

# test 
my_str = "D0e0v0a0n0s0h0"
sys = my_str[0:14:2]
print(sys)

#methods
# upper(), lower(), split(), join(), find(), replace()

#upper

g = "abhay"
fragment= g.upper()
print(fragment)

#lower
h = "ABHAY"
bruh = h.lower()
print(bruh)

#split
p = "A b h a y"
we = p.split()
print(we)

#join
zam = "S Y S T E M"
lol = zam.split()
k = "".join(lol)
print(k)

#find
my_fork = input("Find Some Thing From String?")
my_lol = "WORD"
ans = my_lol.find(my_fork)
print(ans)


# Reverse
fo = "FGHI"
koko = fo.split('0')
print(type(koko))
print(koko.reverse())
meo = "".join(koko)
print(meo)
