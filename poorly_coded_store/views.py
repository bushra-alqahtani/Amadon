from django.shortcuts import redirect, render
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if request.method == 'POST':
        
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = float(request.POST["price"])
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        return redirect("/checkout/result")


def result(request):

    #to get the total price and total quantity
    allOrders=Order.objects.all() 
    total_quantity = 0
    total = 0
    for order in allOrders:
        total += order.total_price 
        total_quantity += order.quantity_ordered

    context ={
        'total': total,
        'total_quantity':total_quantity,

        'order': order,
        'ordersCount': len(allOrders)
    }

    return render(request, "store/checkout.html",context)

    



