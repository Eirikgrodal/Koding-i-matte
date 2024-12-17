import math

# Basic arithmetic operations
a = 5
b = 3
addition = a + b  # Addition: 5 + 3 = 8
subtraction = a - b  # Subtraction: 5 - 3 = 2
multiplication = a * b  # Multiplication: 5 * 3 = 15
division = a / b  # Division: 5 / 3 = 1.6666666666666667
exponentiation = a ** b  # Exponentiation: 5^3 = 125
modulo = a % b  # Modulo: 5 % 3 = 2 (remainder of division)

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Exponentiation: {exponentiation}")
print(f"Modulo: {modulo}")

# Trigonometric functions
angle = math.pi / 4  # 45 degrees in radians
sin_value = math.sin(angle)  # Sine: sin(45 degrees) = 0.7071067811865476
cos_value = math.cos(angle)  # Cosine: cos(45 degrees) = 0.7071067811865476
tan_value = math.tan(angle)  # Tangent: tan(45 degrees) = 1.0

print(f"Sine: {sin_value}")
print(f"Cosine: {cos_value}")
print(f"Tangent: {tan_value}")

# Square root and logarithmic functions
number = 16
square_root = math.sqrt(number)  # Square root: sqrt(16) = 4.0
logarithm = math.log(number, 2)  # Logarithm: log base 2 of 16 = 4.0

print(f"Square root: {square_root}")
print(f"Logarithm: {logarithm}")


# Calculating the area of a circle
radius = 5
area = math.pi * radius ** 2
print(f"The area of a circle with radius {radius} is {area}")

# Calculating the circumference of a circle
circumference = 2 * math.pi * radius
print(f"The circumference of a circle with radius {radius} is {circumference}")

# Calculating the hypotenuse of a right triangle
side_a = 3
side_b = 4
hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)
print(f"The hypotenuse of a right triangle with sides {side_a} and {side_b} is {hypotenuse}")

# Calculating the factorial of a number
number = 5
factorial = math.factorial(number)
print(f"The factorial of {number} is {factorial}")

# Generating random numbers
random_number = random.random()  # Random float between 0 and 1
print(f"A random number between 0 and 1: {random_number}")

random_integer = random.randint(1, 10)  # Random integer between 1 and 10
print(f"A random integer between 1 and 10: {random_integer}")

# Rounding numbers
decimal_number = 3.14159
rounded_number = round(decimal_number, 2)  # Round to 2 decimal places
print(f"The rounded number is {rounded_number}")

# Converting degrees to radians
degrees = 90
radians = math.radians(degrees)
print(f"{degrees} degrees is equal to {radians} radians")

# Converting radians to degrees
radians = math.pi / 2
degrees = math.degrees(radians)
print(f"{radians} radians is equal to {degrees} degrees")

# Calculating the absolute value of a number
number = -5
absolute_value = abs(number)
print(f"The absolute value of {number} is {absolute_value}")

# Calculating the ceiling and floor of a number
number = 3.7
ceiling = math.ceil(number)
floor = math.floor(number)
print(f"The ceiling of {number} is {ceiling}")
print(f"The floor of {number} is {floor}")

# Calculating the greatest common divisor (GCD) of two numbers
number1 = 12
number2 = 18
gcd = math.gcd(number1, number2)
print(f"The GCD of {number1} and {number2} is {gcd}")

# Calculating the least common multiple (LCM) of two numbers
number1 = 4
number2 = 6
lcm = number1 * number2 // math.gcd(number1, number2)
print(f"The LCM of {number1} and {number2} is {lcm}")

# Calculating the natural logarithm of a number
number = 2.71828
natural_logarithm = math.log(number)
print(f"The natural logarithm of {number} is {natural_logarithm}")

# Calculating the base 10 logarithm of a number
number = 100
log_base_10 = math.log10(number)
print(f"The base 10 logarithm of {number} is {log_base_10}")

# Calculating the exponential value of a number
number = 2
exponential_value = math.exp(number)
print(f"The exponential value of {number} is {exponential_value}")

# Calculating the hyperbolic sine of a number
number = 1
hyperbolic_sine = math.sinh(number)
print(f"The hyperbolic sine of {number} is {hyperbolic_sine}")

# Calculating the hyperbolic cosine of a number
number = 1
hyperbolic_cosine = math.cosh(number)
print(f"The hyperbolic cosine of {number} is {hyperbolic_cosine}")

# Calculating the hyperbolic tangent of a number
number = 1
hyperbolic_tangent = math.tanh(number)
print(f"The hyperbolic tangent of {number} is {hyperbolic_tangent}")

# Calculating the inverse hyperbolic sine of a number
number = 1
inverse_hyperbolic_sine = math.asinh(number)
print(f"The inverse hyperbolic sine of {number} is {inverse_hyperbolic_sine}")

