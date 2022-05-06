from app import app
import urllib.request,json
from .models import Sources


Source = source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["http://newsapi.org/v2/sources?&apiKey={}"]



def get_sources():
    """
    Function that gets the json response to our url request
    """
    get_sources_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None
#check if response has data
        if get_sources_response['results']:
            source_results_list = get_sources_response['results']
            source_results = process_results(source_results_list)
#return a list of source objects
    return source_results


def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []  
    # to store our newly created source objects
    for sources_item in source_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')

        source_object = Sources(id, name, description, url, category, language)
        source_results.append(source_object)
    return source_results
