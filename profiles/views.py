from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core import serializers
from django.contrib.auth.models import User
import json
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from products.models import Review
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
        orders = profile.orders.all()

        if  request.user.is_superuser:
            data = Review.objects.all()
        else:
            data = Review.objects.filter(user=request.user)
        reviews_json = serializers.serialize('json', data)
        
        reviews = json.loads(reviews_json)

    for review in reviews:
        user =  User.objects.filter(pk=review['fields']['user']).first()
        review['fields']['user'] = user.username

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'reviews' : reviews,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)   