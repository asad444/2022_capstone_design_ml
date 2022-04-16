"""
recommendation_api.py
사용자의 일기로부터 감정, 날씨, 시간을 기반으로 음악, 행동, 음식을 추천하는 API

music_recommendation_with_tags
    return "list of 20 musics"
    e.g.,
    [
        {'Title': '밤 편지', 'Artist': '아이유'}, 
        {'Title': '가나다라', 'Artist': 박재범},
        ... 
    ]

food_recommendation_with_emotion
    return "list of 3 foods"
    e.g.,
    [
        {'food1': '엽떡'},
        {'food2': '제육'},
        {'food3': '고추바사삭'}
    ]
"""

def music_recommendation_with_tags(*args):
    # tags: ['슬픔', '교수', '운동']
    tags = list(args)
    """
    recommendation with tags!
    """
    return [{'Title': '밤 편지', 'Artist': '아이유'}, {'Title': '가나다라', 'Artist': '박재범'}]

def food_recommendation_with_emotion(emotion):
    """
    recommendation with emotion!
    """
    return [{'food1': '엽떡'}, {'food2': '제육'}, {'food3': '고추바사삭'}]
