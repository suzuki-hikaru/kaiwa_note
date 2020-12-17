# -*- coding: utf-8 -*- 
import tweepy
import config

# 先ほど取得した各種キーを代入する
CK=config.CK
CS=config.CS
AT=config.AT
AS=config.AS
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

#1ツイートずつループ
for status in api.home_timeline(count=1):
    #見映えのため区切る
    print("---")
    #ユーザ名表示
    print(status.user.name)
    #内容表示
    print(status.text)
