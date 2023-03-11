from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Application(App):
    def build(self):
        main_layout = BoxLayout()

        butt = Button(text='Нажми', font_size=25, background_color="magenta")
        another_butt = Button(text='Не нажимай', font_size=25, background_color="cyan")

        main_layout.add_widget(butt)
        main_layout.add_widget(another_butt)

        return main_layout


if __name__ == "__main__":
    Application().run()
