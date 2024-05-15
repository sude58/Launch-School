speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)
# WIll print True since breaking force is smaller than acceleration and acceleration is larger than 0.

is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)
# It will not same as a version with parentheses since and operator have precedence over or. So and will be evaluated before or, which changes expression.