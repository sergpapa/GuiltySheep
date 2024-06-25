from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core import serializers
import json
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Collection, Artist, Review
from django.contrib.auth.models import User
from .forms import ProductForm, ReviewForm

# Create your views here.
def new_rating(product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)

    initial_rating = product.rating
    print(initial_rating)
    review_count = reviews.count()
    if review_count <= 1 :
        review_count = 2
    reviews_sum = 0

    for review in reviews:
        old_rating = review.rating
        reviews_sum += old_rating

    new_avg_rating = (initial_rating + reviews_sum) / review_count

    print(new_avg_rating, 'avg')

    formatted_new_rating = '{0:.2f}'.format(new_avg_rating)
    product.rating = Decimal(formatted_new_rating)
    product.save()

    print(product.rating)

    return "Ratings updated successfully"


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
    data = Review.objects.filter(product=product)
    reviews_json = serializers.serialize('json', data)

    on_wishlist_page = request.session.pop('from_wishlist', False)
    
    reviews = json.loads(reviews_json)

    for review in reviews:
        user =  User.objects.filter(pk=review['fields']['user']).first()
        review['fields']['user'] = user.username

    context = {
        'product': product,
        'reviews' : reviews,
        'on_wishlist_page' : on_wishlist_page
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

        template = 'products/edit_product.html'
        context = {
            'form': form,
            'product': product,
        }

        return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))



@login_required
def add_review(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  
            review.product = product
            review.save()

            new_rating(product_id)

            messages.success(request, f'Review for {product.name} added successfully!')

            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()
    

    template = 'products/add_review.html'
    context = {
        'form': form,
        'product': product,
        'on_review_page' : True
    }

    return render(request, template, context)
    

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    product = get_object_or_404(Product, pk=review.product.id)

    if request.method == 'POST':

        if not request.user == review.user:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('product_detail'))

        form = ReviewForm(request.POST, request.FILES, instance=review)

        if form.is_valid():
            review = form.save()

            new_rating(product.pk)

            print(new_rating)

            messages.success(request, f'Review for {product.name} updated successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
    
    template = 'products/edit_review.html'
    context = {
        'form': form,
        'product': product,
        'review' : review,
        'on_review_page' : True
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    product_id = product.pk

    if not request.user == review.user:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('product_detail'))
    else:
        review.delete()

        messages.success(request, 'Review deleted!')
        return redirect(reverse('product_detail', args=[product_id]))