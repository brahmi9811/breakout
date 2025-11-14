import turtle

SPEED = 10
HEIGHT = 10
WIDTH = 70

STARTX = 0
STARTY = -200
MINX = -280
MAXX = -MINX

LEFT = -1
RIGHT = 1
NEUTRAL = 0

class Paddle(turtle.Turtle):
    def __init__(self, screen, x=STARTX, y=STARTY):
        turtle.Turtle.__init__(self)

        # Load the paddle image
        screen.addshape("paddle.gif")
        self.shape("paddle.gif")
        self.penup()

        # Position
        self.goto(x, y)

        # Default state
        self.state = NEUTRAL

        # Key bindings
        screen.onkeypress(self.left, "Left")
        screen.onkeypress(self.right, "Right")
        screen.onkeyrelease(self.release, "Left")
        screen.onkeyrelease(self.release, "Right")

    def animate(self):
        """Move paddle left/right depending on state."""
        if self.state == LEFT:
            new_x = self.xcor() - SPEED
            if new_x >= MINX:
                self.setx(new_x)

        elif self.state == RIGHT:
            new_x = self.xcor() + SPEED
            if new_x <= MAXX:
                self.setx(new_x)

    def left(self, amt=SPEED):
        self.state = LEFT

    def right(self, amt=SPEED):
        self.state = RIGHT

    def release(self):
        self.state = NEUTRAL

    def width(self):
        return WIDTH

    def height(self):
        return HEIGHT

    def hit_ball(self, ball):
        """
        Bounce the ball depending on where it hits the paddle.
        If hit at center → 90° (straight up).
        Otherwise adjust based on deltaX.
        """
        ball_x = ball.xcor()
        paddle_x = self.xcor()

        deltaX = ball_x - paddle_x  # negative left, positive right

        # Map this to an angle change (simple scaling factor)
        angle_offset = deltaX * 1.2

        # Base bounce straight upward
        new_heading = 90 + angle_offset

        ball.setheading(new_heading)


# -----------------------------------------
# DEMO
# -----------------------------------------
def make_paddle(screen):
    global paddle
    paddle = Paddle(screen)
    return paddle

if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(640, 480)

    paddle = make_paddle(screen)

    def animate_loop():
        paddle.animate()
        screen.ontimer(animate_loop, 10)

    screen.listen()
    screen.onkey(screen.bye, "Escape")

    screen.ontimer(animate_loop, 10)
    screen.mainloop()