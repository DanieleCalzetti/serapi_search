from serpapi import GoogleSearch
import json

def google_engine(google_query, google_API_KEY):
  params = {
    "engine": "google",
    "q": google_query,
    "google_domain": "google.com",
    "hl": "en",
    "lr": "lang_it|lang_en",
    "filter": "0",
    "start": "100",
    "num": "100",
    "api_key": google_API_KEY
  }

  google_search = GoogleSearch(params)
  json_google = google_search.get_json()
  
  with open("google.json", "w") as file:
    json.dump(json_google, file)			


def yandex_engine(yandex_query, yandex_API_KEY):
  params = {
    "engine": "yandex",
    "text": yandex_query,
    "p": "10",
    "no_cache": "true",
    "api_key": yandex_API_KEY
    }
    
  yandex_search = GoogleSearch(params)
  json_resultsY = yandex_search.get_json()
  
  with open("yandex.json", "w") as file:
    json.dump(json_resultsY, file)			


def bing_engine(bing_query, bing_API_KEY):
  params = {
    "engine": "bing",
    "q": bing_query,
    "first": "10",
    "count": "100",
    "api_key": bing_API_KEY
  }

  bing_search = GoogleSearch(params)
  json_bing = bing_search.get_json()

  with open("bing.json", "w") as file:
      json.dump(json_bing, file)			


def duckduckgo_engine(duckduckgo_query, duckduckgo_API_KEY):
  params = {
    "engine": "duckduckgo",
    "q": duckduckgo_query,
    "no_cache": "true",
    "api_key": duckduckgo_API_KEY
  }

  duck_search = GoogleSearch(params)
  json_ddgo = duck_search.get_json()

  with open("duckduckgo.json", "w") as file:
      json.dump(json_ddgo, file)			
    

def baidu_engine(baidu_query, baidu_API_KEY):
  params = {
    "engine": "baidu",
    "q": baidu_query,
    "pn": "10",
    "rn": "100",
    "no_cache": "true",
    "api_key": baidu_API_KEY
  }

  baidu_search = GoogleSearch(params)
  json_baidu = baidu_search.get_json()

  with open("baidu.json", "w") as file:
      json.dump(json_baidu, file)			#crea un file: .json