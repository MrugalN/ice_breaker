import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()


twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
)


def scrape_user_tweets(username, num_tweets=5, mock: bool = True):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """
    tweet_list = []

    if mock:
        Mrugal_TWITTER_GIST = "https://gist.githubusercontent.com/MrugalN/188e6a915d61f6e441f84899d2c3a898/raw/a6045ea89a1dd8bb8729782fc25a9c81ea8b8cb7/mrugal-nikhar%2520twitter%2520data"
        user_data = requests.get(Mrugal_TWITTER_GIST, timeout=5).json()

    else:
        user_response = twitter_client.get_user(
            username=username,
            user_field=[
                "created_at",
                "description",
                "entities",
                "id",
                "location",
                "name",
                "public_metrics",
                "url",
            ],
        )
        user_data = user_response.data

    user_details = {
        "id": user_data["id"],
        "name": user_data["name"],
        "username": user_data["username"],
        "created_at": user_data["created_at"],
        "description": user_data["description"],
        "location": user_data["location"],
        "followers_count": user_data["public_metrics"]["followers_count"],
        "following_count": user_data["public_metrics"]["following_count"],
        "tweet_count": user_data["public_metrics"]["tweet_count"],
    }

    return user_details


if __name__ == "__main__":

    tweets = scrape_user_tweets(username="mrugal08", mock=False)
    print(tweets)
