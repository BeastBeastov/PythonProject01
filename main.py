
"""
Created on Mon Feb 13 00:26:50 2023

@author: Alexey Ovsyannikov

Этот проект должен реализовать рабочее приложение для телефона андроид.
Приложение должно включать постоянно пополняемый и обновляемый набор
функций для применения и приложения инженерных расчетов для работы по
строительству бассейнов.
"""

from workmod import *
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Ellipse
from random import randint
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

# Разрешение экрана телефона 1440х3200 или 720х1480
#Window.size = (360, 700)
#Window.top = 20
#Window.left = 500

from kivymd.theming import ThemeManager
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDRaisedButton

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
    def clear_canvas(self):
        self.canvas.clear()
    def save(self):
        self.size = (Window.size[0], Window.size[1])
        self.export_to_png('image.png')

class Container(ScreenManager):

    def calc_formwork_materials(self):
        l = float(self.length1.text) if self.length1.text else 0
        w = float(self.width1.text) if self.width1.text else 0
        P = 2 * l + 2 * w
        M = formwork_materials(P)
        self.perimeter.text = str(P) + ' п.м.'
        self.metal_profile.text = str(M[0]) + ' п.м.'
        self.buttress.text = str(M[1]) + ' компл.'
        self.bolts.text = str(M[2][0])+' шт.\n'+str(M[2][1])+' кг.'
        self.nuts.text = str(M[3][0])+' шт.\n'+str(M[3][1])+' кг.'
        self.washers.text = str(M[4][0])+' шт.\n'+str(M[4][1])+' кг.'
        self.screws.text = str(M[5])+' шт.'
    def calc_local_materials(self):
        l = float(self.length2.text) if self.length2.text else 0
        w = float(self.width2.text) if self.width2.text else 0
        M = local_materials(l, w)
        self.concrete.text = str(M[0])+' куб.м.'
        self.steel.text = str(M[1])+' п.м.\n'+str(M[2])+' п.м.'
        self.stone.text = str(M[3])+' куб.м.'
        self.sand.text = str(M[4])+' куб.м.'
        self.block.text = str(M[5])+' шт.'
        self.plaster.text = str(M[6])+' меш.'
        self.putty.text = str(M[7])+' меш.'
        self.glue.text = str(M[8])+' меш.'
    def calc_face_materials(self):
        l = float(self.length3.text) if self.length3.text else 0
        w = float(self.width3.text) if self.width3.text else 0
        M = face_materials(l, w)
        self.liner.text = str(M[0])+' кв.м.'
        self.corner.text = str(M[1])+' п.м.'
        self.liquid.text = str(M[2])+' шт.'
        self.dowel.text = str(M[3])+' шт.'
        self.side_stone.text = str(M[4])+' шт.'
        self.grout.text = str(M[5])+' меш.'
        self.silicone.text = str(M[6]) + ' шт.'

    def calc_length_per_roll(self):
        D = float(self.diametr1.text) if self.diametr1.text else 0
        d = float(self.diametr.text) if self.diametr.text else 0
        thickness = float(self.thickness.text) if self.thickness.text else 1.5
        L = linerlen(D, d, thickness)
        self.lenroll.text = 'В этом рулоне ' + str(L) + ' п.м.'

    def start(self):
        self.length1.text = self.width1.text = ''
        self.length2.text = self.width2.text = ''
        self.length3.text = self.width3.text = ''
        self.diametr1.text = self.diametr.text = ''
        self.login.text = self.pwd.text = ''
        self.login.hint_text = 'логин'
        self.pwd.hint_text = 'пароль'
        self.current = 'login'
        self.transition.direction = 'right'
    def startlogin(self):
        if self.login.text == '' and self.pwd.text == '':
            self.current = 'menu'
            self.transition.direction = 'left'
        else:
            pass
    def settings(self):
        if self.current != 'menu':
            self.transition.direction = 'right'
        else:
            self.transition.direction = 'left'
        self.current = 'settings'
    def menu(self):
        self.current = 'menu'
        self.transition.direction = 'right'
    def profile(self):
        self.current = 'profile'
        self.transition.direction = 'left'

    def show_theme_picker(self):
        #theme_dialog = MDColorPicker()
        #theme_dialog.open()
        pass
    def theme(self):
        self.current = 'theme'
        self.transition.direction = 'left'
        # self.show_theme_picker()
    def calcs(self):
        self.current = 'calcs'
        self.transition.direction = 'left'
    def back_to_calcs(self):
        self.current = 'calcs'
        self.transition.direction = 'right'
    def on_login(self, instance, *args):
        self.login.text = ''
    def on_pwd(self, instance, *args):
        self.pwd.text = ''
    def projects(self):
        pass
    def painter(self):
        self.current = 'painter'
        self.transition.direction = 'left'
    def form_mc(self):
        self.current = 'form_mc'
        self.transition.direction = 'left'
    def local_mc(self):
        self.current = 'local_mc'
        self.transition.direction = 'left'
    def face_mc(self):
        self.current = 'face_mc'
        self.transition.direction = 'left'
    def len_mc(self):
        self.current = 'liner'
        self.transition.direction = 'left'
    def wsc(self):
        pass

class PoolToolApp(MDApp):
    title = 'PoolTool'
    def build(self):
        paletts = ['Red', 'Pink', 'Purple', 'DeepPurple',
                   'Indigo', 'Blue', 'LightBlue', 'Cyan',
                   'Teal', 'Green', 'LightGreen', 'Lime',
                   'Yellow', 'Amber', 'Orange', 'DeepOrange',
                   'Brown', 'Gray', 'BlueGray']
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.primary_hue = "700"  # "500"
        self.theme_cls.theme_style = 'Light'
        return Container()

if __name__ == '__main__':
    PoolToolApp().run()
