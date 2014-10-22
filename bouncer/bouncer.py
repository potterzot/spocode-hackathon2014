from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.animation import Animation
from kivy.graphics import Color, Ellipse, Line
from kivy.vector import Vector
from kivy.clock import Clock
from random import random

class Bouncer(Widget):
    #velocity on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    gravity = NumericProperty(.01*-9.8)

    # This creates a shortcut for both velocities so we can reference ball.velocity    
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        vx,vy = self.velocity
        if vy==0: vy -= 0.2
        else: vy += self.gravity
        vel = Vector(vx,vy)
        self.velocity = vel.x, vel.y
        self.pos = vel + self.pos

class Balloon(Widget):
    score = NumericProperty(0)
    factor = NumericProperty(1.2)
    inflate = NumericProperty(1)

    def flate(self):
        sx,sy = self.size
        if self.inflate==0 and sy<1:
            pass #balloon disappears
        elif self.inflate==1 and sy<60:
            size = self.factor*Vector(sx,sy)
        if sy>60:
            self.inflate = 0
            size = Vector(sx,sy) * 1/self.factor

    def bounce_bouncer(self, bouncer):
        if self.collide_widget(bouncer):
            vx, vy = bouncer.velocity
            offset = (bouncer.center_y - self.center_y) / (self.height/2)
            vel = -1*.8*Vector(vx, vy)
            bouncer.velocity = vel.x, vel.y + offset

class BouncerGame(Widget):
    bouncer = ObjectProperty(None)
    balloon = ObjectProperty(None)

    def start(self, vel=(0,-1)):
        # Bouncer
        self.bouncer.center = (30,self.top-10)
        self.bouncer.velocity = Vector(vel)
        
        # Balloons
        self.balloon.center = (30, 10)
        
    def update(self, dt):
        self.bouncer.move()
        #self.flate(self.balloon)
        
        self.balloon.bounce_bouncer(self.bouncer)
        
        if (self.bouncer.y < 0):
            self.game_over()

    def on_touch_down(self, touch): 
        color = (random(), 1.0, 1.0)
        with self.canvas:
            #self.remove_widget(self.balloon)
            #d = 200.
            #speed = 0.5
            Color(*color, mode='hsv')
            self.balloon.color = color
            #self.balloon = Balloon()
            self.balloon.pos = (touch.x-1/2, touch.y-1/2)
            
            #pulse = AnimateBalloon(x=touch.x-d/2, y=touch.y-d/2, size=(d,d), t='out_circ', duration=speed)
            #pulse.start(balloon)
       
    def game_over(self):
        label = Label(text="GAME OVER\n Score: ")
        label.center = self.center
        self.add_widget(label)

class BouncerApp(App):
    def build(self):
        game = BouncerGame()
        game.start()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__=='__main__':
    BouncerApp().run()
