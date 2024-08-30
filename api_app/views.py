from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from api_project import settings
import stripe

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    items = Item.objects.all()  # Fetch all items or apply any filters
    context = {
        'title': 'Home',
        'items': items,
    }
    return render(request, 'index.html', context=context)


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),  # Stripe требует сумму в центах
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://yourdomain.com/success/',
        cancel_url='https://yourdomain.com/cancel/',
    )
    return JsonResponse({'sessionId': session.id})


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'item_detail.html', {
        'item': item,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })
