import turtle

def draw_square(some_turtle):

    for i in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    move = turtle.Turtle()
    move.shape("turtle")
    move.speed(2)
    move.color("green")

    for i in range(1,37):
        draw_square(move)
        move.right(10)

    window.exitonclick()


#def draw_circle():
   # circ = turtle.Turtle()
   # circ.shape("arrow")
   # circ.color("blue")
   # circ.speed(1)
   # circ.circle(100)


#def draw_triangle():
  #  tri = turtle.Turtle()
   # tri.shape("turtle")
   # tri.color("black")
    #tri.speed(1)
   # tri.forward(100)
   # tri.left(120)
   # tri.forward(100)
   # tri.left(120)
   # tri.forward(100)

draw_art()
#draw_circle()
#draw_triangle()



