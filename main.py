#importing library calls tweepy
import tweepy as tw

#credentials
import credentials.credentials as cr

#API - with twitter keys
auth = tw.OAuthHandler(cr.consumer_secret(), cr.consumer_secret())
auth.set_access_token(cr.acess_token_key(), cr.acess_token_secret())

api = tw.API(auth)