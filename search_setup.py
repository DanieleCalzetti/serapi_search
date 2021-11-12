from time import gmtime, strftime
import os


def create_directory():
  date_time = strftime("%Y_%m_%d_%H%M%S", gmtime())
  mypath = "".join(["results_", date_time])
  os.makedirs(mypath)
  os.chdir(mypath)


def arguments_to_search(global_query, google_query, yandex_query, bing_query, duckduckgo_query, baidu_query):
  if global_query != None:
    if google_query == None:
      google_query = global_query
    if yandex_query == None: 
      yandex_query = global_query
    if bing_query == None:
      bing_query = global_query
    if duckduckgo_query == None:
      duckduckgo_query = global_query
    if baidu_query == None:
      baidu_query = global_query
    return google_query, yandex_query, bing_query, duckduckgo_query, baidu_query
  else:
    return google_query, yandex_query, bing_query, duckduckgo_query, baidu_query

  

