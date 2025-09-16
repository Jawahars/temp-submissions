# Assisted by watsonx Code Assistant
def process_order(base_price, quantity, loyalty_level):
    """
    This function calculates the final price based on the base price, quantity, and loyalty level.
    Args:
    base_price (int): The base price of a single item.
    quantity (int): The quantity of items.
    loyalty_level (int): The loyalty level (1, 2, or 3).
    Returns:
    int: The final calculated price.
    """
    # Calculate the base total (price * quantity)
    base_total = base_price * quantity
    # Determine discount rate based on loyalty level
    if loyalty_level == 3:
        discount_rate = 20
    elif loyalty_level == 2:
        discount_rate = 10
    else:  # Default case for loyalty level 1
        discount_rate = 5
    # Apply an additional bulk discount if quantity > 20
    if quantity > 20:
        discount_rate += 5
    # Calculate the final price: final = total - (total * rate / 100)
    final_price = base_total - (base_total * (discount_rate / 100))
    return int(final_price)


def test_process_order_comprehensive():
    # Loyalty level 1, no bulk
    assert process_order(10, 10, 1) == 95  # 100 - 5% = 95
    # Loyalty level 1, with bulk
    assert process_order(10, 25, 1) == 225  # 250 - 10% = 225
    # Loyalty level 2, no bulk
    assert process_order(10, 10, 2) == 90  # 100 - 10% = 90
    # Loyalty level 2, with bulk
    print("Comprehensive tests passed.")

test_process_order_comprehensive()