import requests
from django.shortcuts import render
import random


def home(request):
  response = requests.get(
      "https://uselessfacts.jsph.pl/random.json?language=en")
  data = response.json()
  fact = data["text"]
  source = data["source_url"]

  response2 = requests.get("https://zenquotes.io/api/random").json()
  quote = response2[0]["q"]
  author = response2[0]["a"]
  end = response2[0]["h"]

  response3 = requests.get(
      "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=explicit&type=single"
  ).json()
  joke = response3["joke"]

  num= random.randint(0,2)
  respose4 = requests.get(
      "https://api.thenewsapi.com/v1/news/top?api_token=c7TdqXFPWgkgatSsRi2WBSDqrw5Q35Ng5CiOsJaB&language=en&locale=us&limit=3&categories=politics"
  ).json()
  news_title = respose4["data"][num]["title"]
  news_description = respose4["data"][num]["description"]
  news_url = respose4["data"][num]["url"]
  news_image = respose4["data"][num]["image_url"]
  news_source = respose4["data"][num]["source"]

  response5 = requests.get("https://api.thecatapi.com/v1/images/search").json()
  url = response5[0]["url"]
  response6 = requests.get("https://meowfacts.herokuapp.com/").json()
  cat_facts = response6["data"][0]

  response
  return render(
      request, 'templates/home.html', {
          'fact': fact,
          'source': source,
          'joke': joke,
          'quote': quote,
          'author': author,
          'end': end,
          'url': url,
          'cat_facts': cat_facts,
          'news_title': news_title,
          'news_description': news_description,
          'news_url': news_url,
          'news_image': news_image,
          'news_source': news_source
      })
