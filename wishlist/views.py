# Contains Code Institute Provided Code

from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.
def view_wishlist(request):

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    product_id = product.pk
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        wishlist.pop(item_id)
        messages.success(request, f'Removed {product.name} from your wishlist')
    else:
        wishlist[item_id] = {'item_id': item_id}
        messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist
    request.session['from_wishlist'] = True

    return redirect(reverse('product_detail', args=[product_id]))


def add_wishlist_item_to_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    size = request.POST['product_size']

    print(request.POST)
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if size in bag[item_id]['items_by_size'].keys():
            bag[item_id]['items_by_size'][size] += quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        bag[item_id] = {'items_by_size': {size: quantity}}
        messages.success(request, f'Added size {size.upper()} {product.name} to your bag')

    request.session['bag'] = bag

    context = {
        'on_wishlist_page' : True,
    }

    return redirect(redirect_url, context)


def remove_from_wishlist(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        wishlist = request.session.get('wishlist', {})

        wishlist.pop(item_id)
        messages.success(request, f'Removed {product.name} from your wishlist')
       

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

