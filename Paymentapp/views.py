from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt

from .models import Coffee
import json
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        # mobile = request.POST.get('mobile')
        # email = request.POST.get('email')
        amount = int(request.POST.get('amount')) * 100
        client = razorpay.Client(auth =("rzp_test_JSEvpJyaEVuJ8Q" , "KrkzC9t5UO8Vf7jIdNjJtom9"))
        payment = client.order.create({'amount':amount, 'currency':'INR',
                              'payment_capture':'1' })  
        coffee = Coffee(name = name , amount =amount , payment_id = payment['id'])
        # coffee = Coffee(name = name , amount =amount , mobile = mobile, email = email , payment_id = payment['id'])
       
        coffee.save()
        return render(request, 'index.html' ,{'payment':payment})
    return render(request, 'index.html')


@csrf_exempt
def success(request):
    if request.method == "POST":
        a =  (request.POST)
        payment_id = ""
        for key , val in a.items():   
            if key == "razorpay_order_id":
                payment_id = val
                break
        user = Coffee.objects.filter(payment_id = payment_id).first()
        user.paid = True
        user.save()
    return render(request, "success.html")