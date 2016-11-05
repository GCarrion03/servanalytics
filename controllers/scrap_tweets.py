'''
Created on Oct 2, 2016

@author: Jorge Pantoja
'''

import tweepy
import json
import time
import csv  # @UnusedImport

##Location details
#https://www.freemaptools.com/radius-around-point.htm
    
#Ecuador

location1_lat=-1.831239
location1_long=-78.183406
location1_accuracy_km=422
location1_accuracy_miles=263

#Galapagos

location2_lat=-0.953769
location2_long=-90.965602
location2_accuracy_km=367
location2_accuracy_miles=228

#track list
#keyword_list = ['leninmoreno', 'jorgeglas'] #track list
keyword_list = ['leninmoreno','jorgeglas']

#users_list
list_users = ['LeninMorenoPAIS ','LeninMoreno', 'JorgeGlas']   #Some ids

#system time
start_time = time.asctime( time.localtime(time.time()) ) #grabs the system time

#Twitter details

consumer_key = 'vnHVAguDeUlKnFyFNIMEFEZlc'
consumer_secret = 'zD1jlTTR0plz5KF7qrUYsDE7YET3pVCHcRi2e1OQv2wrICxDAw'
access_token = '353206269-KgBxqV0ueGVHVZITeMR5rcvVVKCt7zlJIMKiUAdA'
access_token_secret = 'YtKs60mgNVxBD53Iv9Hdv6berknhaaUblkNSEHQnR4gDj'

#local tweets path
tweets_data_path = 'TwitterAPI.txt'

#create file headers
saveFile = open(tweets_data_path, 'a', encoding='utf-8', errors='ignore')
saveFile.write('id; realtime; created_at; retweet_count; favorite_count; user_screen_name; user_geo_enabled; user_url; user_followers_count; user_friends_count; user_text; user_location; geo_coordinates; place_name; place_full_name; place_country_code; place_country; id_retweeted_status; retweeted_status_retweet_count; retweeted_status_favorite_count; screen_name_retweeted_status; text_retweeted_status; id_quoted_status; quoted_status_retweet_count; quoted_status_favorite_count; screen_name_quoted_status; text_quoted_status')
saveFile.write('\n')
saveFile.close()

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    
#     def __init__(self): #def __init__(self, start_time, time_limit=60):
#         self.saveFile = open('abcd.json', 'a')
#  
#         self.time = start_time
#         self.limit = time_limit
#         self.tweet_data = []
        
    def on_data(self, data):
#         print ('Ok, this is actually running')

        print (data)

        decoded = json.loads(data)
        msg = (
            decoded['id'],
            start_time,
            decoded['created_at'],
            decoded['retweet_count'],
            decoded['favorite_count'],
            decoded['user']['screen_name'].replace(",", "-").replace(";", "-"),
            decoded['user']['geo_enabled'],
            decoded['user']['url'],
            decoded['user']['followers_count'],
            decoded['user']['friends_count'],
            decoded['text'].replace(",", "-").replace(";", "-").encode('ascii', 'ignore'))
        
        if decoded['user']['location'] is not None:
            msg += decoded['user']['location'].replace(",", "-").replace(";", "-"),
        else:
            msg += 'location is none',
        
        if decoded['geo'] is not None:
            msg += decoded['geo']['coordinates'],
        else:
            msg += 'geo coordinates is none',
        
        if decoded['place'] is not None:
            msg += decoded['place']['name'].replace(",", "-").replace(";", "-").encode('ascii', 'ignore'),
        else:
            msg += 'place name is none',
            
        if decoded['place'] is not None:
            msg += decoded['place']['full_name'].replace(",", "-").replace(";", "-").encode('ascii', 'ignore'),
        else:
            msg += 'place full_name is none',
           
        if decoded['place'] is not None:
            msg += decoded['place']['country_code'].replace(",", "-").replace(";", "-").encode('ascii', 'ignore'),
        else:
            msg += 'place country_code is none',
           
        if decoded['place'] is not None:
            msg += decoded['place']['country'].replace(",", "-").replace(";", "-").encode('ascii', 'ignore'),
        else:
            msg += 'place country is none',
        
        if 'retweeted_status' in decoded:   
            if decoded['retweeted_status'] is not None:
                msg += decoded['retweeted_status']['id'],
                msg += decoded['retweeted_status']['retweet_count'],
                msg += decoded['retweeted_status']['favorite_count'],
                msg += decoded['retweeted_status']['user']['screen_name'].replace(",", "-").replace(";", "-"),
                msg += decoded['retweeted_status']['text'].replace(",", "-").replace(";", "-").encode('ascii', 'ignore'),
            else:
                msg += 'id_retweeted_status is none',
                msg += 'screen_name_retweeted_status is none',
                msg += 'text_retweeted_status is none',
        
        if 'quoted_status' in decoded:       
            if decoded['quoted_status'] is not None:
                msg += decoded['quoted_status']['id'],
                msg += decoded['quoted_status']['retweet_count'],
                msg += decoded['quoted_status']['favorite_count'],
                msg += decoded['quoted_status']['user']['screen_name'].replace(",", "-").replace(";", "-"),
                msg += decoded['quoted_status']['text'].replace(",", "-").replace(";", "-").encode('ascii', 'ignore'),
            else:
                msg += 'id_quoted_status is none',
                msg += 'screen_name_quoted_status is none',
                msg += 'text_quoted_status is none',
        
        saveFile = open(tweets_data_path, 'a', encoding='utf-8', errors='ignore')
        msgtemp = (';'.join(map(str, msg)));
        saveFile.write(msgtemp)
        saveFile.write('\n')
        saveFile.close()
        
#         while (time.time() - self.time) < self.limit:
#             try:
#                 self.tweet_data.append(data)
#                 return True
#             
#             except BaseException, e:
#                 print 'failed ondata,', str(e)
#                 time.sleep(5)
#                 pass

        return True
    
    def on_status(self, status):
        print ('Ran on_status')
        print(status.text)
        
        #filter retweets
#         if status.retweeted_status:
#             return
#         print(status.text)

    def on_error(self, status):
        print ('Error: ' + repr(status))
        if status == 420:
            #returning False in on_data disconnects the stream
            return False
        
    def on_timeout(self, status):
        print ('Timeout: ' + repr(status))
        return True # Don't kill the stream
#End class

if __name__ == '__main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #print ("Showing all new tweets for: " + str(keyword_list))
    
    stream = tweepy.Stream(auth, listener) #tweepy.Stream(auth, listener(start_time, time_limit=20))
    #[SWlongitude, SWLatitude, NElongitude, NELatitude]
    
    #http://boundingbox.klokantech.com/
    #CSV RAW
    GEOBOX_ECUADOR = [-93.0322265793,-5.572249701,-74.4433593918,2.8552628848] #Incluye Galapagos
    #languages=['es']
    
#     stream.filter(track=keyword_list, follow=list_users, async=True)

    stream.filter(track=keyword_list, async=True)
    