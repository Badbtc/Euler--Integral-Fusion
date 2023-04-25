import math

def f(x):
    return math.sin(x**2)

n = 1000 # number of subintervals
delta_x = math.pi/n # width of each subinterval
sum = 0

for i in range(n):
    x_i = delta_x * (i + 0.5) # midpoint of subinterval i
    sum += f(x_i) * delta_x

print(sum)
