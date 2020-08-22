#Python supports the following logical operators
# 1. and - if both the operands are true, the condition is true
# 2. or - if any of the operands are true, the condition is true 
# 3. not - return false if the results is true, and return true if the results is false. 
x = 1
y = 0
# the  statment in this is false, the not statment is the inverse x does not equal y so it's false but since it's a not statement it becomomes the inverse so it's a true
# false or true is equal to a true statment
z = ((x == y) and (x == y)) or not(x == y)
# false or true is equal to a true statment but because of the not it's inverse is false 
print(not(z))
