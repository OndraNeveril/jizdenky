# Jízdenky

## Anotace

Projekt, jehož cílem je vytvoření jednoduché mobilní aplikace, do které si uživatel může přidávat jednotlivé jízdenky napříč systémy a dopravci a udržovat si tak přehled o svých cestách a dlouhodobých jízdenkách.

Další v budoucnu plánovanou funkcí je minimalistický vyhledávač spojení pracující offline na bázi uživatelem nahraných jízdních řádů vybraných linek.

## Funkce

* Přidání jízdenky
* Upravení/smazání jízdenky
* (Vyhledání jízdenek podle data/místa)
* Zobrazení jízdního dokladu
* Typy jízdenek:
    * Jednorázové (odkud, kam, čas, datum, místenka)
    * Dlouhodobé (od, do, kde platí)

## Soubory

* attachments - složka s uloženými soubory (jízdní doklady)
* data - složka s databází jízdenek a jízdních řádů
* database.py - funkce pro kumunikaci s databází uložených jízdenek
* gui\_jizdenky.py - funkce definující chování a vzhled části aplikace pro práci s jízdenkami
* (gui\_vyhledavac.py - funkce definující vzhled vyhledávače spojení)
* main.py - samotná aplikace - má dvě oddělená rozhraní pro ukládání jízdenek a vyhledávání spojů
