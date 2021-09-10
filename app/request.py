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
  get_sources_url = base_url.format(api_key) #maybe add category

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data) #converts json resp to python dict

    sources_results = None

    if get_sources_response['sources']:
      news_sources_list = get_sources_response['sources']
      sources_results = process_results(news_sources_list)
  
  return sources_results


def process_results(source_list):
  '''
  Function that processes the news results & turns them into a list of objs
  '''
  sources_results = [] #empty list
  for source_item in source_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')

    source_object = Source(id,name,description,url)
    sources_results.append(source_object)
  return sources_results

