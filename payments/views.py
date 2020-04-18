import stripe
from django.shortcuts import render
from django.conf import settings
from shopping_cart.views import get_user_pending_order  

from django.views.generic.base import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY


class checkout(TemplateView):
    template_name = 'payments/checkout.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

    



def charge(request): 
    existing_order = get_user_pending_order(request)
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=existing_order.get_cart_total(),
            currency='inr',
            description='A Django charge',
            source=request.POST['stripeToken']
        )

        
        return render(request, 'payments/payment_done.html')



def final_total(request):
    existing_order = get_user_pending_order(request)
    context = {
        'total': existing_order
    }
    return render(request, 'payments/checkout.html', context)
