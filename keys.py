import tweepy


class KeysTweet:
    def __init__(self):
        # KEYS CONSTANS
        CKEY = "YOUR TWITTER CLIENTE KEY"
        CSECRET = "YOUR TWITTER SECRET KEY CLIENT"

        AKEY = "YOUR ACCESS TOKEN"
        ASECRET = "YOUR ACCESS SECRET TOKEN"

        self.auth = tweepy.OAuthHandler(CKEY, CSECRET)
        self.auth.set_access_token(AKEY, ASECRET)

        self.api = tweepy.API(self.auth)

    # UPDATE JUST TEXT
    def enviar(self, texto):
        self.api.update_status(status=texto)

    # UPDATE IMAGE AND TEXT
    def post_text_img(self, img, texto):
        self.api.update_with_media(img, texto)
