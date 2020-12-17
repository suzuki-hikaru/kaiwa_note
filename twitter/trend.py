# -*- coding: utf-8 -*- 
import tweepy
import random

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

for area, wid in woeid.items():
    print("--- {} ---".format(area))
    trends = api.trends_place(wid)[0]
    
    for i, content in enumerate(trends["trends"]):
        print(i+1, content['name'])
        rank=i+1
        items.append('トレンド'+str(rank)+'位     '+content['name'])
    print("----------")

print([random.randint(0, 50) for i in range(5)])
print("----------")

for i in range(5):
    print(items[random.randint(0,49)])

