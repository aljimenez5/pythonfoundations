import turtle

def turtle_diamond(dturtle):
        for i in range (1, 5):
                dturtle.forward(100)
                dturtle.left(60)
		dturtle.left(60)

def turtle_flower():
        window = turtle.Screen()
        window.bgcolor("black")

        wartortle = turtle.Turtle()
        wartortle.shape("turtle")
        wartortle.color("yellow")

        for i in range (1, 40):
                turtle_diamond(wartortle)
                wartortle.right(10)
        wartortle.hideturtle()
	window.exitonclick()
turtle_flower()
