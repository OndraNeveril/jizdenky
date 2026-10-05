CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    ticket_id INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS jednorazove (
    id	INTEGER PRIMARY KEY,
    dopravce TEXT NOT NULL,
    datum TEXT NOT NULL,
    cas_od TEXT NOT NULL,
    odkud TEXT NOT NULL,
    kam TEXT NOT NULL,
    vlak TEXT NOT NULL,
    misto TEXT,
    doklad TEXT
);

CREATE TABLE IF NOT EXISTS casove (
    id	INTEGER PRIMARY KEY,
    ids	TEXT NOT NULL,
    datum_od TEXT NOT NULL,
    cas_od TEXT NOT NULL,
    datum_do TEXT NOT NULL,
    cas_do TEXT NOT NULL,
    zony TEXT NOT NULL,
    doklad TEXT
);