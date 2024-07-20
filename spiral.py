"""
trying to compute a good spiral for the festival of lights ferris wheel
This program uses the Law of Cosines to compute how much string is used for
a spiral of given dimensions. In that sense it won't solve the problem directly,
only let you play with parameters until you come to a workable solution.
"""

from math import tau, atan, cos, radians, sqrt

# constants, all in inches
inner_radius = 5
inner_circumference = tau * inner_radius
outer_radius = 49
outer_circumference = tau * outer_radius
spokes = 12
spoke_angle = radians(360) / spokes
string_ratio = atan(spoke_angle)
strings_joined = 6
string_length = 16 * 12 * strings_joined
inches_per_light = 4
increment_per_circle = 6.5  # <= an interesting value to change
increment_per_spoke = increment_per_circle / spokes

print(f"inner radius: {inner_radius} in")
# print(f"inner circumference: {inner_circumference:.1f} in")
print(f"outer radius: {outer_radius} in")
# print(f"outer circumference: {outer_circumference:.1f} in")
print(f"string length: {string_length} in")
print(f"using increment {increment_per_circle:.1f} inches per revolution")
print(f"using increment of {increment_per_spoke:.2f} inches per SPOKE")
print("=" * 30)

def length_of_opp_side(side_a, side_b, angle_radians)->float:
    """We're computing the length of one side of a triangle where the other two sides
    (current radius and current radius plus one spoke increment)
    and the interior angle (30 degrees with 12 spokes).
    If the sides are a, b, c and angles A, B, C are opposite the
    same lettered side
    c = sqrt(a**2 + b**2 - (2 * a * b * cos(C))
    """
    length = sqrt((side_a ** 2) + (side_b ** 2) - (2 * side_a * side_b * cos(angle_radians)))
    curious = length * 2 / (side_a + side_b)
    return length


radius = inner_radius
string_used = 0
spoke_number = 1
test = True
while test:
    string_used = string_used + length_of_opp_side(radius, radius + increment_per_spoke, spoke_angle)
    if spoke_number % spokes == 0:
        print(
            f"string used {string_used:.1f}, lights {string_used/inches_per_light:.1f}, current radius {radius:.1f}"
        )
        pass
    radius = radius + increment_per_spoke
    if radius > outer_radius:
        print(
            f"ran out of wheel before running out of lights, try smaller increment than {increment_per_circle}"
        )
        print(f"radius {radius:.1f}, outer radius: {outer_radius} in")
        print(f"string used {string_used:.1f}, string length: {string_length} in")
        test = False
    if string_used > string_length:
        print(f"ran out of lights, try larger increment than {increment_per_circle}")
        print(f"radius {radius:.1f}, outer radius: {outer_radius} in")
        print(f"string used {string_used:.1f}, string length: {string_length} in")
        test = False
    spoke_number += 1


print("done")
