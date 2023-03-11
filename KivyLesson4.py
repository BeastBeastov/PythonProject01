"""
Created on Sat Mar 11 01:04:39 2023

@author: Alexey Ovsyannikov
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Line, Color, Rectangle, Ellipse

from kivy.config import Config

Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')


class PainterWidget(Widget):
    def __init__(self, **kwargs):
        super(PainterWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 1, 1, 1)
            Ellipse(pos=(100, 100), size=(50, 50))
            Color(1, 1, 0, 1)
            Rectangle(pos=(150, 300), size=(40, 120))
            Color(0, 1, 0, 1)
            # Line(points=(50,50,50,170,230,170,250,430,50,50), close=True)
            self.line = Line(points=(), width=10, joint='miter', cap='square')

    def on_touch_down(self, touch):
        self.line.points += (touch.x, touch.y)


class CanvasApp(App):

    def build(self):
        return PainterWidget()


if __name__ == "__main__":
    CanvasApp().run()