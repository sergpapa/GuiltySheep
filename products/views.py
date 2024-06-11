from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Collection, Artist

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    collections = None
    artists = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'artist':
                collections = []
                sortkey = 'lower_collection_name'
                artists = Artist.objects.all()
                collection_lst = Collection.objects.filter(artist__name__in=artists)
                for collection in collection_lst:
                    collections.append(collection.name)
                products = products.annotate(lower_collection_name=Lower('collection__name'))
            elif sortkey == 'collection':
                sortkey = 'lower_collection_name'
                products = products.annotate(lower_collection_name=Lower('collection__name'))

            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'collection' in request.GET:
            collections = request.GET['collection'].split(',')
            products = products.filter(collection__name__in=collections)
            collections = Collection.objects.filter(name__in=collections)
        if 'artist' in request.GET:
            artists = request.GET['artist'].split(',')
            collection_lst = Collection.objects.filter(artist__name__in=artists)
            collections = []
            for collection in collection_lst:
                collections.append(collection.name)
            products = products.filter(collection__name__in=collections)
            artists = Artist.objects.filter(name__in=artists)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_collections' : collections,
        'current_artists' : artists,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    pass

def edit_product(request):
    pass


def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))