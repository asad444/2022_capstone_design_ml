from recommendation_api import recommendation_with_tags
from mypage_api import mypage
from sentiment_extract_api import extract_sentiment_from_diary
from flask import Flask, request, jsonify

app = Flask(__name__)

# 날씨/시간으로 음악 추천 (일기 쓰기 전에 첫 페이지)
@app.route('/music/weather', methods=["GET"])
def weather_recommendation():
    weather = request.args.get('weather')
    time = request.args.get('time')
    if not weather or not time:
        return 'Bad Request!', 400
    
    # tags for recommendation -> (weather, time)
    music_list = recommendation_with_tags(weather, time)
    
    return jsonify(
        musicList = music_list
    )

# 감정, 키워드로 음악/행동 추천(일기)
@app.route('/music/diary', methods=["GET"])
def diary_recommendation():
    content = request.args.get('content')
    if not content:
        return 'Bad Request!', 400
    
    # extract tags from diary
    emotion, keywords = extract_sentiment_from_diary(content)
    
    # tags for recommendation -> (emotion, [keywords])
    music_list = recommendation_with_tags(emotion, keywords)
    food_list = 
    
    return jsonify(
        musicList = music_list,
        FoodList = food_list,
    )
    
    
@app.route('/mypage')
def checkmypage():
    mypage()

if __name__ == "__main__":
    app.run(debug=True)
