from sys import path
import search_setup
import search_engines
import args
import report

# Config section

GLOBAL_API_KEY = ""

google_API_KEY = ""
yandex_API_KEY = ""
bing_API_KEY = ""
duckduckgo_API_KEY = ""
baidu_API_KEY = ""

# Little hack to use multiple API keys or just one key

if GLOBAL_API_KEY != "":
  if google_API_KEY == "":
    google_API_KEY = GLOBAL_API_KEY
  if yandex_API_KEY == "":
    yandex_API_KEY = GLOBAL_API_KEY
  if bing_API_KEY == "":
    bing_API_KEY = GLOBAL_API_KEY
  if duckduckgo_API_KEY == "":
    duckduckgo_API_KEY = GLOBAL_API_KEY
  if baidu_API_KEY == "":
    baidu_API_KEY = GLOBAL_API_KEY

arguments = args.interactive_cli()

query_to_search = search_setup.arguments_to_search(
  arguments.global_query,
  arguments.google_query, 
  arguments.yandex_query,
  arguments.bing_query,
  arguments.duckduckgo_query,
  arguments.baidu_query)

search_setup.create_directory()

if query_to_search[0] != None:
  google_results  = search_engines.google_engine(query_to_search[0], google_API_KEY)
  report.report_generator(google_results, arguments.json)
if query_to_search[1] != None:
  yandex_results = search_engines.yandex_engine(query_to_search[1], yandex_API_KEY)
  report.report_generator(yandex_results, arguments.json)
if query_to_search[2] != None:
  bing_results = search_engines.bing_engine(query_to_search[2], bing_API_KEY)
  report.report_generator(bing_results, arguments.json)
if query_to_search[3] != None:
  duck_results = search_engines.duckduckgo_engine(query_to_search[3], duckduckgo_API_KEY)
  report.report_generator(duck_results, arguments.json)
if query_to_search[4] != None:
  baidu_results = search_engines.baidu_engine(query_to_search[4], baidu_API_KEY)
  report.report_generator(baidu_results, arguments.json)

