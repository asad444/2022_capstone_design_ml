"""
CLASS
recommender.py
extractor로 부터 추출한 감정과 키워드를 기반으로 음악, 행동, 음식을 추천하는 class

METHODS

    - recommend_music_with_tags(emotion: str, *args: list) -> list:
        return list of 20 musics
        e.g.,
        [
            {'Title': '밤 편지', 'Artist': '아이유'}, 
            {'Title': '가나다라', 'Artist': 박재범},
            ... 
        ]
        
    - recommend_food_with_emotion(emotion: str) -> list:
        return list of 3 foods
        e.g.,
        [
            {'food1': '엽떡'},
            {'food2': '제육'},
            {'food3': '고추바사삭'}
        ]
        
    - recommend_behavior_with_emotion(emotion: str) -> list:
        return list of 2 behaviors
        e.g.,
        [
            {'behavior1': '산책하기'},
            {'behavior2': '영화보기'}
        ]
    
"""
import random
from db_api import connect_to_db, disconnect_from_db

class recommender:
    def __init__(self):
        self.music_recommender = Music_recommender()
        self.food_recommender = Food_recommender()
        self.behavior_recommender = Behavior_recommender()
    
    # recommend 20 musics from user's emotion and tags
    def recommend_music_with_tags(self, *args):
        tags = [*args]
        self.music_recommender.run(tags)
        return [{'Title': '밤 편지', 'Artist': '아이유'}, {'Title': '가나다라', 'Artist': '박재범'}]

    # recommend 3 foods from user's emotion
    def recommend_food_with_emotion(self, emotion: str):
        # self.food_recommender.run(emotion)
        return [{'food1': '엽떡'}, {'food2': '제육'}, {'food3': '고추바사삭'}]

    # recommend 2 behaviors from user's emotion
    def recommend_behavior_with_emotion(self, emotion: str):
        # return self.behavior_recommender.run(emotion)
        return [{'behavior1': '산책하기'}, {'behavior2': '영화보기'}]
    
class Music_recommender:
    def __init__(self):
        pass
    
    def run(self, keywords: list):
        conn, cur = connect_to_db()
        
        """
        Music Recommendation Logic
        """
        
        disconnect_from_db(conn, cur)
        return None

class Food_recommender:
    def __init__(self):
        pass
    
    def run(self, emotion: str):
        conn, cur = connect_to_db()
        
        """
        Food Recommendation Logic
        """
        
        disconnect_from_db(conn, cur)
        return None

class Behavior_recommender:
    def __init__(self):
        self.emo_dict = {'중립': 0, '걱정': 1, '슬픔': 2, '분노': 3, '행복': 4}
        
    def run(self, emotion: str):
        conn, cur = connect_to_db()
         
        """
        Behavior Recommendation Logic
        """
        cur.execute("SELECT `name`, content FROM BEHAVIOR WHERE label = ?", [self.emo_dict[emotion]])
        result = cur.fetchall()
        if not result:
            return ""
        
        disconnect_from_db(conn,cur)
        return result[random.randint(0, len(result)-1)]

if __name__ == "__main__":
    recom = Behavior_recommender()
    print(recom.run("중립"))