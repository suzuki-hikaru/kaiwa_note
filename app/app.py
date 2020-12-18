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

@app.route("/cwCreante", methods=['POST'])
def cw():
    # 名詞だけ抽出、単語をカウント
    def counter(texts):
        t = Tokenizer()
        words_count = defaultdict(int)
        words = []
        for text in texts:
            tokens = t.tokenize(text)
            for token in tokens:
                # 品詞から名詞だけ抽出
                pos = token.part_of_speech.split(',')[0]
                if pos in ['名詞']:
                    # 必要ない単語を省く(実際の結果を見てから不必要そうな単語を記載しました)
                    if token.base_form not in ["こと"]:
                        words_count[token.base_form] += 1
                        words.append(token.base_form)
        return words_count, words

    with open('./talk_data.txt', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        texts = []
        for row in reader:
            if(len(row) > 0):
                text = row[0].split('http')
                texts.append(text[0])

    words_count, words = counter(texts)
    text = ' '.join(words)

    # fontは自分の端末にあるものを使用する
    fpath = "./SourceHanSerifK-Light.otf"
    wordcloud = WordCloud(background_color="white",
                        font_path=fpath, width=900, height=500).generate(text)

    wordcloud.to_file("./static/images/wordcloud.png")



