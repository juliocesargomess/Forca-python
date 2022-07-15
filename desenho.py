import turtle
from turtle import *

def fazerX():
  i = 0
  angulo = 30
  while i < 4:
    turtle.setheading(angulo)
    turtle.forward(8)
    turtle.backward(8)
    i += 1
    angulo += 90
  return

def forcaVazia():
  janela = Screen()
  janela.setup(800, 600)
  janela.title('Jogo da Forca')
  janela.bgcolor('white')

  turtle.hideturtle()
  turtle.penup()
  turtle.speed(0)
  turtle.setposition(-300,-180)
  turtle.color('orange')
  turtle.width('10')
  turtle.pendown()
  turtle.goto(120,-180)
  turtle.goto(-250,-180)
  turtle.goto(-250,190)
  turtle.goto(-45,190)
  turtle.width('4')
  turtle.goto(-65,190)
  turtle.goto(-65,130)
  turtle.penup()
  turtle.goto(-65,110) #circulo corda
  turtle.pendown()
  turtle.fillcolor()
  turtle.circle(10)

def testeErros(erros):
  if erros == 1:
    turtle.penup()
    turtle.goto(-65,120)
    turtle.pendown()
    turtle.color('blue')
    turtle.circle(25)
  elif erros == 2:
    turtle.goto(-65,25)
  elif erros == 3:
    turtle.goto(-65,90)
    turtle.setheading(345)
    turtle.forward(70)
    turtle.backward(70)
  elif erros == 4:
    turtle.setheading(195)
    turtle.forward(70)
    turtle.backward(70)
  elif erros == 5:
    turtle.goto(-65,25)
    turtle.setheading(315)
    turtle.forward(100)
    turtle.backward(100)
  elif erros == 6:
    turtle.setheading(225)
    turtle.forward(100)
    turtle.backward(100)
    #OLHOS
    turtle.goto(-65,90)
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(55)
    turtle.setheading(180)
    turtle.forward(12)
    turtle.pendown()
    fazerX()
    turtle.penup()
    turtle.setheading(360)
    turtle.forward(24)
    turtle.pendown()
    fazerX()

