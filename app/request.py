import urllib.request,json
from .models import Source

#Getting API Key
api_key = None

#Getting News Base URL
base_url = None

def configure_request(app):
  global api_key,base_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']


def get_sources(): #maybe have one where you can search by category
  '''
  Function that gets the json response to our url request
  '''
  get_news_url = base_url.format(api_key) #maybe add category

  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data) #converts json resp to python dict

    news_results = None

    if get_news_response['sources']:
      news_sources_list = get_news_response['sources']
      news_results = process_results(news_sources_list)
  
  return news_results


def process_results(source_list):
  '''
  Function that processes the news results & turns them into a list of objs
  '''
  source_results = [] #empty list
  for source_item in source_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')

    source_object = Source(id,name,description,url)
    source_results.append(source_object)
  return source_results

