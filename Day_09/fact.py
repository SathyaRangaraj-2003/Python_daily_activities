

x = float('nan')
print(x == x)  # Output: False


# Even though x is compared to itself, the result is False!

# Why?
# NaN stands for "Not a Number".
# According to IEEE standards, NaN is not equal to anything, even itself.


x=float('nan')

print(float('nan') == float('nan'))  #False
print(id(x) == id(x)) #True
print(x == x)  #False