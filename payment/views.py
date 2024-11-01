from sslcommerz_lib import SSLCOMMERZ
import random, string
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Function to generate a unique transaction ID
def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
@csrf_exempt
# Payment initiation view
def payment(request):
    settings = { 
        'store_id': 'foysa671dabfd11ca2', 
        'store_pass': 'foysa671dabfd11ca2@ssl', 
        'issandbox': True 
    }
    sslcz = SSLCOMMERZ(settings)
    
    transaction_id = unique_transaction_id_generator()
    post_body = {
        'total_amount': 5600.26,
        'currency': "BDT",
        'tran_id': transaction_id,
        'success_url': request.build_absolute_uri(reverse('payment_success', args=[transaction_id])),
        'fail_url': request.build_absolute_uri(reverse('payment_fail')),
        'cancel_url': request.build_absolute_uri(reverse('payment_cancel')),
        'emi_option': 0,
        'cus_name': "test",
        'cus_email': "test@test.com",
        'cus_phone': "01700000000",
        'cus_add1': "Cantonment",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "",
        'num_of_item': 1,
        'product_name': "Test",
        'product_category': "Test Category",
        'product_profile': "general"
    }

    response = sslcz.createSession(post_body)
    
    if response['status'] == 'SUCCESS':
        return HttpResponseRedirect(response['GatewayPageURL'])
    else:
        return HttpResponse("Payment initiation failed. Please try again later.")

# Success view
@csrf_exempt
def payment_success(request, transaction_id):
    context = {'transaction_id': transaction_id}
    return render(request, 'payment_success.html', context)

# Failure view
@csrf_exempt
def payment_fail(request):
    return HttpResponse("Payment failed. Please try again.")

# Cancel view
@csrf_exempt
def payment_cancel(request):
    return HttpResponse("Payment was cancelled.")