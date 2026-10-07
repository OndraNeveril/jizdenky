from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from datetime import datetime

import database


class JizdenkyApp(App):
    def build(self):
        root = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )

        root.add_widget(Label(
            text='Přidat jízdenku:',
            font_size=20,
            size_hint_y=None,
            height=50
        ))

        buttons = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=100,
            spacing=10
        )

        buttons.add_widget(Button(
            text='Přidat jednorázovou jízdenku',
            font_size=16
        ))

        buttons.add_widget(Button(
            text='Přidat časovou jízdenku',
            font_size=16
        ))

        root.add_widget(buttons)

        root.add_widget(Label(
            text='Jízdenky',
            font_size=24,
            size_hint_y=None,
            height=60
        ))

        seznam = GridLayout(
            cols=4,
            size_hint_y=None,
            spacing=2
        )
        seznam.bind(minimum_height=seznam.setter('height'))

        for text in ['dopravce', 'datum', 'cíl', 'místo']:
            seznam.add_widget(Label(
                text=text,
                bold=True,
                size_hint_y=None,
                height=40
            ))

        for jizdenka in database.get_jednorazove():
            seznam.add_widget(Label(
                text=jizdenka[1],
                size_hint_y=None,
                height=40
            ))
            seznam.add_widget(Label(
                text=f'{datetime.strptime(jizdenka[2], "%Y-%m-%d").strftime("%d. %m. %Y")}    {jizdenka[3]}',
                size_hint_y=None,
                height=40
            ))
            seznam.add_widget(Label(
                text=jizdenka[5],
                size_hint_y=None,
                height=40
            ))
            seznam.add_widget(Label(
                text=jizdenka[7] or '',
                size_hint_y=None,
                height=40
            ))

        scroll = ScrollView()
        scroll.add_widget(seznam)
        root.add_widget(scroll)

        root.add_widget(Label(
            text='Časové jízdenky',
            font_size=24,
            size_hint_y=None,
            height=60
        ))

        seznam2 = GridLayout(
            cols=4,
            size_hint_y=None,
            spacing=2
        )
        seznam2.bind(minimum_height=seznam2.setter('height'))

        for text in ['dopravce', 'začátek', 'konec', 'zóny']:
            seznam2.add_widget(Label(
                text=text,
                bold=True,
                size_hint_y=None,
                height=40
            ))

        for jizdenka in database.get_casove():
            seznam2.add_widget(Label(
                text=jizdenka[1],
                size_hint_y=None,
                height=40
            ))
            seznam2.add_widget(Label(
                text=f'{datetime.strptime(jizdenka[2], "%Y-%m-%d").strftime("%d. %m. %Y")}    {jizdenka[3]}',
                size_hint_y=None,
                height=40
            ))
            seznam2.add_widget(Label(
                text=f'{datetime.strptime(jizdenka[4], "%Y-%m-%d").strftime("%d. %m. %Y")}    {jizdenka[5]}',
                size_hint_y=None,
                height=40
            ))
            seznam2.add_widget(Label(
                text=jizdenka[6],
                size_hint_y=None,
                height=40
            ))

        scroll2 = ScrollView()
        scroll2.add_widget(seznam2)
        root.add_widget(scroll2)

        return root


if __name__ == '__main__':
    JizdenkyApp().run()