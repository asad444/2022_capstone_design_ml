from recommender import recommender
from extractor import extractor

# 추천을 위한 API 호출을 담당하는 메인 컨트롤러
class main_controller:
    
    def __init__(self):
        self.extractor = extractor()        # 키워드, 감정 추출 
        self.recommender = recommender()    # 음악, 행동, 음식 추천
        self.diary = None
        
        # extracted from diary
        self.emotion = None
        self.keywords = []
        
        self.musics = []
        self.foods = []
        self.behaviors = []
    
    # load user's diary(content) for recommendation
    def get_diary(self, content):
        self.diary = content
        
    def keyword_extract(self):
        if self.diary:
            self.keywords = self.extractor.extract_keyword_from_diary(self.diary)
        else: print("There is no diary contents!")
        
        if not self.keywords: print("There are no keywords!")    
        
    def sentiment_extract(self):
        if self.diary:
            self.emotion = self.extractor.extract_sentiment_from_diary(self.diary)
        else: print("There is no diary contents!")
        
        if not self.emotion: print("There is no emotion!")
        
    
    def music_recommend(self):
        if self.emotion and self.keywords:
            self.musics = self.recommender.recommend_music_with_tags(self.emotion, self.keywords)
        else: print("There is no emotion or keywords")
        
        if not self.musics: print("There are no recommended musics!")
        
    def food_recommend(self):
        if self.emotion:
            self.foods = self.recommender.recommend_food_with_emotion(self.emotion)
        else: print("There is no emotion!")
        
        if not self.foods: print("There are no recommended foods")

    def behavior_recommend(self):
        if self.emotion:
            self.behaviors = self.recommender.recommend_behavior_with_emotion(self.emotion)
        else: print("There is no emotion!")
        
        if not self.behaviors: print("There are no recommended behaviors!")