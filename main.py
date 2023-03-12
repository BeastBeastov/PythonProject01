from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.config import Config

Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '500')

# Создайте оба экрана. Обратите внимание на root.manager.current: вот как
# вы можете управлять ScreenManager из kv. Каждый экран по умолчанию имеет
# менеджер свойств, который дает вам экземпляр используемого ScreenManager.

Builder.load_string("""
<LoginScreen>:
    Image:
        source: 'pool.png'
        valign: 'top'
    BoxLayout:
        orientation: 'vertical'
        valign: 'top'
        padding: 10
        spacing: 10
        size_hint: [1, 0.3]
        TextInput:
            text: 'Логин : '
        TextInput:
            text: 'Пароль : '    
        Button:
            text: 'Войти'
            on_press: 
                root.manager.current = 'menu'
                root.manager.transition.direction = 'left'

<MenuScreen>:
    GridLayout:
        rows: 3
        Button:
            text: 'Settings'
            on_press: 
                root.manager.current = 'settings'
                root.manager.transition.direction = 'left'
        Button:
            text: 'Menu'
            on_press: 
                root.manager.current = 'menu'
                root.manager.transition.direction = 'right'
        Button:
            text: 'Pass'
        Button:
            text: 'Pass'
        Button:
            text: 'Pass'
        Button:
            text: 'Login'
            on_press: 
                root.manager.current = 'login'
                root.manager.transition.direction = 'right'
    

<SettingsScreen>:
    GridLayout:
        rows: 3
        Button:
            text: 'Settings'
            on_press: 
                root.manager.current = 'settings'
                root.manager.transition.direction = 'right'
        Button:
            text: 'Menu'
            on_press: 
                root.manager.current = 'menu'
                root.manager.transition.direction = 'right'
        Button:
            text: 'Pass'
        Button:
            text: 'Pass'
        Button:
            text: 'Pass'
        Button:
            text: 'Login'
            on_press: 
                root.manager.current = 'login'
                root.manager.transition.direction = 'left'

""")

# Declare both screens
class LoginScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))


class PoolskeeperApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    PoolskeeperApp().run()
