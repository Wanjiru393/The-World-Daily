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
