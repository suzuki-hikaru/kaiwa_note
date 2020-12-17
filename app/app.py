from flask import Flask,render_template, request
import tweepy
import random
import config

#Flaskオブジェクトの生成
app = Flask(__name__)

"""""""""""""""""""""""""""
hikaru suzuki
"""""""""""""""""""""""""""
@app.route("/", methods=['GET'])
def get_index():
    return render_template("index.html",)

@app.route("/", methods=['POST'])
def post_index():
    # name = request.form['name']
    return render_template("index.html")

@app.route("/wimage", methods=['POST'])
def wi():
    # name = request.form['name']
    return render_template("index.html",imagename="wordcloud_201217.png")

@app.route("/twReload", methods=['POST'])
def tw():
    # 取得した各種キーを代入
    CK=config.CK
    CS=config.CS
    AT=config.AT
    AS=config.AS

    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    #tweet 範囲指定
    woeid = {
        "日本": 23424856
    }

    items=[]
    random_items=[]

    for area, wid in woeid.items():
        trends = api.trends_place(wid)[0]
        for i, content in enumerate(trends["trends"]):
            rank=i+1
            items.append('トレンド'+str(rank)+'位     '+content['name'])

    for i in range(5):
        random_items.append(items[random.randint(0,49)])


    return render_template("index.html",items=random_items)
