import turtle
import math

WIDTH = 60
HEIGHT = 20

ROWS = 4
COLS = 10
START_X = -270
START_Y = 100

bricks = []


def make_bricks(screen):
    """
    Makes all of the bricks for Breakout:
    4 rows × 10 columns starting at (-270, 100)
    """
    global bricks
    bricks = []

    screen.addshape("brick.gif")

    T = turtle.Turtle()
    T.hideturtle()
    T.penup()
    T.speed(0)
    T.shape("brick.gif")

    for row in range(ROWS):
        for col in range(COLS):
            x = START_X + col * WIDTH
            y = START_Y + row * HEIGHT
            T.goto(x, y)
            bricks.append(Brick(T))


def check_hit(ball):
    """
    Checks whether the ball hits any brick.
    If a brick is hit:
      * Determine bounce direction using deltaX, deltaY
      * Remove the brick
      * Return True
    """
    global bricks

    for b in bricks:
        if ball.hits(b):
            # Determine bounce direction
            dx = ball.xcor() - b.xcor()
            dy = ball.ycor() - b.ycor()

            # Horizontal bounce if abs(dx) >= 3 * abs(dy)
            if abs(dx) >= 3 * abs(dy):
                ball.hbounce()
            else:
                ball.vbounce()

            # Remove brick
            b.destroy()
            bricks.remove(b)

            return True

    return False


def has_won():
    """Return True if no bricks remain."""
    return len(bricks) == 0


class Brick:
    def _init_(self, T):
        """
        Creates a brick by stamping the given turtle.
        Stores the position and stamp id.
        """
        self.T = T
        self.x = T.xcor()
        self.y = T.ycor()
        self.id = T.stamp()

    def xcor(self):
        return self.x

    def ycor(self):
        return self.y

    def width(self):
        return WIDTH

    def height(self):
        return HEIGHT

    def destroy(self):
        """Erase this brick's stamp."""
        self.T.clearstamp(self.id)