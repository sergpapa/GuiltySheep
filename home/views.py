# Contains Code Institute Provided Code
from django.shortcuts import render
from products.models import Collection

# Create your views here.
def index(request):
    """ A view to return home url """
    collections = Collection.objects.all()

    context = {
        'collections' : collections
    }
    
    return render(request, 'home/index.html', context)
