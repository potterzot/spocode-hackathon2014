from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from random import random

class PaintGame(Widget):
    def on_touch_down(self, touch):
        color = (random(), 1.0, 1.0)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 10.
            #Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y] 

class PaintApp(App):
    def build(self):
        parent = Widget()
        painter = PaintGame()
        clearbtn = Button(text='Clear')
        parent.add_widget(painter)
        parent.add_widget(clearbtn)

        def clear_canvas(obj):
            painter.canvas.clear()
        clearbtn.bind(on_release=clear_canvas)
        return parent

if __name__=='__main__':
    PaintApp().run()
