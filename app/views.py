from .request import get_sources

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    sources = get_sources()
    title = 'Headline News'
    print (sources)

    return render_template('index.html', title=title, sources=sources)

