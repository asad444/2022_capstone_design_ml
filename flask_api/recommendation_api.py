"""
recom_api.py
사용자의 일기로부터의 감정, 날씨, 시간을 기반으로 음악, 행동, 음식을 추천하는 API
"""

"""
return "list of json (20 musics)"
[
    {'Title': '밤 편지', 'Artist': '아이유'}, 
    {'Title': '가나다라', 'Artist': 박재범},
    ... 
    ]
"""
def recommendation_with_tags(*args):
    # tags: ['슬픔', '교수', '운동']
    tags = list(args)
    return [{'Title': '밤 편지', 'Artist': '아이유'}, {'Title': '가나다라', 'Artist': '박재범'}]