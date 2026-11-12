from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager


class JizdenkyApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.96, 0.97, 1)

        root = BoxLayout(
            orientation="vertical",
            spacing=dp(0)
        )

        self.obrazovky = ScreenManager()

        jizdenky = Screen(name="jizdenky")
        jizdenky_layout = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )
        jizdenky_layout.add_widget(
            Label(
                text="Jízdenky",
                font_size=sp(24),
                color=(0.15, 0.2, 0.25, 1),
                size_hint_y=None,
                height=dp(60)
            )
        )
        jizdenky_layout.add_widget(
            Label(
                text="Zde bude seznam jízdenek",
                font_size=sp(16),
                color=(0.15, 0.2, 0.25, 1)
            )
        )
        jizdenky.add_widget(jizdenky_layout)

        vyhledavac = Screen(name="vyhledavac")
        vyhledavac_layout = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )
        vyhledavac_layout.add_widget(
            Label(
                text="Vyhledávač",
                font_size=sp(24),
                color=(0.15, 0.2, 0.25, 1),
                size_hint_y=None,
                height=dp(60)
            )
        )
        vyhledavac_layout.add_widget(
            Label(
                text="Zde bude vyhledávač spojení",
                font_size=sp(16),
                color=(0.15, 0.2, 0.25, 1)
            )
        )
        vyhledavac.add_widget(vyhledavac_layout)

        self.obrazovky.add_widget(jizdenky)
        self.obrazovky.add_widget(vyhledavac)

        root.add_widget(self.obrazovky)

        navigace = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(60),
            spacing=dp(1)
        )

        navigace.add_widget(
            Button(
                text="Jízdenky",
                font_size=sp(16),
                background_normal="",
                background_color=(0.25, 0.35, 0.45, 1),
                on_release=lambda instance: self.prepnout("jizdenky")
            )
        )

        navigace.add_widget(
            Button(
                text="Vyhledávač",
                font_size=sp(16),
                background_normal="",
                background_color=(0.25, 0.35, 0.45, 1),
                on_release=lambda instance: self.prepnout("vyhledavac")
            )
        )

        root.add_widget(navigace)

        return root

    def prepnout(self, obrazovka):
        self.obrazovky.current = obrazovka


if __name__ == "__main__":
    JizdenkyApp().run()