from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages
#models and forms
from Order_Application.models import Order, Cart
from Payment_Application.forms import BillingAddress
from Payment_Application.forms import BillingForm


from django.contrib.auth.decorators import login_required
from random import randint



# Create your views here.
@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    print(saved_address)
    form = BillingForm(instance=saved_address)
    if request.method == "POST":
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request, f"Shipping Address Saved!")
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    #print(order_qs)
    order_items = order_qs[0].orderitems.all()
    #print(order_items)
    order_total = order_qs[0].get_totals()
    return render(request, 'Payment_Application/checkout.html', context={"form":form, "order_items":order_items, "order_total":order_total, "saved_address":saved_address})


@login_required
def payment(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    if not saved_address.is_fully_filled():
        messages.info(request, f"Please complete shipping address!")
        return redirect("Payment_Application:checkout")

    if not request.user.profile.is_fully_filled():
        messages.info(request, f"Please complete profile details!")
        return redirect("Login_Application:profile")

    return redirect("Payment_Application:paymentform")

@login_required
def paymentform(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    #print(order_qs)
    order_items = order_qs[0].orderitems.all()
    #print(order_items)
    order_total = order_qs[0].get_totals()
    return render(request, 'Payment_Application/paymentform.html', context={"order_items":order_items, "order_total":order_total, "saved_address":saved_address})

@login_required
def complete(request):
    if request.method == 'POST' or request.method == 'post':

        tran = randint(100, 999)
        tran_id = 'Trx'+ str(tran)
        val = randint(100, 999)
        val_id = 'Od'+ str(val)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        order = order_qs[0]
        orderId = tran_id
        order.ordered = True
        order.orderId = orderId
        order.paymentId = val_id
        order.save()
        cart_items = Cart.objects.filter(user=request.user, purchased=False)
        for item in cart_items:
            item.purchased = True
            item.save()
        messages.info(request, f"Your payment is made.")
        return HttpResponseRedirect(reverse("Shop_Application:home"))
    else:
        messages.info(request, f"Your payment is not complete.")


@login_required
def order_view(request):
    try:
        orders = Order.objects.filter(user=request.user, ordered=True)
        context = {"orders": orders}
    except:
        messages.warning(request, "You do no have an active order")
        return redired("Shop_Application:home")
    return render(request, "Payment_Application/order.html", context)

