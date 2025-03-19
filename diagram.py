import turtle
import math
import time
#drawing background
scren=turtle.Screen()
scren.bgcolor('black')
p=turtle.Turtle()
p.pencolor('#2a93d4')
p.pensize(4)
p.speed(20)
x=0
p.penup()
p.goto(-300,-100)
p.pendown()
#drawing waves:
for k in range(3):
        for i in range(8):
            p.penup()
            p.goto(-300 + i * 69.2, -100+k * 60)
            p.setheading(0)  
            p.pendown()


            p.left(30)
            p.forward(80)
            p.setheading(-120) #curves
            p.circle(40,60)
#drawing line
p.penup()
p.goto(-300,85)
p.pencolor('#d3d51f')
p.setheading(0)
p.pendown()
p.forward(170)
p.penup()
p.goto(-130,85)
p.pendown()
p.forward(200)
p.penup()
p.goto(90,85)
p.pendown()
p.forward(170)
#drawing sun
p.penup()
p.goto(-110,85)
#filling sun
p.pencolor('#e5df08')
p.begin_fill()
p.fillcolor('#f2ec13')
p.setheading(270)
p.pendown()
p.circle(85,-180)
p.end_fill()
#drawing rays

p.speed(100)
ray_length = 25
num_rays = 50
radius = 85

for i in range(0,num_rays,1):
    if i%3==0:
         ray_length=40 
    elif i%2==0:
         ray_length=30

    angle_deg = i * (180 / num_rays)  
    angle_rad = math.radians(angle_deg)  # Convert to radians

    
    x_offset = 80+radius * math.cos(angle_rad)
    y_offset = radius * math.sin(angle_rad)

    p.penup()
    p.goto(-105 +x_offset, 85 + y_offset)  # Move to ray's starting point
    p.setheading(angle_deg)  # Point turtle in the correct direction
    p.pendown()
    p.forward(ray_length)  # Draw the rayy

text="მე გადმოვცურავ ზღვას..."

p.penup()
p.goto(-305, -200)  # Adjust position based on where you want the text
p.pencolor('#efe6a8')  # Set the color for the text
for letter in text:
  
    p.write(letter, font=("Sylfaen", 24, "bold"))
    time.sleep(0.2)  # Delay of 0.3 seconds between each letter
    p.setx(p.xcor() +30)
    
p.hideturtle()
scren.mainloop()


