#program print out a random color picture using a turtle library


from random import choice,randint
from turtle import Turtle, Screen
import turtle as t

# list for the turtle movement

directions = ["0", "90", "180", "270"]

tim = Turtle()
tim.pen(pensize=10)
screen = Screen()

#Changing the color mode to 0 - 255

t.colormode(255)

#function to create an RGB color scheme for pencolor
def color_mode():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)

  rand_color = (r,g,b)
  return rand_color

for i in range(255):
  
  tim.pencolor(color_mode())
  tim.forward(20)
  tim.seth(float(choice(directions)))
   

