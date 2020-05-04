# TrigonometryVisualization

A very small PyGame program that I made to help me better visualize the Sine and Cosine trigonometric functions, and how they relate to the cartesian plane.

![Demo](https://github.com/Nytra/TrigonometryVisualization/blob/master/demo.gif)

A demo of the program in action.

The green line is the cosine of the angle theta enclosed by the positive x-axis and the white line in the anticlockwise direction
The blue line is the sine of the same angle.

It works by taking the position of the mouse cursor, normalizing it so that the origin is the center of the circle (if the mouse cursor is on the left half of the circle, the normalized x value would be negative) and passing those values to some code that uses the arctan() function to calculate the angle theta. i had to add some special cases to get this to work correctly. 

then passing theta to sin() and cos() to get the point on the circle, and then drawing a line from the center of the circle to that point
