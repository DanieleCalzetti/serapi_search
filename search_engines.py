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
  return google_search

def yandex_engine(yandex_query, yandex_API_KEY):
  params = {
    "engine": "yandex",
    "text": yandex_query,
    "p": "10",
    "no_cache": "true",
    "api_key": yandex_API_KEY
    }
    
  yandex_search = GoogleSearch(params)
  return yandex_search

def bing_engine(bing_query, bing_API_KEY):
  params = {
    "engine": "bing",
    "q": bing_query,
    "first": "10",
    "count": "100",
    "api_key": bing_API_KEY
  }

  bing_search = GoogleSearch(params)
  return bing_search

def duckduckgo_engine(duckduckgo_query, duckduckgo_API_KEY):
  params = {
    "engine": "duckduckgo",
    "q": duckduckgo_query,
    "no_cache": "true",
    "api_key": duckduckgo_API_KEY
  }

  duck_search = GoogleSearch(params)
  return duck_search    

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
  return baidu_search
