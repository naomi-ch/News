from flask import render_template #request,redirect,url_for
from . import main
from ..request import get_sources
#from ..models import Source 
#from forms import 

#Source
@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  sources = get_sources()
  title = 'Home - Welcome to the most accessible News site'
  return render_template('index.html', title = title, sources = sources)