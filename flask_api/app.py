from recom_api import recom
from mypage_api import mypage
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommendation')
def recommendation():
    recom()

@app.route('/mypage')
def checkmypage():
    mypage()

if __name__ == "__main__":
    app.run(debug=True)
