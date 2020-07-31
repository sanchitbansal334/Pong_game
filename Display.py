import turtle
import os
import winsound
#Function

def pong():
	wn = turtle.Screen()
	wn.title("Pong Game")
	wn.bgcolor("black")
	wn.setup(width=900,height=700)
	wn.tracer(0)
	#margin
	tur = turtle.Turtle()
	tur.speed(0)
	tur.color('Cyan')
	tur.penup()
	tur.goto(0,300)
	tur.pendown()
	tur.forward(400)
	tur.right(90)
	tur.forward(600)
	tur.right(90)
	tur.forward(800)
	tur.right(90)
	tur.forward(600)
	tur.right(90)
	tur.forward(400)
	tur.hideturtle()
	#Paddle A
	pad_a = turtle.Turtle()
	pad_a.speed(0)
	pad_a.shape("square")
	pad_a.color("white")
	pad_a.shapesize(stretch_wid=5 , stretch_len=1)
	pad_a.penup()
	pad_a.goto(-350,0)
	#Paddle B
	pad_b = turtle.Turtle()
	pad_b.speed(0)
	pad_b.shape("square")
	pad_b.color("white")
	pad_b.shapesize(stretch_wid=5 , stretch_len=1)
	pad_b.penup()
	pad_b.goto(350,0)
	#Ball
	ball = turtle.Turtle()
	ball.speed(0)
	ball.shape("square")
	ball.color("white")
	ball.penup()
	ball.goto(0,0)
	ball.dx = 1
	ball.dy = 1
	#score
	score_a = 0
	score_b = 0
	#score board
	pen = turtle.Turtle()
	pen.speed(0)
	pen.color('white')
	pen.penup()
	pen.hideturtle()
	pen.goto(0,300)
	pen.write("Player A : {}		Player B : {}".format(score_a,score_b) ,align = "center" , font=("Courier",24,"normal"))
	#function
	def pad_a_up():
		y = pad_a.ycor()
		if y >=240:
			return
		else:
			y+=20
			pad_a.sety(y)
	def pad_a_down():
		y = pad_a.ycor()
		if y <=-240:
			return
		else:
			y-=20
			pad_a.sety(y)
	def pad_b_up():
		y = pad_b.ycor()
		if y >=240:
			return
		else:
			y+=20
			pad_b.sety(y)
	def pad_b_down():
		y = pad_b.ycor()
		if y <=-240:
			return
		else:
			y-=20
			pad_b.sety(y)

	#Keyboard Binding
	wn.listen()
	wn.onkeypress(pad_a_up,'w')
	wn.onkeypress(pad_a_down,'s')
	wn.onkeypress(pad_b_up,'Up')
	wn.onkeypress(pad_b_down,'Down')
	#main game loop
	while True:
		wn.update()
		#move the ball
		ball.setx(ball.xcor()+ball.dx)
		ball.sety(ball.ycor()+ball.dy)

		#border checking
		if ball.ycor()>290:
			ball.sety(290)
			ball.dy*=-1
			#os.system("afplay bounce.wav&")
			winsound.Beep(800,20)
		if ball.ycor()<-290:
			ball.sety(-290)
			ball.dy*=-1
			winsound.Beep(800,20)
		if ball.xcor()>390:
			ball.goto(0,0)
			ball.dx*=-1
			score_a+=1
			pen.clear()
			pen.write("Player A : {}		Player B : {}".format(score_a,score_b) ,align = "center" , font=("Courier",24,"normal"))
			winsound.Beep(2000,20)
		if ball.xcor()<-390:
			ball.goto(0,0)
			ball.dx*=-1
			score_b+=1
			pen.clear()
			pen.write("Player A : {}		Player B : {}".format(score_a,score_b) ,align = "center" , font=("Courier",24,"normal"))
			winsound.Beep(2000,20)
		#Paddle and ball collision
		if (ball.xcor()>330 and ball.xcor() < 350) and (ball.ycor()<pad_b.ycor() +40 and ball.ycor() > pad_b.ycor() -40 ):
			ball.setx(330)
			ball.dx *=-1
			winsound.Beep(800,20)
		if (ball.xcor()< -330 and ball.xcor() > -350) and (ball.ycor()<pad_a.ycor() +40 and ball.ycor() > pad_a.ycor() -40 ):
			ball.setx(-330)
			ball.dx *=-1
			winsound.Beep(800,20)
		#Winner
		if (score_a - score_b >=5):
			ball.clear()
			pad_a.clear()
			pad_b.clear()
			pen.clear()
			pen.goto(0,0)
			pen.pensize(2)
			pen.write("Player A Wins",align = "center" , font=("Courier",26,"normal"))
			#turtle.done()
			turtle.exitonclick()
			break
		if (score_b - score_a >=5):
			ball.clear()
			pad_a.clear()
			pad_b.clear()
			pen.clear()
			pen.goto(0,0)
			pen.pensize(2)
			pen.write("Player B Wins",align = "center" , font=("Courier",26,"normal"))
			turtle.exitonclick()
			#wn.exitonclick()
			break
