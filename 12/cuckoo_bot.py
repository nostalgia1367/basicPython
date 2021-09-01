import tweepy
import datetime
import threading

# pip install tweepy

def check_time(curr_hour):
    dt = datetime.datetime.now() 
    
    if curr_hour != dt.hour:
        print(dt)
        curr_hour = dt.hour        
        
        consumer_key = "hhdWRkXc9p6qRbzcNGNNYhQio"
        consumer_secret = "4drkYDzcwYk5dWsGaAxCV6Gi95sHet9WTgnrqTLsSdMUOZdjNh"                            
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        
        access_token = "2470701600-B3Sqgl7qhyITQfQitlUeLuSl6wuAm6hsgxG0KHp"
        access_token_secret = "KwrYkaieduvt0gp8gpelUPjPUxi1xkUF5HMmptv1iyXBp"   
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        
        hour = 0
        
        if curr_hour == 0:
            hour = 24
        else:
            hour = curr_hour
            
        tweet = "@브릴리언트님 {0}시 입니다.".format(hour)
        #print('{0}'.format(no_list.pop()))
        #for i in range(0, hour):
        #    tweet += '뻐꾹{0}시 '.format(i+1)
            
        api.update_status(status=tweet)

        print("트윗 작성 완료")
   
    threading.Timer(1, check_time, args=[curr_hour]).start()

if __name__ == '__main__':    
    check_time(-1)