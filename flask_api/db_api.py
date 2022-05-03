import sqlite3
DB = './db.db'

"""
db_api.py
db에 접근하는 api들
"""

def connect_to_db(DB = './db.db'):
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
    except:
        conn, cur = None, None
        pass
    return conn, cur

def disconnect_from_db(conn, cur):
    if not conn or not cur:
        return
    conn.commit()
    conn.close()
        
# musicId -> {'title': title, 'artist': artist}
def lookup_music_info(musicId):
    conn, cur = connect_to_db()
    
    cur.execute("SELECT title, artist FROM MUSIC WHERE musicId = ?", [musicId])
    result = cur.fetchall()
    if not result:
        return ""
    
    disconnect_from_db(conn, cur)
    return {'title': result[0][0], 'artist': result[0][1]}

if __name__ == "__main__":
    result = lookup_music_info(174749)
    print(result)
    