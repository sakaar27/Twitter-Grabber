from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
#consumer key, consumer secret, access token, access secret.
ckey="Og16DDv9ReloNpNx2J1N1O3sk"
csecret="ZrPWHEg8A2MzNQq3VWWVdduTHWpyOMoMe7spRi1s5BEiL4ekTi"
atoken="877258384982003712-9xDXLYN2bD7vAQyHpTBpOtX8RCMPk7p"
asecret="uGgmDWdUW8ItdloUYz67UZ9KOyGirMRMXP2RxsEo9YHCJ"
class listener(StreamListener):

    def on_status(self, data):
        try:
            print(data.text)
            #print(data.user.location)
            #print tweetf
            saveThis=str(time.ctime())+'::'+data.text+'/n'
            saveFile = open('twitDB3.txt','a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return(True)
        except BaseException, e:
            print 'failed on data,',str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())

twitterStream.filter(locations=[77.11,28.47,77.38,28.72]) #INDIA!
