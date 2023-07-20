import turtle

animation = turtle.Turtle()

animation.speed(0)

animation.hideturtle()

animation.getscreen().bgcolor("black")

animation.color("red")

for i in range(100):
	
	animation.circle(i)

	animation._rotate(5)

turtle.done()
