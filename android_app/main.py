from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup

from datetime import datetime

import database


BARVA_TEXTU = (0.15, 0.2, 0.25, 1)
BARVA_TLACITKA = (0.25, 0.35, 0.45, 1)


class JizdenkyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        scroll = ScrollView()

        obsah = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            size_hint_y=None
        )
        obsah.bind(minimum_height=obsah.setter("height"))

        obsah.add_widget(
            Label(
                text="Přidat jízdenku:",
                font_size=sp(22),
                bold=True,
                color=BARVA_TEXTU,
                size_hint_y=None,
                height=dp(50)
            )
        )

        tlacitko_jednorazova = Button(

            text="Přidat jednorázovou jízdenku",
            font_size=sp(16),
            size_hint_y=None,
            height=dp(50),
            background_normal="",
            background_color=BARVA_TLACITKA
        )
        tlacitko_jednorazova.bind(
            on_release=lambda instance: self.otevrit_formular("jednorazova")
        )
        obsah.add_widget(tlacitko_jednorazova)

        tlacitko_casova = Button(
            text="Přidat časovou jízdenku",
            font_size=sp(16),
            size_hint_y=None,
            height=dp(50),
            background_normal="",
            background_color=BARVA_TLACITKA
        )
        tlacitko_casova.bind(
            on_release=lambda instance: self.otevrit_formular("casova")
        )
        obsah.add_widget(tlacitko_casova)

        obsah.add_widget(
            Label(
                text="Jízdenky",
                font_size=sp(22),
                bold=True,
                color=BARVA_TEXTU,
                size_hint_y=None,
                height=dp(60)
            )
        )

        self.seznam_jednorazovych = BoxLayout(
            orientation="vertical",
            spacing=dp(2),
            size_hint_y=None
        )
        self.seznam_jednorazovych.bind(
            minimum_height=self.seznam_jednorazovych.setter("height")
        )
        obsah.add_widget(self.seznam_jednorazovych)

        obsah.add_widget(
            Label(
                text="Časové jízdenky",
                font_size=sp(22),
                bold=True,
                color=BARVA_TEXTU,
                size_hint_y=None,
                height=dp(60)
            )
        )

        self.seznam_casovych = BoxLayout(
            orientation="vertical",
            spacing=dp(2),
            size_hint_y=None
        )
        self.seznam_casovych.bind(
            minimum_height=self.seznam_casovych.setter("height")
        )
        obsah.add_widget(self.seznam_casovych)

        scroll.add_widget(obsah)
        layout.add_widget(scroll)

        self.add_widget(layout)

    def on_enter(self):
        self.nacist_jizdenky()

    def nacist_jizdenky(self):
        self.seznam_jednorazovych.clear_widgets()
        self.seznam_casovych.clear_widgets()

        hlavicka = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(35)
        )

        for text in ["Dopravce", "Datum", "Cíl", "Místo"]:
            hlavicka.add_widget(
                Label(
                    text=text,
                    font_size=sp(12),
                    bold=True,
                    color=BARVA_TEXTU
                )
            )

        self.seznam_jednorazovych.add_widget(hlavicka)

        for jizdenka in database.get_jednorazove():
            datum = datetime.strptime(
                jizdenka[2], "%Y-%m-%d"
            ).strftime("%d. %m. %Y")

            tlacitko = Button(
                text=(
                    f"{jizdenka[1]} | {datum} {jizdenka[3]}\n"
                    f"{jizdenka[4]} → {jizdenka[5]} | "
                    f"Vlak {jizdenka[6]} | Místo {jizdenka[7] or '—'}"
                ),
                font_size=sp(12),
                halign="center",
                valign="middle",
                size_hint_y=None,
                height=dp(65),
                background_normal="",
                background_color=(0.85, 0.88, 0.91, 1),
                color=BARVA_TEXTU
            )
            tlacitko.bind(
                size=lambda instance, size: setattr(
                    instance, "text_size", (size[0] - dp(10), None)
                )
            )
            tlacitko.bind(
                on_release=lambda instance, ticket_id=jizdenka[0]:
                self.zobrazit_detail("jednorazova", ticket_id)
            )
            self.seznam_jednorazovych.add_widget(tlacitko)

        hlavicka = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(35)
        )

        for text in ["IDS", "Začátek", "Konec", "Zóny"]:
            hlavicka.add_widget(
                Label(
                    text=text,
                    font_size=sp(12),
                    bold=True,
                    color=BARVA_TEXTU
                )
            )

        self.seznam_casovych.add_widget(hlavicka)

        for jizdenka in database.get_casove():
            datum_od = datetime.strptime(
                jizdenka[2], "%Y-%m-%d"
            ).strftime("%d. %m. %Y")

            datum_do = datetime.strptime(
                jizdenka[4], "%Y-%m-%d"
            ).strftime("%d. %m. %Y")

            tlacitko = Button(
                text=(
                    f"{jizdenka[1]} | {datum_od} {jizdenka[3]}\n"
                    f"Do {datum_do} {jizdenka[5]} | Zóny {jizdenka[6]}"
                ),
                font_size=sp(12),
                halign="center",
                valign="middle",
                size_hint_y=None,
                height=dp(60),
                background_normal="",
                background_color=(0.85, 0.88, 0.91, 1),
                color=BARVA_TEXTU
            )
            tlacitko.bind(
                size=lambda instance, size: setattr(
                    instance, "text_size", (size[0] - dp(10), None)
                )
            )
            tlacitko.bind(
                on_release=lambda instance, ticket_id=jizdenka[0]:
                self.zobrazit_detail("casova", ticket_id)
            )
            self.seznam_casovych.add_widget(tlacitko)

    def pridat_pole(self, obsah, popisek, vychozi="", napoveda=""):
        obsah.add_widget(
            Label(
                text=popisek,
                font_size=sp(14),
                color=BARVA_TEXTU,
                size_hint_y=None,
                height=dp(28),
                halign="left",
                valign="middle"
            )
        )

        pole = TextInput(
            text=str(vychozi),
            hint_text=napoveda,
            multiline=False,
            font_size=sp(16),
            size_hint_y=None,
            height=dp(45),
            padding=(dp(10), dp(10))
        )
        obsah.add_widget(pole)
        return pole

    def otevrit_formular(self, typ, ticket_id=None):
        if typ == "jednorazova":
            jizdenka = (
                database.get_jednorazova(ticket_id)
                if ticket_id is not None else None
            )
        else:
            jizdenka = (
                database.get_casova(ticket_id)
                if ticket_id is not None else None
            )

        obsah = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            padding=dp(15)
        )

        scroll = ScrollView()

        formular = BoxLayout(
            orientation="vertical",
            spacing=dp(5),
            size_hint_y=None
        )
        formular.bind(minimum_height=formular.setter("height"))

        nazev = (
            "Upravit jednorázovou jízdenku"
            if typ == "jednorazova" and jizdenka is not None
            else "Přidat jednorázovou jízdenku"
            if typ == "jednorazova"
            else "Upravit časovou jízdenku"
            if jizdenka is not None
            else "Přidat časovou jízdenku"
        )

        formular.add_widget(
            Label(
                text=nazev,
                font_size=sp(20),
                bold=True,
                color=BARVA_TEXTU,
                size_hint_y=None,
                height=dp(50)
            )
        )

        pole = {}

        if typ == "jednorazova":
            formular.add_widget(
                Label(
                    text="Dopravce",
                    font_size=sp(14),
                    color=BARVA_TEXTU,
                    size_hint_y=None,
                    height=dp(28),
                    halign="left"
                )
            )

            dopravce = Spinner(
                text=jizdenka[1] if jizdenka else "ČD",
                values=("ČD", "Regiojet", "Leoexpres", "Arriva", "Jiný"),
                size_hint_y=None,
                height=dp(45),
                font_size=sp(16)
            )
            formular.add_widget(dopravce)
            pole["dopravce"] = dopravce

            pole["datum"] = self.pridat_pole(
                formular,
                "Datum",
                jizdenka[2] if jizdenka else datetime.today().strftime("%Y-%m-%d"),
                "RRRR-MM-DD"
            )
            pole["cas_od"] = self.pridat_pole(
                formular,
                "Čas odjezdu",
                jizdenka[3] if jizdenka else "",
                "HH:MM"
            )
            pole["odkud"] = self.pridat_pole(
                formular,
                "Odkud",
                jizdenka[4] if jizdenka else ""
            )
            pole["kam"] = self.pridat_pole(
                formular,
                "Kam",
                jizdenka[5] if jizdenka else ""
            )
            pole["vlak"] = self.pridat_pole(
                formular,
                "Vlak",
                jizdenka[6] if jizdenka else ""
            )
            pole["misto"] = self.pridat_pole(
                formular,
                "Místo (nepovinné)",
                jizdenka[7] or "" if jizdenka else ""
            )

        else:
            formular.add_widget(
                Label(
                    text="IDS",
                    font_size=sp(14),
                    color=BARVA_TEXTU,
                    size_hint_y=None,
                    height=dp(28),
                    halign="left"
                )
            )

            ids = Spinner(
                text=jizdenka[1] if jizdenka else "PID",
                values=("PID", "jiný"),
                size_hint_y=None,
                height=dp(45),
                font_size=sp(16)
            )
            formular.add_widget(ids)
            pole["ids"] = ids

            pole["datum_od"] = self.pridat_pole(
                formular,
                "Datum od",
                jizdenka[2] if jizdenka else datetime.today().strftime("%Y-%m-%d"),
                "RRRR-MM-DD"
            )
            pole["cas_od"] = self.pridat_pole(
                formular,
                "Čas od",
                jizdenka[3] if jizdenka else "",
                "HH:MM"
            )
            pole["datum_do"] = self.pridat_pole(
                formular,
                "Datum do",
                jizdenka[4] if jizdenka else datetime.today().strftime("%Y-%m-%d"),
                "RRRR-MM-DD"
            )
            pole["cas_do"] = self.pridat_pole(
                formular,
                "Čas do",
                jizdenka[5] if jizdenka else "",
                "HH:MM"
            )
            pole["zony"] = self.pridat_pole(
                formular,
                "Zóny",
                jizdenka[6] or "" if jizdenka else ""
            )

        scroll.add_widget(formular)
        obsah.add_widget(scroll)

        chyba = Label(
            text="",
            color=(0.8, 0.1, 0.1, 1),
            font_size=sp(13),
            size_hint_y=None,
            height=dp(30)
        )
        obsah.add_widget(chyba)

        tlacitka = BoxLayout(
            orientation="horizontal",
            spacing=dp(10),
            size_hint_y=None,
            height=dp(50)
        )

        popup = Popup(
            title="Jízdenky",
            content=obsah,
            size_hint=(0.95, 0.9),
            auto_dismiss=False
        )

        def ulozit(instance):
            try:
                if typ == "jednorazova":
                    hodnoty = {
                        "dopravce": pole["dopravce"].text,
                        "datum": pole["datum"].text.strip(),
                        "cas_od": pole["cas_od"].text.strip(),
                        "odkud": pole["odkud"].text.strip(),
                        "kam": pole["kam"].text.strip(),
                        "vlak": pole["vlak"].text.strip(),
                        "misto": pole["misto"].text.strip() or None
                    }

                    if not all(hodnoty[k] for k in (
                        "dopravce", "datum", "cas_od",
                        "odkud", "kam", "vlak"
                    )):
                        raise ValueError("Vyplň všechna povinná pole.")

                    datetime.strptime(hodnoty["datum"], "%Y-%m-%d")
                    datetime.strptime(hodnoty["cas_od"], "%H:%M")

                    if ticket_id is None:
                        database.pridat_jednorazovou(
                            hodnoty["dopravce"],
                            hodnoty["datum"],
                            hodnoty["cas_od"],
                            hodnoty["odkud"],
                            hodnoty["kam"],
                            hodnoty["vlak"],
                            hodnoty["misto"],
                            None
                        )
                    else:
                        puvodni = database.get_jednorazova(ticket_id)
                        database.upravit_jednorazovou(
                            ticket_id,
                            hodnoty["dopravce"],
                            hodnoty["datum"],
                            hodnoty["cas_od"],
                            hodnoty["odkud"],
                            hodnoty["kam"],
                            hodnoty["vlak"],
                            hodnoty["misto"],
                            puvodni[8]
                        )

                else:
                    hodnoty = {
                        "ids": pole["ids"].text,
                        "datum_od": pole["datum_od"].text.strip(),
                        "cas_od": pole["cas_od"].text.strip(),
                        "datum_do": pole["datum_do"].text.strip(),
                        "cas_do": pole["cas_do"].text.strip(),
                        "zony": pole["zony"].text.strip()
                    }

                    if not all(hodnoty.values()):
                        raise ValueError("Vyplň všechna pole.")

                    datetime.strptime(hodnoty["datum_od"], "%Y-%m-%d")
                    datetime.strptime(hodnoty["datum_do"], "%Y-%m-%d")
                    datetime.strptime(hodnoty["cas_od"], "%H:%M")
                    datetime.strptime(hodnoty["cas_do"], "%H:%M")

                    if ticket_id is None:
                        database.pridat_casovou(
                            hodnoty["ids"],
                            hodnoty["datum_od"],
                            hodnoty["cas_od"],
                            hodnoty["datum_do"],
                            hodnoty["cas_do"],
                            hodnoty["zony"],
                            None
                        )
                    else:
                        puvodni = database.get_casova(ticket_id)
                        database.upravit_casovou(
                            ticket_id,
                            hodnoty["ids"],
                            hodnoty["datum_od"],
                            hodnoty["cas_od"],
                            hodnoty["datum_do"],
                            hodnoty["cas_do"],
                            hodnoty["zony"],
                            puvodni[7]
                        )

            except ValueError as chyba_text:
                chyba.text = (
                    str(chyba_text)
                    if str(chyba_text).startswith("Vyplň")
                    else "Zkontroluj formát data (RRRR-MM-DD) a času (HH:MM)."
                )
                return

            self.nacist_jizdenky()
            popup.dismiss()

        tlacitko_zrusit = Button(
            text="Zrušit",
            background_normal="",
            background_color=(0.45, 0.45, 0.45, 1)
        )
        tlacitko_zrusit.bind(on_release=lambda instance: popup.dismiss())

        tlacitko_ulozit = Button(
            text="Uložit změny" if ticket_id is not None else "Uložit",
            background_normal="",
            background_color=BARVA_TLACITKA
        )
        tlacitko_ulozit.bind(on_release=ulozit)

        tlacitka.add_widget(tlacitko_zrusit)
        tlacitka.add_widget(tlacitko_ulozit)
        obsah.add_widget(tlacitka)

        popup.open()

    def zobrazit_detail(self, typ, ticket_id):
        if typ == "jednorazova":
            jizdenka = database.get_jednorazova(ticket_id)
            udaje = [
                ("Dopravce", jizdenka[1]),
                ("Datum", jizdenka[2]),
                ("Čas odjezdu", jizdenka[3]),
                ("Odkud", jizdenka[4]),
                ("Kam", jizdenka[5]),
                ("Vlak", jizdenka[6]),
                ("Místo", jizdenka[7] or "—"),
                ("Doklad", "Přiložen" if jizdenka[8] else "Žádný")
            ]
        else:
            jizdenka = database.get_casova(ticket_id)
            udaje = [
                ("IDS", jizdenka[1]),
                ("Datum od", jizdenka[2]),
                ("Čas od", jizdenka[3]),
                ("Datum do", jizdenka[4]),
                ("Čas do", jizdenka[5]),
                ("Zóny", jizdenka[6]),
                ("Doklad", "Přiložen" if jizdenka[7] else "Žádný")
            ]

        obsah = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        scroll = ScrollView()
        udaje_layout = BoxLayout(
            orientation="vertical",
            spacing=dp(12),
            size_hint_y=None
        )
        udaje_layout.bind(minimum_height=udaje_layout.setter("height"))

        udaje_layout.add_widget(
            Label(
                text=(
                    "Detail jednorázové jízdenky"
                    if typ == "jednorazova"
                    else "Detail časové jízdenky"
                ),
                font_size=sp(20),
                bold=True,
                color=BARVA_TEXTU,
                size_hint_y=None,
                height=dp(50)
            )
        )

        for popisek, hodnota in udaje:
            udaje_layout.add_widget(
                Label(
                    text=f"{popisek}: {hodnota}",
                    font_size=sp(16),
                    color=BARVA_TEXTU,
                    size_hint_y=None,
                    height=dp(35),
                    halign="left",
                    valign="middle"
                )
            )

        scroll.add_widget(udaje_layout)
        obsah.add_widget(scroll)

        tlacitka = BoxLayout(
            orientation="horizontal",
            spacing=dp(10),
            size_hint_y=None,
            height=dp(50)
        )

        popup = Popup(
            title="Jízdenky",
            content=obsah,
            size_hint=(0.95, 0.8)
        )

        zpet = Button(
            text="Zpět",
            background_normal="",
            background_color=(0.45, 0.45, 0.45, 1)
        )
        zpet.bind(on_release=lambda instance: popup.dismiss())

        upravit = Button(
            text="Upravit",
            background_normal="",
            background_color=BARVA_TLACITKA
        )

        def otevrit_upravu(instance):
            popup.dismiss()
            self.otevrit_formular(typ, ticket_id)

        upravit.bind(on_release=otevrit_upravu)

        tlacitka.add_widget(zpet)
        tlacitka.add_widget(upravit)
        obsah.add_widget(tlacitka)

        popup.open()


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
