import tweepy
# 先ほど取得した各種キーを代入する
CK=config.CK
CS=config.CS
AT=config.AT
AS=config.AS
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        print('------------------------------')
        print(status.text)
        for hashtag in status.entities['hashtags']:
            print(hashtag['text']),
        print("------------------------------")
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True

listener = Listener()
stream = tweepy.Stream(auth, listener)
stream.filter(track=['#NiziU'])
