import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler
import os
from discord_webhook import DiscordWebhook


def tweet_id(tw_id):
    client = tweepy.Client(os.environ['TWITTER_TOKEN'])
    query = 'from:' + tw_id

    tweets = client.search_recent_tweets(query=query,
                                        tweet_fields = ["created_at", "text", "source"],
                                        user_fields = ["name", "username", "location", "verified", "description",'url'],
                                        max_results = 10,
                                        expansions='author_id'
                                        )
    first_tweet = tweets.data[0]
    # print(first_tweet)
    aaa = dict(first_tweet)
    text = str(aaa['id'])
    return text



def check(user, text):
    user = str(user)
    text = str(text)
    file_name = user +'.txt'
    if os.path.isfile(file_name):
        with open(file_name, 'r')as g:
            latest_id = g.read()
        if latest_id != text:
            with open('latest.txt', 'w')as f:
                f.write(text)
            link = 'https://twitter.com/' + user + '/status/' + text
            print('新推文!')
            return link
        else:
            print('數據相同')
            a = '數據相同'
            return a

    else:
        with open(file_name, 'w')as f:
            f.write(text)
        link = 'https://twitter.com/' + user + '/status/' + text
        print('新id和新推文!')
        return link
         
def send(url,username,link):
    url = str(url)
    msg = str(username) + '推文了!' + str(link)
    webhook = DiscordWebhook(url=url, content=msg)
    response = webhook.execute()




        


       
       
def basic(watcher, webhook_url):
        id = tweet_id(watcher)
        link = check(watcher, id)
        if link != '數據相同':
            send(webhook_url, watcher,link)


def liyuu():
    url = 'https://discord.com/api/webhooks/965444159626440725/-15rZya-frNtT3Og63EiZT_frfAWrgEtlfXDMujbBfKXqN96fwOmDuASu8x-S604fmcf'
    basic('Liyu0109', url)

def hand():
    url = 'https://discord.com/api/webhooks/966666502440878151/RmPzUaRKA2ONcDMgaUZWMf9Y9fTMeC4zHjaXmSe2ZdeCHHHsm33vuyiXPRs3KmhSVBX5'
    basic('homoto_akina',url)
def neko():
    url = 'https://discord.com/api/webhooks/967078779212165150/Ubzrv15z2YLS8l_TCrURSEKsE495WJ40wdJQyMYYnVW_UEF51Es9X56JPwybD6yKDj5z'
    basic('95rn16',url)


scheduler = BlockingScheduler()
scheduler.add_job(liyuu, 'interval', seconds=90)
scheduler.add_job(hand, 'interval', seconds=90)
scheduler.add_job(neko, 'interval', seconds=90)
scheduler.start()
                





