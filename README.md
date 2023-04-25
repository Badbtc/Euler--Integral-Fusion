# Euler--Integral-Fusion

<a>The Integral Fusion problem involves finding the value of the integral of the function f(x) = sin(x^2) on the interval [0,π]. Here are the steps to solve this problem:</a>

1-We can approximate the value of the integral using the midpoint rule, which states that the integral of a function f(x) over an interval [a,b] can be approximated as (b-a) * f((a+b)/2).
2-We can use this rule to approximate the value of the integral of f(x) on the interval [0,π] by dividing the interval into n subintervals of equal length and computing 3-the sum of the areas of rectangles with height f((x_i + x_{i-1})/2) and width (π/n), where x_i and x_{i-1} are the endpoints of the i-th subinterval.
4-We can compute the sum using a loop that iterates over the subintervals and adds up the areas of the rectangles.
5-We can then return the value of the sum as the approximate value of the integral.
