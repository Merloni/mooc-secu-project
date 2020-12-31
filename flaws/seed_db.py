import sqlite3
import os

# Creates agents.sqlite
# TMC has issues with binary files, so we will go around by creating it locally from the text dump.

db = """
INSERT INTO auth_user (id, username, first_name,last_name, password, is_superuser, email, is_staff, is_active, date_joined) VALUES(1,'Tuomo', 'Tuomo','Testaaja','SALASANA', 1, 'testi@mail.fi', 1,1, '');
INSERT INTO auth_user (id, username, first_name,last_name, password, is_superuser, email, is_staff, is_active, date_joined) VALUES(2,'BOBI', 'BOBI','NELIÖHOUSU','SALASANA', 1, 'testi@mail.fi', 1,1, '');
INSERT INTO flaws_account VALUES(1,1);
INSERT INTO flaws_account VALUES(2,1);
"""


conn = sqlite3.connect("../db.sqlite3")
conn.cursor().executescript(db)
conn.commit()
