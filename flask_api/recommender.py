"""
CLASS
recommender.py
extractor로 부터 추출한 감정과 키워드를 기반으로 음악, 행동, 음식을 추천하는 class

METHODS

    - music_recommendation_with_tags(*args: list) -> list:
        return list of 20 musics
        e.g.,
        [
            {'Title': '밤 편지', 'Artist': '아이유'}, 
            {'Title': '가나다라', 'Artist': 박재범},
            ... 
        ]
        
    - food_recommendation_with_emotion(emotion: str) -> list:
        return list of 3 foods
        e.g.,
        [
            {'food1': '엽떡'},
            {'food2': '제육'},
            {'food3': '고추바사삭'}
        ]
        
    - behavior_recommendation_with_emotion(emotion: str) -> list:
        return list of 2 behaviors
        e.g.,
        [
            {'behavior1': '산책하기'},
            {'behavior2': '영화보기'}
        ]
    
"""

def music_recommendation_with_tags(*args: list):
    # tags: ['슬픔', '교수', '운동']
    tags = list(args)
    """
    recommendation with tags!
    """
    return [{'Title': '밤 편지', 'Artist': '아이유'}, {'Title': '가나다라', 'Artist': '박재범'}]

def food_recommendation_with_emotion(emotion: str):
    """
    recommendation with emotion!
    """
    return [{'food1': '엽떡'}, {'food2': '제육'}, {'food3': '고추바사삭'}]

def behavior_recommendation_with_emotion(emotion: str):
    """
    recommendation with emotion!
    """
    return [{'behavior1': '산책하기'}, {'behavior2': '영화보기'}]