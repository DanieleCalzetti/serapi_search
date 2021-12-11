import argparse
import sys

def interactive_cli():
  parser_serapi = argparse.ArgumentParser(description='Tool to query multiple search engine')
  parser_serapi.add_argument('-gl','--global_query',
                      action="store",
                      help='Search on all the search engine')
  parser_serapi.add_argument('-g','--google_query',
                      action="store",
                      help='Search only in google')
  parser_serapi.add_argument('-y','--yandex_query',
                      action="store",
                      help='Search only in yandex')
  parser_serapi.add_argument('-bg','--bing_query',
                      action="store",
                      help='Search only in bing')
  parser_serapi.add_argument('-d','--duckduckgo_query',
                      action="store",
                      help='Search only in duckduckgo')
  parser_serapi.add_argument('-ba','--baidu_query',
                      action="store",
                      help='Search only in baidu')
  parser_serapi.add_argument('-js', '--json',
                      action='store_true',
                      help='Use this flag to generate a file json')
  if len(sys.argv)==1:
    parser_serapi.print_help()
    parser_serapi.exit()
  args = parser_serapi.parse_args()
  return args