import turtle

def draw_shapes():
    # window screen
    window = turtle.Screen()
    window.bgcolor("red")
    #turtle class and methods
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("Green")
    brad.speed(10)
    count = 1
    #size of the circle and instruction
    brad.forward(100)

    while(count <= 3):
     brad.right(90)
     brad.forward(100)
     count = count + 1
    # Draw a circle
    bingo = turtle.Turtle()
    bingo.shape("arrow")
    bingo.color("blue")
    bingo.circle(100)
   # draw a tringle
    tango = turtle.Turtle() # Turtle()is a clsss, tango bingo are the instances 
    tango.shape("turtle")
    tango.color("black")
    tango.forward(100)
    tango.left(120)
    tango.forward(100)
    tango.left(120)
    tango.forward(100)


    window.exitonclick()
draw_shapes()