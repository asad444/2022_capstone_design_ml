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

class recommender:
    def __init__(self):
        pass
    
    # recommend 20 musics from user's emotion and tags
    def recommend_music_with_tags(self, emotion: str, *args: list):
        tags = list(args)
        return [{'Title': '밤 편지', 'Artist': '아이유'}, {'Title': '가나다라', 'Artist': '박재범'}]

    # recommend 3 foods from user's emotion
    def recommend_food_with_emotion(self, emotion: str):
        return [{'food1': '엽떡'}, {'food2': '제육'}, {'food3': '고추바사삭'}]

    # recommend 2 behaviors from user's emotion
    def recommend_behavior_with_emotion(self, emotion: str):
        return [{'behavior1': '산책하기'}, {'behavior2': '영화보기'}]