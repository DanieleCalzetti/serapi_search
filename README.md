# Search through SERAPI

This tool will use SERAPI API to search a query inside google, yandex, bing, duckduckgo, baidu.

## Contribuitors

[Daniele Calzetti](https://www.linkedin.com/in/daniele-calzetti/)

[P0lif3m0](https://twitter.com/P0lif3m0)

## TODO

- Create an html file with custom results

## Disclaimer

Currently SERPapi saves a copy of the results in their server and retain them for 30 days. 
There isn't a way to delete the results but hopefully they will be implemented in the next future.
Neverthless this little experiment will keep going. ;)

## Execution of the tool

### Download the tool

    git clone https://github.com/DanieleCalzetti/serapi_search.git
    cd serapi_search

### Setup up

Register for an API Key at https://serpapi.com/pricing (the free plan gives 100queries/month)

Open main.py and set the variable GLOBAL_API_KEY equal to the api_key

    GLOBAL_API_KEY = "change me"

Or it is possible to set an API key for each search engine

    google_API_KEY = "change me"
    yandex_API_KEY = "change me"
    bing_API_KEY = "change me"
    duckduckgo_API_KEY = "change me"
    baidu_API_KEY = "change me"

If the above variable are lefted empty but it is provided a GLOBAL_API_KEY, the tool will set the variable equal to GLOBAL_API_KEY.

### Execution tool

#### Creation virtual env

    python3 -m venv /path/to/new/virtual/environment

#### Activation virtual env

    /path/to/new/virtual/environment/Scripts/activate

#### Install google-search-results

    pip install google-search-results

#### Print help

    python main.py -h

#### Flags to use

    python main.py -gl <query to search> --> search the query on all the engines
    python main.py -g <query to search> --> search only in google
    python main.py -y <query to search> --> search only in yandex
    python main.py -bg <query to search> --> search only in bing
    python main.py -d <query to search> --> search only in duckduckgo
    python main.py -ba <query to search> --> search only in baidu

    python main.py -ba <query to search> -g <query to search> -gl <query to search> --> search in bing and google the given query and on the other search engines the query passed via gl

