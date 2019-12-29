print("Program №3")
a = float(input("Enter the first number " ))
b = float(input("Enter the second number " ))
c = float(input("Enter the third number " ))
d = a + b + c ;
print("The sum of three numbers: ", d)
d = a * b * c ;
print("Multiplication of three numbers: ", d)
d = (a + b + c) / 3 ;
print("The average of three numbers: ", d)

if a > b :
	max = a
else:
	max = b
if c > max:
	max = c
print("The larger of three numbers: ", max)

if a < b and a < c:
	print("The smaller of three numbers: ", a)
if b < a and b < c:
	print("The smaller of three numbers: ", b)
if c < a and c < b:
	print("The smaller of three numbers: ", c)


