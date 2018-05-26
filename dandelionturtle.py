import turtle

def turtle_triangle(triturtle):
	for i in range (1, 4):
		triturtle.forward(100)
		triturtle.left(60)
		triturtle.left(60)

def turtle_flower():
	window = turtle.Screen()
	window.bgcolor("black")

	wartortle = turtle.Turtle()
	wartortle.shape("turtle")
	wartortle.color("yellow")
	
	for i in range (1, 45):
		turtle_triangle(wartortle)
		wartortle.right(10)	
	wartortle.right(10)	
	wartortle.forward(250)
	
	window.exitonclick()
turtle_flower()
