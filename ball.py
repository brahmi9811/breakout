import turtle
import time

INITIAL_SPEED = 7
DIAMETER = 8
SPEED_MULT = 1.005

STARTX = 0
STARTY = 0
START_ANGLE = 45
MINX = -310
MAXX = -MINX
MAXY = 230
MINY = -230

class Ball (turtle.Turtle):
  def __init__(self, screen, x = STARTX, y = STARTY, head = START_ANGLE):
    '''
      Creates the ball at the given location and heading
      Assumes ball.gif is in the same directory
    '''
    turtle.Turtle.__init__(self)
    screen.addshape('ball.gif')
    self.shape('ball.gif')
  def width(self):
    '''Returns object width'''
    return WIDTH
  def height(self):
    '''Returns object height'''
    return HEIGHT
  def hits(self, obj):
    '''Returns whether ball hits given object'''
    return False
  def animate(self):
    '''
      Animates the ball
      Moves forward based on speed and heading
      Will bounce off left, right, or top walls
    '''
    pass
  def hbounce(self):
    '''
      Bounces horizontally, changing direction and increasing speed by 0.5%
    '''
    pass
  def vbounce(self):
    '''
      Bounces vertically, changing direction and increasing speed by 0.5%
    '''
    pass
  def has_lost(self):
    '''Returns whether the player has lost (y position < MINY)'''
    return True

if __name__ == '__main__':
  # Simple demo (bounces twice and ends at bottom)
  screen = turtle.Screen()
  screen.setup(640, 480)
  ball = Ball(screen)

  while not ball.has_lost():
    ball.animate()
    time.sleep(0.005)
  screen.bye()
  
