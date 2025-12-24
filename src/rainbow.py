from turtle import *
from colorsys import*


tracer(10)
bgcolor("black") # Set background color to black
shape("circle") # Set turtle shape to circle
pensize(1) # Set pen size
hue = 0 # Hue value for color
penup()

for i in range(700): # Number of iterations for the spiral
   hue = (hue + 0.01) % 1 # Increment hue and wrap around
   color(hsv_to_rgb(hue, 1, 1)) # Convert HSV to RGB and set color
   size = 0.1 + i * 0.01 # Calculate size for spiral effect
   shapesize(size, size) # Set the size of the turtle shape
   forward(i * 0.5) # Move forward to create spiral
   right(59) # Turn right to create spiral effect
   stamp() # Stamp the turtle shape at the current position
done()