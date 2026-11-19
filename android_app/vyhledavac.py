from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

BARVA_TEXTU = (0, 0, 0, 1)
BARVA_TEXTU2 = (0.9, 0.9, 0.9, 1)
BARVA_TLACITKA = (0.25, 0.35, 0.45, 1)

class VyhledavacScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        layout.add_widget(
            Label(
                text="Vyhledávač",
                font_size=sp(24),
                color=BARVA_TEXTU,
                size_hint_y=None,
                height=dp(60)
            )
        )

        layout.add_widget(
            Label(
                text="Zde bude vyhledávač spojení",
                font_size=sp(16),
                color=BARVA_TEXTU
            )
        )

        self.add_widget(layout)
