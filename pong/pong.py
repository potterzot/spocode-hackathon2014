from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.clock import Clock
from random import randint

class PongBall(Widget):
    #velocity on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # This creates a shortcut for both velocities so we can reference ball.velocity    
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Move function moves the ball one step, called at equal intervals to animate
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height/2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

class PongButton(Widget):

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    
    def serve_ball(self, vel=(4,0)):
        self.ball.center = self.center
        self.ball.velocity = Vector(vel).rotate(randint(0,360))

    def update(self, dt):
        self.ball.move()

        # Bounce off paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # Bounce off the top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        
        # Score a point
        if self.ball.x < self.x:
            self.player2.score +=1
            self.serve_ball(vel=(4,0))
        if self.ball.x > self.width:
            self.player1.score +=1
            self.serve_ball(vel=(4,0))
         
    def on_touch_move(self, touch): 
        # if touch is the left 3rd, adjust player 1
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        # if the right 3rd, adjust player 2
        if touch.x < self.width - self.width/3:
            self.player2.center_y = touch.y

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
