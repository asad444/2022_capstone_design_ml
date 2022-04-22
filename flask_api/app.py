from db_api import lookup_music_info
from controller import main_controller
from flask import Flask, request, jsonify

app = Flask(__name__)

# 추천을 위한 API 호출을 담당하는 메인 컨트롤러
controller = main_controller()

# 날씨/시간으로 음악 추천 (일기 쓰기 전에 첫 페이지)
@app.route('/music/weather', methods=["GET"])
def weather_recommendation():
    weather = request.args.get('weather')
    time = request.args.get('time')
    if not weather or not time:
        return 'Bad Request!', 400
    
    music_list = controller.music_recommend(weather = True)
    # tags for recommendation -> (weather, time)
    music_list = music_recommendation_with_tags(weather, time)
    
    return jsonify(
        musicList = music_list
    )

# 감정, 키워드로 음악/행동 추천(일기)
@app.route('/music/diary', methods=["GET"])
def diary_recommendation():
    content = request.args.get('content')
    if not content:
        return 'Bad Request!', 400
    
    # extract emotion and tags from diary
    emotion = extract_sentiment_from_diary(content)
    keywords = extract_keyword_from_diary(content)
    
    # tags for recommendation -> (emotion, [keywords])
    music_list = music_recommendation_with_tags(emotion, keywords)
    behavior_list = behavior_recommendation_with_emotion(emotion)
    food_list = food_recommendation_with_emotion(emotion)
    
    return jsonify(
        musicList = music_list,
        behaviorList = behavior_list,
        FoodList = food_list
    )

# 마이페이지에서 music의 정보를 넘기는 API
@app.route('/mypage/music', methods=["GET"])
def request_music_info():
    musicId = request.args.get('musicId')
    musicInfo = lookup_music_info(musicId)
    
    return jsonify(
        title = musicInfo['title'],
        artist = musicInfo['artist']
    )

if __name__ == "__main__":
    app.run(debug=True)
