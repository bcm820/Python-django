from django.shortcuts import render, HttpResponse, redirect

def form(request):
    
    # Create cart and init order if new session
    if 'cart' not in request.session:
        request.session['cart'] = []
        request.session['total'] = 0
    
    # Create lists for each product
    request.session['tshirt'] = ["Dojo T-Shirt", 19.99]
    request.session['sweater'] = ["Dojo Sweater", 29.99]
    request.session['cup'] = ["Dojo Cup", 4.99]
    request.session['book'] = ["Algorithm Book", 49.99]
    
    # Create product catalog to display on page
    request.session['product_list'] = [
        {'id': 'tshirt', 'name': 'Dojo T-Shirt', 'price': 19.99},
        {'id': 'sweater', 'name': 'Dojo Sweater', 'price': 29.99},
        {'id': 'cup', 'name': 'Dojo Cup', 'price': 4.99},
        {'id': 'book', 'name': 'Dojo Book', 'price': 49.99}
    ]

    return render(request, "amadon/form.html")

def buy(request):

    # Pull cart from session, add items, and restore to display on page
    cart = request.session['cart']
    for key, val in request.POST.iteritems():
        if key != 'csrfmiddlewaretoken':
            if val > 0:
                cart.append(
                    {
                        'name': request.session[key][0],
                        'quantity': int(request.POST[key]),
                        'subtotal': request.session[key][1] * int(request.POST[key])
                    }
                )
    request.session['cart'] = cart

    # Add subtotals in cart to session total
    for item in request.session['cart']:
        request.session['total'] += item['subtotal']

    # Format to two decimal places for currency
    request.session['total'] = round(request.session['total'], 2)

    return redirect('/amadon/')

def checkout(request):

    # Empty cart and post order confirmation
    if 'checkout' in request.POST:
        if 'cart' in request.session:
            if request.session['total'] > 0:
                request.session['confirm'] = "Your order of ${} has been placed! Thank you!".format(request.session['total'])
                del request.session['cart']

    # Empty cart
    if 'clear' in request.POST:
        if 'cart' in request.session:
            del request.session['cart']
            del request.session['total']

    # End session
    if 'end' in request.POST:
        if 'confirm' in request.session:
            del request.session['confirm']
        if 'cart' in request.session:
            del request.session['cart']
            del request.session['total']

    return redirect('/amadon/')