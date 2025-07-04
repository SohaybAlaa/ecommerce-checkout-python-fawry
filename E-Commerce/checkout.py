from shipping_service import ShippingService

def checkout(customer, cart):
    if cart.is_empty():
        raise Exception("Cart is empty.")

    subtotal = 0
    shipping_fee = 0
    shippables = []

    for item in cart.items:
        product = item.product
        quantity = item.quantity

        if product.quantity < quantity:
            raise Exception(f"Product {product.name} is out of stock.")
        if product.is_expired():
            raise Exception(f"Product {product.name} is expired.")

        subtotal += product.price * quantity
        if product.is_shippable():
            shipping_fee += 10
            shippables.append({'product': product, 'quantity': quantity})

    total = subtotal + shipping_fee
    if customer.balance < total:
        raise Exception("Insufficient balance.")

    for item in cart.items:
        item.product.quantity -= item.quantity

    customer.balance -= total

    if shippables:
        ShippingService.ship_items(shippables)

    print("** Checkout receipt **")
    for item in cart.items:
        print(f"{item.quantity}x {item.product.name} {item.product.price * item.quantity}")
    print("----------------------")
    print(f"Subtotal {subtotal}")
    print(f"Shipping {shipping_fee}")
    print(f"Amount {total}")
    print(f"Balance after payment: {customer.balance}")