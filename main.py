"""
Tool to query google, yandex, bing, baidu and duckduckgo via API mantained by SERAPI.
https://serpapi.com/
"""

import sys
import search_setup
import search_engines
import args
import report

__author__ = "Daniele Calzetti and P0lif3m0"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Daniele Calzetti", "P0lif3m0"]
__license__ = "GNU GPLv3"
__maintainer__ = "Daniele Calzetti"

# Config section

global_api_key = ""

google_api_key = ""
yandex_api_key = ""
bing_api_key = ""
duckduckgo_api_key = ""
baidu_api_key = ""

# Little hack to use multiple API keys or just one key

if global_api_key != "":
  if google_api_key == "":
    google_api_key = global_api_key
  if yandex_api_key == "":
    yandex_api_key = global_api_key
  if bing_api_key == "":
    bing_api_key = global_api_key
  if duckduckgo_api_key == "":
    duckduckgo_api_key = global_api_key
  if baidu_api_key == "":
    baidu_api_key = global_api_key

if google_api_key == "" and yandex_api_key == "" and bing_api_key == "" and duckduckgo_api_key == "" and baidu_api_key == "":
  sys.exit("Define at least an api key")

arguments = args.interactive_cli()

query_to_search = search_setup.arguments_to_search(
  arguments.global_query,
  arguments.google_query,
  arguments.yandex_query,
  arguments.bing_query,
  arguments.duckduckgo_query,
  arguments.baidu_query)

search_setup.create_directory()

if query_to_search[0] != None and google_api_key != "":
  google_results  = search_engines.google_engine(query_to_search[0], google_api_key)
  report.report_generator(google_results, arguments.json)

if query_to_search[1] != None and yandex_api_key != "":
  yandex_results = search_engines.yandex_engine(query_to_search[1], yandex_api_key)
  report.report_generator(yandex_results, arguments.json)

if query_to_search[2] != None and bing_api_key != "":
  bing_results = search_engines.bing_engine(query_to_search[2], bing_api_key)
  report.report_generator(bing_results, arguments.json)

if query_to_search[3] != None and duckduckgo_api_key != "":
  duck_results = search_engines.duckduckgo_engine(query_to_search[3], duckduckgo_api_key)
  report.report_generator(duck_results, arguments.json)

if query_to_search[4] != None and baidu_api_key != "":
  baidu_results = search_engines.baidu_engine(query_to_search[4], baidu_api_key)
  report.report_generator(baidu_results, arguments.json)