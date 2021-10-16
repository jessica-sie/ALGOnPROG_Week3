"""
An elementary school teacher has asked for your help in teaching their students about types of fractions,
as well as reducing (or simplifying) fractions.
The teacher also reminds you that a fraction cannot be reduced if the greatest common divisor (gcd) is 1;
if it is not 1, the gcd can be used to reduce the fraction by dividing both the numerator and the denominator
by the gcd.

1) Ask the user to enter a numerator and denominator. Use input validation to ensure that both the numerator and
denominator are positive. (Note: 0 is not considered positive.)
2) Calculate the greatest common divisor (gcd) using the gcd function from the math module. The function can be used as:
math.gcd(a,b) where a and b are the numerator and denominator respectively. Don’t forget to include the math module!
"""

import math
num = 0
den = 0
# input validation to ensure positive inputs for numerator and denominator
while num <= 0:
    num = int(input("Enter numerator with a value greater than 0:"))
while den <= 0:
    den = int(input("Enter denominator with a value greater than 0:"))

# proper fractions
if num <= den:
    print(num, "/", den, " is a proper fraction")
    # simplifying proper fractions
    gcd = math.gcd(num, den)
    if gcd == 1:
        print("this fraction can no longer be reduced")
    else:
        while gcd != 1:
            num = num // gcd
            den = den // gcd
            gcd = math.gcd(num, den)
        print("this fraction can be reduced to", num, "/", den)


# improper fractions
else:
    # can it be reduced further?
    gcd = math.gcd(num, den)
    if gcd == 1:
        print("this improper fraction cannot be reduced any further")
    else:
        while gcd != 1:
            num = num // gcd
            den = den // gcd
            gcd = math.gcd(num, den)
        print("this improper fraction can be reduced to", num, "/", den)
    # mixed number or whole number
    mod = num % den
    if mod == 0:
        print("the whole number is", int(num/den))
    else:
        whole = (num - mod) // den
        print("the mixed number is", whole, "and", mod, "/", den)
