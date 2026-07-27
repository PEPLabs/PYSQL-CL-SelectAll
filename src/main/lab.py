import os
import sqlite3

from src.main.song import Song

"""
SQL sublanguage: DQL (Data Query Language)

In this lab we are going to learn how to retrieve all the records from a table.

The syntax for retrieving all rows and columns from a database table looks like the following:
SELECT * FROM table_name;

NOTE: the * is a wildcard character to retrieve all the columns from the table.
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()



def problem1():
    """
    Assignment: write the SQL statement in the problem1.sql file to retrieve all the rows and columns from the
    table "song". The db table we will utilize for this problem is the "song" table below

    Song Table Diagram:
    |      title        |        artist         |
    ---------------------------------------------
    |"Let it be"        |Beatles                |
    |"Hotel California" |Eagles                 |
    |"Kashmir"          |Led Zeppelin           |

    NOTE: Do not change anything in this code. You should write your sql statement on a single line in the
    problem1.sql file.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE song(
        title TEXT,
        artist TEXT
    );
    """)
    cur.execute("INSERT INTO song VALUES ('Let it be', 'Beatles');")
    cur.execute("INSERT INTO song VALUES ('Hotel California', 'Eagles');")
    cur.execute("INSERT INTO song VALUES ('Kashmir', 'Led Zeppelin');")
    conn.commit()

    songs = []
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            songs.append(Song(row[0], row[1]))
    except Exception as e:
        print(f"problem1: {e}\n")
    finally:
        conn.close()

    return songs
