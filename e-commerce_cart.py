def total_price(c):
    t = sum(c.values())
    if len(c) == 0:
        return "NA"
    else:
        if len(c) > 5:
            t = t * 0.9
            return t
    return t


cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
total = total_price(cart_items)
print(f"Total price: {total}")
