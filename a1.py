import turtle

print("Create a 6-pointed star using Turtle")

t = turtle.Turtle()
t.speed(3)

# Number of star points
points = 6  
angle = 144  # Angle for star shape

# Draw the star
for _ in range(points):
    t.forward(100)
    t.right(angle)
    t.forward(100)
    t.left(72)  # Adjust to connect points properly

# Keep the window open
turtle.done()
