from django.shortcuts import render
from library.models import *
from api.serializers import *

# Create your views here.
def index(req):
    return render(req, 'index.html')
