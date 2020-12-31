import sqlite3
import os


db = """
INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$180000$HflwDiluSl4P$grBCR4npO2jzf9vPHFvZfN9cDyc8ASCN/WOHDn0i3Ag=','2020-07-24 18:21:52.048307',1,'admin','','admin@admin.gov',1,1,'2020-07-24 18:21:30.963004','');
INSERT INTO auth_user VALUES(2,'pbkdf2_sha256$180000$Zi0ouavqZHiP$5tskdMLhbkrPUhRsUeXr4xdUgt6ty1/8HLIvvyiTPUI=','2020-07-24 18:49:41.802576',0,'alice','','',0,1,'2020-07-24 18:22:06.886227','');
INSERT INTO auth_user VALUES(3,'pbkdf2_sha256$180000$BwMk1wzXzBju$vZtYfG5+frziABQ2My/F5KKjwKkBgOUxAC8JOQMm7SE=','2020-07-24 18:49:51.614764',0,'bob','','',0,1,'2020-07-24 18:22:18.885086','');
INSERT INTO flaws_account VALUES(1,1);
INSERT INTO flaws_account VALUES(2,1);
INSERT INTO flaws_account VALUES(3,2);
INSERT INTO flaws_account VALUES(4,2);
INSERT INTO flaws_account VALUES(5,3);
INSERT INTO flaws_account VALUES(6,3);
"""


conn = sqlite3.connect("../db.sqlite3")
conn.cursor().executescript(db)
conn.commit()
