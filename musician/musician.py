from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.bubble import Bubble
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Ellipse, Line
from kivy.animation import Animation

from random import random



class AnimateBeat(Animation):
    pass

class MusicianBeat(Widget):
    pass 

class MusicianGame(Widget):
    def on_touch_down(self, touch):
        color = (random(), 1.0, 1.0)
        with self.canvas:
            d = 200.
            speed = 0.5
            Color(*color, mode='hsv')
            beat = MusicianBeat()
            beat.pos = (touch.x-1/2, touch.y-1/2)
            pulse = AnimateBeat(x=touch.x-d/2, y=touch.y-d/2, size=(d,d), t='out_circ', duration=speed)
            pulse.start(beat)
            self.remove_widget(beat)

class MusicianApp(App):
    def build(self):
        parent = Widget()
        game = MusicianGame()

        parent.add_widget(game)
        return parent

if __name__=='__main__':
    MusicianApp().run()
