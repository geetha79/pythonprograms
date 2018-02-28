import os 
import time
import tweepy
consumer_key = 'u5OUscNEumo1MFM6ydaYOZxad'
consumer_secret = 'FB4WOShOKw4PueBUumSjOmKO5vHWeRIHNnKoi6Dqjp5f6WaGP4'
access_token = '966157062332932096-FFEVOD5PqBr8JQRPo9VtpfXeE7PJGlR'
access_token_secret = 'Kxf0CSimk54r23jGtPamnRG50XPar3iZH3eykQOaMO29f'

# these are the key and access secret codes for sending the tweet
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
b=1
a=0
while a<=2 :
    img="/home/user/Desktop/img"+str(b)+".jpg"
    cmd="fswebcam -F 3 --fps 20 -r 800x600 "+img
    os.system(cmd)
    print ("pic taken")
    #read image from location
    file = open(img, 'rb')
    data = file.read()
    api.update_with_media(img, status="Nice one")
    print("wait for 5 seconds for selfiiii!!!")
    time.sleep(5)
    a+=1
    b+=1
   # r = api.request('statuses/update_with_media', {'status':'pic from pyhton script'}, {'media[]':data})
    print("success")
