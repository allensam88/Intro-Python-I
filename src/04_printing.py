"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("%2d %0.5f %s" % (x, y, z))

# Use the 'format' string method to print the same thing
print("{0:2d} {1:0.5f} {2}".
      format(x, y, z))

# Finally, print the same thing using an f-string
print(f"{x} {y} {z}")
