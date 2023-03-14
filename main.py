
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
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.properties import ObjectProperty


# Разрешение экрана телефона 1440х3200
# Window.size = (288, 540)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

# from kivymd.theming import ThemeManager

class Container(ScreenManager):

    login = ObjectProperty()
    pwd = ObjectProperty()
    def calc_formwork_materials(self):
        l = float(self.length1.text)
        w = float(self.width1.text)
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
        l = float(self.length2.text)
        w = float(self.width2.text)
        M = local_materials(l, w)
        self.concrete.text = str(M[0])+' куб.м.'
        self.steel.text = str(M[1])+' п.м.\n'+str(M[2])+' п.м.'
        self.stone.text = str(M[3])+' куб.м.'
        self.sand.text = str(M[4])+' куб.м.'
        self.block.text = str(M[5])+' шт.'
        self.plaster.text = str(M[6])+' меш.'
        self.putty.text = str(M[7])+' меш.'
        self.glue.text = str(M[8])+' меш.'


    def start(self):
        self.login.text = ''
        self.login.hint_text = 'логин'
        self.pwd.text = ''
        self.pwd.hint_text = 'пароль'
        self.current = 'login'
        self.transition.direction = 'right'
        # self.switch_to('manu', direction='left')
        # print('Начало')
    def startlogin(self):
        if self.login.text == 'admin' and self.pwd.text == 'admin':
            self.current = 'menu'
            self.transition.direction = 'left'
            # print('Выполняется вход : ' + self.login.text)
        elif self.login.text == '' and self.pwd.text == '':
            self.current = 'menu'
            self.transition.direction = 'left'
            # print('Выполняется вход без пароля!')
        else:
            pass
    def settings(self):
        self.current = 'settings'
        self.transition.direction = 'left'
        # print('Настройки')
    def menu(self):
        self.current = 'menu'
        self.transition.direction = 'right'
        # print('Меню')
    def profile(self):
        self.current = 'profile'
        self.transition.direction = 'right'
        # print('Профиль')
    def calcs(self):
        self.current = 'calcs'
        self.transition.direction = 'left'
        # print('Рассчеты')
    def back_to_calcs(self):
        self.current = 'calcs'
        self.transition.direction = 'right'
        # print('Рассчеты')
    def on_login(self, instance, *args):
        self.login.text = ''
    def on_pwd(self, instance, *args):
        self.pwd.text = ''
    def projects(self):
        # print('Проекты')
    def form_mc(self):
        self.current = 'form_mc'
        self.transition.direction = 'left'
        # print('Расчет материалов опалубки')
    def local_mc(self):
        self.current = 'local_mc'
        self.transition.direction = 'left'
        # print('Расчет местных стройматериалов')
    def face_mc(self):
        # print('Расчет облицовочных материалов')
    def wsc(self):
        # print('Расчет работ и услуг')

class PoolToolApp(App):
    #theme_cls = ThemeManager()
    #title = 'PoolTool'
    def build(self):
        # self.theme_cls.theme_style = 'Light'
        return Container()


if __name__ == '__main__':
    PoolToolApp().run()
