from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib import messages
from store.models import Products,Cart,Order,OrderItem


import random

def index(request):
    rawcart=Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty>item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cartitems:
        total_price+=item.product.selling_price*item.product_qty

    context={'cartitems':cartitems,'total_price':total_price}
    return render(request,'store/checkout.html',context)


def placeorder(request):
    if request.method=='POST':
        neworder=Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('fname')
        neworder.lname=request.POST.get('lname')
        neworder.email=request.POST.get('email')
        neworder.phone=request.POST.get('phone')
        neworder.address=request.POST.get('address')
        neworder.city=request.POST.get('city')
        neworder.state=request.POST.get('state')
        neworder.country=request.POST.get('country')
        neworder.pincode=request.POST.get('pincode')
        neworder.pincode=request.POST.get('pincode')
        neworder.pincode=request.POST.get('pincode')
        neworder.payment_mode=request.POST.get('payment_mode')

        cartitems=Cart.objects.filter(user=request.user)
        total_price=0
        for item in cartitems:
            total_price+=item.product.selling_price*item.product_qty
        
        neworder.total_price=total_price
        trackno='mani'+str(random.randint(111111111, 999999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno='mani'+str(random.randint(111111111, 999999999))
        neworder.tracking_no=trackno
        neworder.save()


        neworderitems=Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )


            #To decrease the product quantity from available stock
            orderproduct=Products.objects.filter(id=item.product_id).first()
            orderproduct.quantity=orderproduct.quantity-item.product_qty
            orderproduct.save()

        # To clear the users cart
        Cart.objects.filter(user=request.user).delete()
        messages.success(request, "Your order has been placed successfully!")

    return redirect('/')
    
    