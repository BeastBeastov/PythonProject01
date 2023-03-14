from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

# Разрешение экрана телефона 1440х3200
Window.size = (288, 540)

def login():
    print('Попал в логин')

class Container(ScreenManager):

    def start(self):
        self.login.text = ''
        self.login.hint_text = 'логин'
        self.pwd.text = ''
        self.pwd.hint_text = 'пароль'
        self.current = 'login'
        self.transition.direction = 'right'
        # self.switch_to('manu', direction='left')
        print('Начало')

    def startlogin(self):
        if self.login.text == 'admin' and self.pwd.text == 'admin':
            self.current = 'menu'
            self.transition.direction = 'left'
            print('Выполняется вход : ' + self.login.text)
        elif self.login.text == '' and self.pwd.text == '':
            self.current = 'menu'
            self.transition.direction = 'left'
            print('Выполняется вход без пароля!')
        else:
            pass
    def settings(self):
        self.current = 'settings'
        self.transition.direction = 'left'
        print('Настройки')

    def menu(self):
        self.current = 'menu'
        self.transition.direction = 'right'
        print('Меню')

    def profile(self):
        self.current = 'profile'
        self.transition.direction = 'right'
        # self.sm.switch_to('manu', direction='left')
        print('Профиль')

    def on_login(self, instance, *args):
        self.login.text = instance.text

    def on_pwd(self, instance, *args):
        self.pwd.text = instance.text

    def calcs(self):
        print('Рассчеты')

    def projects(self):
        print('Проекты')

class PoolToolApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    PoolToolApp().run()
