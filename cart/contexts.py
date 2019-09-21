from django.shortcuts import get_object_or_404
from artefacts.models import Artefact

def cart_contents(request):
    """
    This makes sure that the contents of the cart
    are available when every page is rendered
    """

    cart = request.session.get('cart',{})
    cart_items = {}
    total = 0
    item_count = 0

    for id, quantity in cart.items():
        artefact = get_object_or_404(Artefact,pk=id)
        total += artefact.price
        item_count += 1
        cart_items.append({'id':id, 'quantity' : '1', 'artefact' : artefact})

    return {'cart_items' : cart_items, 'total' : total, 'item_count' : item_count}

