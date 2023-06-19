from django.urls import path
from main.views import fetch_tweets, analyze_sentiment

urlpatterns = [
    path('tweets/<str:username>/', fetch_tweets, name='fetch_tweets'),
    path('sentiment-analysis/', analyze_sentiment, name='analyze_sentiment'),
]