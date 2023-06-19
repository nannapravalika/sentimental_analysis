from django.shortcuts import render
import twitter
import nltk
from django.http import JsonResponse
from nltk.sentiment import SentimentIntensityAnalyzer

api = twitter.Api(consumer_key='hGJSH9Y7mIM7Nu7wdXGleVlTw',
                  consumer_secret='i7CubeFDSNuchZ4Xr56LR0sERQdBm8C54CE4o8Onw3b0FyjcFr',
                  access_token_key='1256147195616563200-kKRKnm45ayh29p1RAl1VvdAMCMNahN',
                  access_token_secret='FJUgUaQC5d2BKysrORdPwbwCRDpcrZrKlX4VqUOH0rj47')

sia = SentimentIntensityAnalyzer()

def fetch_tweets(request, username):
    try:
        tweets = api.GetUserTimeline(screen_name=username, count=10)
        tweet_data = [{'text': tweet.text, 'created_at': tweet.created_at} for tweet in tweets]
        return JsonResponse(tweet_data, safe=False)
    except twitter.error.TwitterError as e:
        return JsonResponse({'message': str(e)}, status=400)

def analyze_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        sentiment_score = sia.polarity_scores(text)
        return JsonResponse({'text': text, 'sentiment_score': sentiment_score})
    return JsonResponse({'message': 'Invalid request.'}, status=400)

nltk.download()