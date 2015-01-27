#coding:utf-8

import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

import os.path
import pickle
import webbrowser
import tweepy
from datetime import datetime

CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
TOKEN_FILE = 'tw4d.token'

access_token = dict()

def main():

  # OAuth認証
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

  # tokenの確認
  access_token = []
  if not os.path.exists(TOKEN_FILE):
    auth_url = auth.get_authorization_url()
    webbrowser.open(auth_url, new = 2)

    # PINコード入力
    verifier = raw_input('PIN:')

    # tokenの生成
    access_token = auth.get_access_token(verifier)
    with open(TOKEN_FILE, 'w') as f:
      pickle.dump(access_token, f)

  else:
    # tokenの読み込み
    with open(TOKEN_FILE, 'r') as f:
      access_token = pickle.load(f)

  auth.set_access_token(access_token[0], access_token[1])
  api = tweepy.API(auth)

  # Search
  tweets = api.search('cinema4d C4D', lang = 'ja')
  for tweet in tweets:
    print '[' + str(tweets.index(tweet)) + '] ----------------------------------------------------------------------------------------------- tw4d <<'
    print '>> ' + tweet.author.screen_name + ' <' + tweet.created_at.strftime('%Y-%m-%d %H:%M:%S') + '>'
    print tweet.text
    print ' '

if __name__ == '__main__':
  main()