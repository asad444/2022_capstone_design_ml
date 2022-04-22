"""
CLASS
extractor.py
사용자의 일기로부터 감정, 키워드를 추출하는 class

METHODS
    
    - extract_sentiment_from_diary(content: str) -> str:
        return emotion of user
        e.g.,
        {'emotion': '슬픔'}
    
    - extract_keyword_from_diary(content: str) -> list:
        return list of keywords
        e.g.,
        [
            {'keyword1': '강남'},
            {'keyword2': '토끼정'},
            {'keyword3': '쉑쉑버거'}
        ]
"""


class extractor:
    def __init__(self):
        self.model = None   # KoBERT model
        pass
    
    # extract emotion from content(diary)
    def extract_sentiment_from_diary(content):
        emotion = ""
        return emotion 
    
    # extract keywords from content(diary)
    def extract_keyword_from_diary(content):
        keywords = []
        return keywords
