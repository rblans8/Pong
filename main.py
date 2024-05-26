from kivy.app import App
from kivy.uix.widget import Widget

''' from: https://kivy.org/doc/stable/tutorials/pong.html
'''

class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()
    

if __name__ == '__main__':
    PongApp().run()

