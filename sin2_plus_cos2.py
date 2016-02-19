print "Part A:"
print "Does sin^2(x)+cos^2(x)=1 ?"
from math import sin, cos, pi
x = pi/4
1_val = math.sin(x)**2 + math.cos(x)**2
print y
if 1_val==1:
    print "Yes."
else:
    print "No."

print "Part B:"
v0= 3 #m/s
t= 1 #s
a= 2 #m/s**2
s= v0*t + 0.5*a*(t**2)
print s

print "Part C:"
a = 3.3
b = 5.3
a2= a**2
b2= b**2

eq1_sum= a2 + (2*a*b) +b2
eq2_sum= a2 - (2*a*b) + b2

eq1_pow=(a+b)**2
eq2_pow=(a-b)**2

print "First equation: %g = %g", % (eq1_sum, eq1_pow)
print "Second equation: %h = %h", (eq2_sum, eq2_pow)
