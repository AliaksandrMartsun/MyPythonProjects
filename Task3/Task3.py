print("Program №3")

a = float(input("Enter the first number " ))
b = float(input("Enter the second number " ))
c = float(input("Enter the third number " ))

print("The sum of three numbers: ", a + b + c )
print("Multiplication of three numbers: ", a * b * c )
print("The average of three numbers: ", ( a + b + c ) / 3 )

if a > b :
	max = a
	min = b
else:
	max = b
	min = a
if c > max:
	max = c
elif c < min:
	min = c

print("The larger of three numbers: ", max)
print("The smaller if three numbers: ", min)
