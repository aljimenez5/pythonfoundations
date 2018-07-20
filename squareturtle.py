import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")
	
	squirtle = turtle.Turtle()
	squirtle.shape("turtle")	
	squirtle.color("yellow")
	squirtle.speed(2)
	
	n = 0
	while n <=  3:
		squirtle.forward(100)
		squirtle.right(90)
		n = n + 1
	window.exitonclick()
draw_square()
