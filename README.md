# Jízdenky

## Anotace

Projekt, jehož cílem je vytvoření jednoduché mobilní aplikace, do které si uživatel může přidávat jednotlivé jízdenky napříč systémy a dopravci a udržovat si tak přehled o svých cestách a dlouhodobých jízdenkách.

## Funkce

* Přidání jízdenky
* Upravení/smazání jízdenky
* Vyhledání jízdenek podle data/místa
* Zobrazení jízdního dokladu
* Typy jízdenek:
    * Jednorázové (odkud, kam, čas, datum, místenka)
    * Dlouhodobé (od, do, kde platí)

## Soubory

* attachments - složka s uloženými soubory (jízdní doklady)
* data - složka s databází jízdenek
* database.py - funkce pro kumunikaci s databází
* gui.py - funkce definující uživatelské rozhraní a využívání databázových funkcí
* main.py - samotná aplikace
