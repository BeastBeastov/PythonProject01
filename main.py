from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from kivy.config import Config

Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '500')
Config.set('kivy', 'exit_on_escape', '1')

from kivy.uix.textinput import TextInput


class LoginScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass

class PoolskeeperApp(App):

    def start(self, instance):
        self.login_input.text = ''
        self.login_input.hint_text = 'логин'
        self.pwd_input.text = ''
        self.pwd_input.hint_text = 'пароль'
        self.sm.current = 'login'
        self.sm.transition.direction = 'right'
        # self.sm.switch_to('manu', direction='left')
        print('Начало')

    def login(self, instance):
        if self.login_text =='admin' and self.pwd_text == 'admin':
            self.sm.current = 'menu'
            self.sm.transition.direction = 'left'
            print('Выполняется вход' + self.login_text +':'+self.pwd_text)
        elif self.login_text =='' and self.pwd_text == '':
            self.sm.current = 'menu'
            self.sm.transition.direction = 'left'
            print('Выполняется вход без пароля!')
        else:
            pass

    def settings(self, instance):
        self.sm.current = 'settings'
        self.sm.transition.direction = 'left'
        print('Настройки')

    def menu(self, instance):
        self.sm.current = 'menu'
        self.sm.transition.direction = 'right'
        print('Меню')

    def profile(self, instance):
        self.sm.current = 'profile'
        self.sm.transition.direction = 'right'
        # self.sm.switch_to('manu', direction='left')
        print('Профиль')

    def on_login(self, instance, *args):
        self.login_text = instance.text

    def on_pwd(self, instance, *args):
        self.pwd_text = instance.text

    def calc(self, instance):
        print('Рассчеты')

    def projects(self, instance):
        print('Проекты')

    def build(self):
        self.sm = ScreenManager()

        ls = LoginScreen(name='login')
        ls.add_widget(Image(source='pool.png'))
        bl = BoxLayout(orientation='vertical', padding=10, spacing=5, size_hint=[1, 0.3])
        self.login_input = TextInput(hint_text='логин')
        self.login_text = ''
        self.login_input.bind(text=self.on_login)
        bl.add_widget(self.login_input)
        self.pwd_input = TextInput(hint_text='пароль', password=True, password_mask='*')
        self.pwd_text = ''
        self.pwd_input.bind(text=self.on_pwd)
        bl.add_widget(self.pwd_input)
        enter_button = Button(text='Войти', on_press=self.login)
        bl.add_widget(enter_button)
        ls.add_widget(bl)
        self.sm.add_widget(ls)

        ms = MenuScreen(name='menu')
        gl = GridLayout(rows=7, spacing=5, padding=10)
        gl.add_widget(Label(text='Меню', font_size=30, color=(1, 1, 0, 1), bold=True))
        sb = Button(text='Настройки', on_press=self.settings)
        gl.add_widget(sb)
        сb = Button(text='Рассчеты', on_press=self.calc)
        gl.add_widget(сb)
        pb = Button(text='Проекты', on_press=self.projects)
        gl.add_widget(pb)
        fb = Button(text='Кнопка 5')
        gl.add_widget(fb)
        eb = Button(text='Выход', on_press=self.start)
        gl.add_widget(eb)
        ms.add_widget(gl)
        self.sm.add_widget(ms)

        ss = SettingsScreen(name='settings')
        gl = GridLayout(rows=7, spacing=5, padding=10)
        gl.add_widget(Label(text='Настройки', font_size=30, color=(1, 1, 0, 1), bold=True))
        mb = Button(text='Меню', on_press=self.menu)
        gl.add_widget(mb)
        pb = Button(text='Профиль', on_press=self.profile)
        gl.add_widget(pb)
        fb = Button(text='Кнопка 4')
        gl.add_widget(fb)
        fb = Button(text='Кнопка 5')
        gl.add_widget(fb)
        eb = Button(text='Выход', on_press=self.start)
        gl.add_widget(eb)
        ss.add_widget(gl)
        self.sm.add_widget(ss)

        ps = ProfileScreen(name='profile')
        gl = GridLayout(rows=7, spacing=5, padding=10)
        gl.add_widget(Label(text='Профиль', font_size=30, color=(1, 1, 0, 1), bold=True))
        sb = Button(text='Настройки', on_press=self.settings)
        gl.add_widget(sb)
        mb = Button(text='Меню', on_press=self.menu)
        gl.add_widget(mb)
        eb = Button(text='Выход', on_press=self.start)
        gl.add_widget(eb)
        ps.add_widget(gl)

        self.sm.add_widget(ps)

        return self.sm


if __name__ == '__main__':
    PoolskeeperApp().run()
