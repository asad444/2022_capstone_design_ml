import sqlite3, json
DB = './db.db'

"""
db_api.py
db에 접근하는 api들
"""

# musicId -> ()
def lookup_music_info(musicId):
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
    except:
        return "DB Connection Error!"," "

    try:
        cur.execute("SELECT title, artist FROM MUSIC WHERE musicId = ?", [musicId])
        result = cur.fetchall()
    except Exception as e:
        print(e)
        return "No song information correspoding to musicId"," "
    
    finally:
        conn.commit()
        conn.close()
    
    return {'title': result[0][0], 'artist': result[0][1]}

if __name__ == "__main__":
    result = lookup_music_info(174749)
    print(result)
    