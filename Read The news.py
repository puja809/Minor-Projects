"""
                                Ready Top 10 News Daily for India
"""
from win32com.client import Dispatch
import requests
import json
speak = Dispatch("SAPI.spVoice")
speak.Speak("You must listen to news everyday")
url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=9eefb3cf88ac4736aa182ba55d1de15e"
news = requests.get(url).text
# print(news)
data_dict = json.loads(news)
# print(data_dict["articles"])
arts = data_dict['articles']
# print((data[0]))
# print(len(arts))
i = 1
for i, articles in enumerate(arts):

    speak.Speak(articles['title'])

    i = i + 1

    if i == len(arts):
        speak.Speak("Thanks for listening")
    else:
        speak.Speak("Moving to next news")
speak.Speak("Come again tomorrow")


