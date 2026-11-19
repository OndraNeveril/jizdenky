from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, NoTransition

import database
from jizdenky import JizdenkyScreen
from vyhledavac import VyhledavacScreen

BARVA_TEXTU = (0, 0, 0, 1)
BARVA_TEXTU2 = (0.9, 0.9, 0.9, 1)
BARVA_TLACITKA = (0.25, 0.35, 0.45, 1)

class JizdenkyApp(App):
    def build(self):
        database.init_db()

        Window.clearcolor = (0.95, 0.96, 0.97, 1)

        root = BoxLayout(
            orientation="vertical",
            spacing=dp(0)
        )

        self.obrazovky = ScreenManager(
            transition=NoTransition()
        )

        self.obrazovky.add_widget(
            JizdenkyScreen(name="jizdenky")
        )

        self.obrazovky.add_widget(
            VyhledavacScreen(name="vyhledavac")
        )

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
                background_color=BARVA_TLACITKA,
                on_release=lambda instance: self.prepnout("jizdenky")
            )
        )

        navigace.add_widget(
            Button(
                text="Vyhledávač",
                font_size=sp(16),
                background_normal="",
                background_color=BARVA_TLACITKA,
                on_release=lambda instance: self.prepnout("vyhledavac")
            )
        )

        root.add_widget(navigace)

        return root

    def prepnout(self, obrazovka):
        self.obrazovky.current = obrazovka


if __name__ == "__main__":
    JizdenkyApp().run()
