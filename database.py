import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "database.db"
SEED_PATH = Path(__file__).parent / "data" / "seed.sql"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with get_connection() as conn:
        with open(SEED_PATH, 'r', encoding='utf-8') as file:
            conn.executescript(file.read())

def pridat_jednorazovou(dopravce, datum, cas_od, odkud, kam, vlak, misto=None, doklad=None):
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO jednorazove
            (dopravce, datum, cas_od, odkud, kam, vlak, misto, doklad)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (dopravce, datum, cas_od, odkud, kam, vlak, misto, doklad)
        )

        ticket_id = cursor.lastrowid

        conn.execute(
            """
            INSERT INTO tickets (type, ticket_id)
            VALUES (?, ?)
            """,
            ("jednorazova", ticket_id)
        )

        return ticket_id

def pridat_casovou(ids, datum_od, cas_od, datum_do, cas_do, zony, doklad=None):
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO casove
            (ids, datum_od, cas_od, datum_do, cas_do, zony, doklad)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (ids, datum_od, cas_od, datum_do, cas_do, zony, doklad)
        )

        ticket_id = cursor.lastrowid

        conn.execute(
            """
            INSERT INTO tickets (type, ticket_id)
            VALUES (?, ?)
            """,
            ("casova", ticket_id)
        )

        return ticket_id

def get_tickets():
    with get_connection() as conn:
        return conn.execute(
            "SELECT id, type, ticket_id FROM tickets"
        ).fetchall()

def get_jednorazove():
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT *
            FROM jednorazove
            ORDER BY datum, cas_od
            """
        ).fetchall()

def get_casove():
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT *
            FROM casove
            ORDER BY datum_od, cas_od
            """
        ).fetchall()

def get_tickets_for_date(datum):
    with get_connection() as conn:
        jednorazove = conn.execute(
            """
            SELECT *
            FROM jednorazove
            WHERE datum = ?
            ORDER BY cas_od
            """,
            (datum,)
        ).fetchall()

        casove = conn.execute(
            """
            SELECT *
            FROM casove
            WHERE datum_od <= ?
            AND datum_do >= ?
            ORDER BY cas_od
            """,
            (datum, datum)
        ).fetchall()

        return jednorazove, casove

def get_jednorazova(id):
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT *
            FROM jednorazove
            WHERE id = ?
            """,
            (id,)
        ).fetchone()

def upravit_jednorazovou(id, dopravce, datum, cas_od, odkud, kam, vlak, misto=None, doklad=None):
    with get_connection() as conn:
        conn.execute(
            """
            UPDATE jednorazove
            SET dopravce = ?, datum = ?, cas_od = ?, odkud = ?, kam = ?,
                vlak = ?, misto = ?, doklad = ?
            WHERE id = ?
            """,
            (dopravce, datum, cas_od, odkud, kam, vlak, misto, doklad, id)
        )

def smazat_jednorazovou(id):
    with get_connection() as conn:
        conn.execute(
            "DELETE FROM tickets WHERE type = ? AND ticket_id = ?",
            ("jednorazova", id)
        )
        conn.execute(
            "DELETE FROM jednorazove WHERE id = ?",
            (id,)
        )

def get_casova(id):
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT *
            FROM casove
            WHERE id = ?
            """,
            (id,)
        ).fetchone()

def upravit_casovou(id, ids, datum_od, cas_od, datum_do, cas_do, zony, doklad=None):
    with get_connection() as conn:
        conn.execute(
            """
            UPDATE casove
            SET ids = ?, datum_od = ?, cas_od = ?, datum_do = ?,
                cas_do = ?, zony = ?, doklad = ?
            WHERE id = ?
            """,
            (ids, datum_od, cas_od, datum_do, cas_do, zony, doklad, id)
        )

def smazat_casovou(id):
    with get_connection() as conn:
        conn.execute(
            "DELETE FROM tickets WHERE type = ? AND ticket_id = ?",
            ("casova", id)
        )
        conn.execute(
            "DELETE FROM casove WHERE id = ?",
            (id,)
        )