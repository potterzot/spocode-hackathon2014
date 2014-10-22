from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.core.audio import SoundLoader
from kivy.base import EventLoop

class Zombie(Widget):
    pass


class Human(Widget):
    # Move function moves the ball one step, called at equal intervals to animate
    def move(self, touch):
        self.pos += (touch.x, touch.y)


class FindMeGame(Widget):
    score = NumericProperty(0)
    player1 = ObjectProperty(None)
    #startmenu = ObjectProperty(None)
    #player2 = ObjectProperty(None)
    running = False
    
    def update(self, dt):
        #self.zombies.move()        
        pass
    
    def on_touch_move(self, touch):
        #if touch.y > self.
        self.player1.center_y += touch.y
        self.player1.center_x += touch.x
        #self.player1.move(touch)          

    def start(self):
        pass


class StartMenu(Widget):

    def on_button_release(self, *args):
        pass

    def callback(self, instance):
        print("The button %s is being pressed" % instance.text)

    def add_buttons(self, button_list):
        self.layout = BoxLayout(orientation='vertical')
        for button in button_list:
            tmpbtn = Button(text=button)
            tmpbtn.bind(on_release = self.callback)
            self.layout.add_widget(tmpbtn)


class FindMeApp(App):
    def __init__(self, **kwargs):
        super(FindMeApp, self).__init__(**kwargs)
        self.sounds = {
            #'': SoundLoader.load('snd/file.wav')
            }
        self.players = 2
  
    def pause_game(self, *args):
        self.game.running = False
    
    def continue_game(self, *args):
        self.game.running = True
   
    def restart_game(self):
        build_level()
        self.game.running = True

    def build(self):
        #parent = Widget()
        self.game = FindMeGame(app=self)

        # main window to hold all widgets
        EventLoop.ensure_window()
        self.window = EventLoop.window()
        self.main = Widget(app=self, size=self.window.size)

        # Add game widget to main window
        self.main.add_widget(self.game) 
        
        #menu = StartMenu()
        #menu.add_buttons(['Start', 'About'])

        #parent.add_widget(game)
        #parent.add_widget(menu)
        #Clock.schedule_interval(game.update, 1.0/60.0)
        return self.main


if __name__=='__main__':
    FindMeApp().run()
