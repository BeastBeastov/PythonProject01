"""
Created on Sat Mar 11 01:04:39 2023

@author: Alexey Ovsyannikov
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Ellipse
from random import randint
from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')


class PainterWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            r = randint(0, 25) / 25
            g = randint(0, 25) / 25
            b = randint(0, 25) / 25
            a = 1
            Color(r, g, b, a)
            r = 20
            Ellipse(pos=(touch.x - r / 2, touch.y - r / 2), size=(r, r))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=10)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)
class CanvasApp(App):

    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        parent.add_widget(self.painter)
        parent.add_widget(Button(text='Clear', on_press=self.clear_canvas,
                                 size=(100, 50)))
        parent.add_widget(Button(text='Save', on_press=self.save,
                                 size=(100, 50), pos=(100, 0)))
        parent.add_widget(Button(text='Screen', on_press=self.screen,
                                 size=(100, 50), pos=(200, 0)))

        return parent

    def clear_canvas(self, instance):
        self.painter.canvas.clear()

    def save(self, instance):
        self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png('image.png')

    def screen(self, instance):
        Window.screenshot('screen.png')


if __name__ == "__main__":
    CanvasApp().run()